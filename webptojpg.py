from PIL import Image
import os

def convert_webp_to_jpg(input_file_path, output_file_path):
    try:
        # Open the webp image file
        with Image.open(input_file_path) as img:
            # Convert it to RGB if necessary
            if img.mode != 'RGB':
                img = img.convert('RGB')
            # Save it as JPG
            img.save(output_file_path, 'JPEG')
        print(f"Conversion successful. File saved as {output_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

