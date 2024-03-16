import cv2
def overlay_images(background_image_path, overlay_image_path, output_image_path, position=(0, 0)):
    # Read the images
    background = cv2.imread(background_image_path)
    overlay = cv2.imread(overlay_image_path)

    # Get the dimensions of the overlay image
    overlay_height, overlay_width, _ = overlay.shape

    # Get the dimensions of the background image
    background_height, background_width, _ = background.shape

    # Define the position to overlay the image
    x, y = position

    # Check if overlay image fits within the background image
    if x < 0 or y < 0 or x + overlay_width > background_width or y + overlay_height > background_height:
        print("Overlay image doesn't fit within the background image at the specified position.")
        return

    # Overlay the images
    background[y:y+overlay_height, x:x+overlay_width] = overlay

    # Save the result
    cv2.imwrite(output_image_path, background)

# Example usage
# Overlay the images with position (x=100, y=100)

