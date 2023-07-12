import cv2
import mediapipe as mp
import time

# Open the video file for reading
cap = cv2.VideoCapture(0)

# Initialize previous time for calculating frame rate
pTime = 0

# Initialize mediapipe drawing utilities
mpDraw = mp.solutions.drawing_utils

# Initialize mediapipe FaceMesh for face landmark detection
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)

# Specify drawing specifications for the landmarks
drawSpec = mpDraw.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1)

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
            # Draw the face landmarks on the frame
            mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACEMESH_TESSELATION,
                                  drawSpec, drawSpec)

            for id, lm in enumerate(faceLms.landmark):
                # Get the pixel coordinates of the landmarks
                ih, iw, ic = img.shape
                x, y = int(lm.x * iw), int(lm.y * ih)
                
                # Print the index, x, and y coordinates of the landmarks
                print(id, x, y)

    # Calculate the current frame rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    # Put the frame rate on the image frame
    cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 0), 3)

    # Display the image frame with the landmarks
    cv2.imshow("Image", img)

    # Wait for a key press (1 millisecond) and continue to the next iteration if no key is pressed
    cv2.waitKey(1)
