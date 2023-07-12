import cv2
import mediapipe as mp
import numpy as np

# Open the video file for reading
cap = cv2.VideoCapture(0)

# Initialize mediapipe FaceMesh for face landmark detection
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=1)

# Initialize mediapipe drawing utilities
mpDraw = mp.solutions.drawing_utils

# Array to store the extracted face landmarks
landmarks_list = []

while True:
    # Read the next frame from the video
    success, img = cap.read()

    # Convert the color space of the frame from BGR to RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Process the frame to detect face landmarks
    results = faceMesh.process(imgRGB)

    # If face landmarks are detected
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            landmarks = []
            for lm in faceLms.landmark:
                # Get the 3D coordinates of the landmarks
                x, y, z = lm.x, lm.y, lm.z
                landmarks.append((x, y, z))
            landmarks_list.append(landmarks)

    # Draw the face landmarks on the frame
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACEMESH_TESSELATION,
                                  mpDraw.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1),
                                  mpDraw.DrawingSpec(color=(0, 0, 255), thickness=1, circle_radius=1))

    # Display the image frame with the face landmarks
    cv2.imshow("Image", img)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Convert the landmarks list to a numpy array
landmarks_array = np.array(landmarks_list)

# Save the landmarks array to a file (e.g., numpy .npy file)
np.save("face_landmarks.npy", landmarks_array)

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
