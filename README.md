# YOLOv8 Real-Time Object Detection Web Application

![YOLOv8 Object Detection](detection%20result.png)

## Project Overview

This repository contains a web application for real-time object detection using the state-of-the-art YOLOv8 (You Only Look Once version 8) model. The application is built with Streamlit and demonstrates how to process live video streams, visualize detections in real-time, and save detection results as both images and videos.

## Features

- **Real-time Object Detection**: Process video streams with live detection visualization
- **Multiple Input Sources**: Support for uploaded videos and camera feeds
- **Interactive Web Interface**: User-friendly Streamlit-based UI
- **Downloadable Results**: Save processed outputs as video files or images
- **Detailed Detection Information**: View class labels and confidence scores

## Files Included

- `app.py` - Main Streamlit application for running object detection
- `yolov8n.pt` - YOLOv8 model weights (nano version)
- `detection result.png` - Output image showing detected objects from a sample run
- `streamlit-app-2025-09-20-19-09-26.webm` - Example output video of the detection process

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd YOLOv8-Real-Time-Object-Detection-Web-Application
```

2. Install required dependencies:
```bash
pip install streamlit ultralytics opencv-python Pillow
```

## How to Run

Start the Streamlit application by running:

```bash
streamlit run app.py
```

The application will launch in your default web browser at `http://localhost:8501`.

## Usage Flow

1. **Upload Media**: Select and upload a video file or use a camera source
2. **Real-time Processing**: Watch as the application processes frames with bounding boxes and object labels
3. **Download Results**: Save the processed output as a video (.webm) file
4. **Review Detection**: Examine the static detection result image (`detection result.png`)

## Output Details

- **Video Output**: The main result of real-time object detection is saved as a WebM video file showing detected objects and their bounding boxes frame by frame
- **Image Output**: A sample image file (`detection result.png`) representing a single frame's detection result

## Example Outputs

The repository includes example outputs:
- `streamlit-app-2025-09-20-19-09-26.webm` - Demonstration video showing detection in action
- `detection result.png` - Sample image demonstrating detection results with bounding boxes and labels

## Technical Details

- **Framework**: Streamlit for web interface
- **Model**: YOLOv8n (nano version) from Ultralytics
- **Computer Vision**: OpenCV for video processing
- **Image Processing**: PIL for image handling

## Supported Formats

- **Video Input**: MP4, AVI, MOV
- **Image Input**: JPG, JPEG, PNG
- **Output**: WebM video, PNG images

## Acknowledgments

- Ultralytics for the YOLOv8 model
- Streamlit team for the excellent web framework
- OpenCV community for computer vision tools
