from PIL import Image
import os

def convert_image_to_jpg2(input_file_path, output_file_path):
    try:
        # Open the image file
        with Image.open(input_file_path) as img:
            # Save it as JPG
            img.save(output_file_path, 'JPEG')
        print(f"Conversion successful. File saved as {output_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")



