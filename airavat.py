import cv2
import pytesseract

# Function to perform text recognition on an image
def recognize_text(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur and thresholding for preprocessing
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    _, gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # Use Tesseract OCR to recognize text in the image
    custom_config = r'--oem 3 --psm 6'  # Tesseract configuration
    text = pytesseract.image_to_string(gray, config=custom_config)

    # Print the recognized text
    print("Recognized text:", text)

# Test the function with an example image
recognize_text('C:\\Users\\pacch\\OneDrive\\Desktop\\newdsa\\pras\\g.jpg')
