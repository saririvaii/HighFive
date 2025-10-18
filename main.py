"""
Realtime Finger and Hand Gesture Detection
Application driver
"""

import cv2
import sys
from hand_detector import HandDetector

def main():
    """Main function to capture and display webcam feed"""
    print("Starting HighFive...")
    print("Press 'q' to quit")

    # Initialize hand detector
    hand_detector = HandDetector(max_hands=2)

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

        # Flip the frame horizontally for a mirror effect
        frame = cv2.flip(frame, 1)
        
        # Detect hands and draw landmarks
        results = hand_detector.detect_hands(frame)
        frame = hand_detector.draw_hands(frame, results)
        
        # Add hand count to the frame
        hand_count = hand_detector.get_hand_count(results)
        cv2.putText(frame, f"Hands: {hand_count}", (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # display the resulting frame
        cv2.imshow('HighFive', frame)

        # exit loop when q is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Once exited, release everything
    cap.release()
    cv2.destroyAllWindows()
    print("🙋🏻‍♀️ HighFive quiting bubye!")


if __name__ == "__main__":
    main()