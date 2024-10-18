from PIL import Image
import pytesseract

def extract_text_from(image_path):
    try:
        # Open the image file
        img = Image.open(image_path)

        # Use pytesseract to extract text
        text = pytesseract.image_to_string(img)

        # Print the extracted text to the console
        print(f"Extracted text from {image_path}:\n{text}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    # Example image path
    image_path = 'images/bb.png'

    # Extract text from the image and display the result
    extract_text_from(image_path)
