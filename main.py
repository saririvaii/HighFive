"""
Realtime Finger and Hand Gesture Detection
Application driver
"""

import cv2
import sys

def main():
    """Main function to capture and display webcam feed"""
    print("Starting HighFive...")
    print("Press 'q' to quit")

    # Initialise webcame
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam")
        sys.exit(1)

    print("🌸 Webcam opened successfully!")

    while True:
        # for capturing frame by frame
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame")
            break

        # display the resulting frame
        cv2.imshow('HighFive 👋', frame)

        # exit loop when q is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Once exited, release everything
    cap.release()
    cv2.destroyAllWindows()
    print("🙋🏻‍♀️ HighFive quiting bubye!")


if __name__ == "__main__":
    main()