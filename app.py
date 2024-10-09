import os
import cv2
import face_recognition
import pandas as pd
from flask import Flask, render_template, request, redirect, send_file
from datetime import datetime

app = Flask(__name__)

# Paths to store images and CSV files
PHOTO_FOLDER = "static/photos/"
CAPTURE_FOLDER = "static/captures/"
CSV_FILE = "static/entry-exit-log.csv"

# Ensure directories exist
os.makedirs(PHOTO_FOLDER, exist_ok=True)
os.makedirs(CAPTURE_FOLDER, exist_ok=True)

# Create or initialize the CSV file
if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=["Name", "Status", "Date", "Time"])
    df.to_csv(CSV_FILE, index=False)

def capture_image(filename):

    cap = cv2.VideoCapture(0)
       
    while True:
        ret, frame = cap.read()
        cv2.imshow('Camera', frame)
        img_path = os.path.join(CAPTURE_FOLDER, filename)
        cv2.imwrite(img_path, frame)
        return img_path
    
    cap.release()
        


def compare_faces(captured_img_path, known_images_folder):
    captured_image = face_recognition.load_image_file(captured_img_path)
    captured_encoding = face_recognition.face_encodings(captured_image)

    if len(captured_encoding) == 0:
        return None  # No face found in captured image

    for img_file in os.listdir(known_images_folder):
        known_img_path = os.path.join(known_images_folder, img_file)
        known_image = face_recognition.load_image_file(known_img_path)
        known_encoding = face_recognition.face_encodings(known_image)

        if len(known_encoding) > 0 and face_recognition.compare_faces([known_encoding[0]], captured_encoding[0])[0]:
            return os.path.splitext(img_file)[0]  # Return name without file extension

    return None

@app.route('/capture', methods=['POST'])
def capture():
    
    cam1_path = capture_image("cam1.jpg")
    
    # Check if faces match with photos in the folder
    
    # Get current date and time
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    # Update the CSV file
  
    person = compare_faces(cam1_path, PHOTO_FOLDER)
    status = "Entry Identity Verified" if person else "Unknown Person"
    df = pd.read_csv(CSV_FILE)
    new_row = pd.DataFrame([{"Name": person or "Unknown", "Status": status, "Date": date, "Time": time}])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(CSV_FILE, index=False)

    
    return render_template('result.html', person=person, status=status)

@app.route('/download-csv', methods=['GET'])
def download_csv():
    return send_file(CSV_FILE, as_attachment=True)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

    

