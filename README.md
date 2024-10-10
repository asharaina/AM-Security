# AM-Security 
(Final Project for Harvard CS50)
#### Video Demo:  https://www.youtube.com/watch?v=95u3_TB2jFE
#### Description:
In this project, I create a web-based security system based on face-recognition software.
The web-app opens to the main page (index.html) where the webcam opens and captures the image of the person once the grey central button is clicked. A pre-trained Face Recognition software module compares the captured image to the set of labeled images in the photos folder. If the faces are a match, the result.html takes the name from the photo and prints that out on the web page. If not, it prints out 'Unknown Person' on the page. Every entry is automatically recorded to the CSV file (entry-exit-log). The result.html page also has two separate links with options of going back to the main page and downloading the CSV file.

I had thought of this idea during the Covid pandemic, when I was wondering how to create a smart, automatic security/attendance system that can operate without any human touch, unless necessary. While it is true that this system is common in many high security facilities in the US, it is not mainstream in Bangladesh, where security systems are entirely manual in most cases. Therefore, I had hoped that this idea could help popularize contact-less, automated security systems.
Initially I wanted to make a web app that connects with two webcams (facing two different directions - one for entry and the other for the exit). I was successfully able to write the code for that, but since my machine (where I was running, testing, debugging, etc.) only has one camera (and I was not able to install a new one in time of completing this project), I restructured the code to be based on a single-camera.
My future plan with this project is to get a new webcam and install it on my machine to update my app to be able to take live video input from both cameras. Furthermore, I plan on adding a register and login feature to the app to enable more personalized experience. Finally, if I can successfully add these features, I hope to turn it into a downloadable desktop and/or android app.

Below are the details of the different files and folders of the app:

app.py

The backend is built entirely on Flask, through the app.py file. Not only does the Flask framework connect directly with the course curriculum covered, but it is a very useful way to integrate the Python-based face-recognition packages and other ML-libraries into the website. The ML-libraries I used include pandas,open-cv (although to be more precise, open-cv is a computer vision software library, like face_recognition - which I also used here). Apart from this, I used the os package for interacting with the local machine to create folder directories and CSV file to input the entry-exit information and datetime package to automatically detect and note the time according to the local server. 
Face_recognition module did the main face detection and recognition, whereas open-cv is needed for accessing the camera (in this app, I have to add. Open-cv does contain other computer vision and image processing tools, but I did not use them here). It contains a special software comprising deep learning-based face identification algorithm from Dlib.

Static
This folder contains the all-important entry-exit-log.csv file, and two folders - captures and photos. Photos contain the labled .jpg images that are used to match the live-stream from the webcam. Currently, it contains pictures of President Obama, Linus Torvalds, Sundar Pichai, etc.

Templates
This folder contains the index.html and results.html files. For now, these pages are simply built and designed, but I plan on adding further elements in the future. The index.html file contains a link to download the CSV file and above it, the button to activate the camera and detect the face. Open-cv and Face_recognition run after the button is clicked and compare the face in front of the webcam to the photos in the photos folder. If there is a match, then the identity of the person is verified and the name of the person is displayed on results.html page. If a matching image is not present, then ‘Unknown Person’ is displayed. These are appended to the .csv file automatically. A downloadable link of the CSV file is also found on the results.html page, along with a link to go back to the main page (index.html).
