YOLOv8 Real-Time Object Detection Web Application
Project Overview
This repository contains a web application for real-time object detection using the YOLOv8 model. The app is built with Streamlit and demonstrates how to process live video streams, visualize detection in real time, and save detection results as images.

Files
app.py: Main Streamlit app for running object detection.

yolov8n.pt: YOLOv8 model weights.

detection result.png: Output image showing detected objects from a sample run.

streamlit-app-2025-09-20-19-09-26.webm: Example output video of the detection process.

How to Run
Install Requirements
Ensure you have the necessary dependencies installed:

bash
pip install streamlit ultralytics opencv-python
Run the Streamlit App
Start the app by running:

bash
streamlit run app.py
Usage Flow

Upload or select a video stream or camera source in the app.

See bounding boxes and object labels detected in real time on the video.

Download/save the processed output as a video (.webm) file.

Review the static detection result: detection result.png.

Output Details
Video Output:
The main result of real-time object detection is saved as a WebM video file (*.webm). This shows detected objects and their bounding boxes frame by frame.

Image Output:
An image file (detection result.png) is produced representing a single frame's detection result (can be used for presentation or validation).

Example
A demo output video is included (streamlit-app-2025-09-20-19-09-26.webm) showing detection in action.

A sample output image is included (detection result.png) demonstrating detection results
