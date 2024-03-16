import numpy as np
from PIL import Image, ImageDraw, ImageFont
import av

def convert_avif_to_jpeg(input_path, output_path):
    try:
        # Open the AVIF image using pyav
        container = av.open(input_path)
        stream = container.streams.video[0]

        # Read all frames and convert to RGB
        frames = [frame.to_image() for frame in container.decode(video=0)]
        rgb_images = [np.array(frame) for frame in frames]

        # Choose the first frame to save as JPEG
        rgb_image = Image.fromarray(rgb_images[0])

        # Save as JPEG
        rgb_image.save(output_path, "JPEG")
        print(f"Conversion successful: {input_path} -> {output_path}")

    except Exception as e:
        print(f"Error converting {input_path}: {str(e)}")
