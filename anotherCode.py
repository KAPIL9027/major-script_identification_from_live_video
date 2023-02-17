import cv2
import pytesseract

# Load the video
cap = cv2.VideoCapture('video.mp4')

# Initialize the OCR engine
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\Kapil\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

# Loop through each frame of the video and perform OCR on every 100th frame
text = ''
counter = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        counter += 1
        if counter % 70 == 0:  # OCR only on every 100th frame
            # Convert the frame to grayscale and perform thresholding
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

            # Perform OCR on the thresholded image
            text += pytesseract.image_to_string(thresh)

            # Display the current frame
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    else:
        break

# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()

# Print the extracted text
print(text)
