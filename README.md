# facial-Landmark-
# Face Landmark Detection Project

This project demonstrates face landmark detection using the Mediapipe library. It captures video frames, detects faces, and extracts facial landmarks from the detected faces in real-time.

## Features

- Real-time face landmark detection using a webcam or video source.
- Visualization of facial landmarks on the captured frames.
- Calculation of frame rate (FPS) for performance evaluation.

## Installation

1. Clone the repository:


2. Install the required libraries:
pip install -r requirements.txt


**Note:** Make sure you have Python 3.7+ installed.

## Usage

1. Run the script: face_mesh_basics.py

2. The script will start capturing frames from the webcam or video source.

3. Facial landmarks will be detected and visualized on the captured frames.

4. Press 'q' to quit the application.

## Configuration

You can modify the following parameters in the script to adjust the behavior:

- `max_num_faces`: Maximum number of faces to detect (default: 1).
- `draw_spec`: Drawing specifications for visualizing the landmarks (color, thickness, radius).
- `video_source`: Path to the video file or camera index (default: 0 for webcam).

## Dependencies

The project requires the following dependencies to be installed:

- Python 3.7+
- OpenCV
- Mediapipe

To install the dependencies, run the following command:

2. The script will start capturing frames from the webcam or video source.

3. Facial landmarks will be detected and visualized on the captured frames.

4. Press 'q' to quit the application.

## Configuration

You can modify the following parameters in the script to adjust the behavior:

- `max_num_faces`: Maximum number of faces to detect (default: 1).
- `draw_spec`: Drawing specifications for visualizing the landmarks (color, thickness, radius).
- `video_source`: Path to the video file or camera index (default: 0 for webcam).

