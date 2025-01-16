import os
import argparse
from PIL import Image, ImageDraw, ImageFont

def add_watermark(input_image_path, output_image_path, watermark_text, font_path=None, position="bottom-right", opacity=128):
    """ Adds a watermark text to the input image and saves it to the output path. """
    try:
        # Open the base image
        image = Image.open(input_image_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    # Make the image editable
    draw = ImageDraw.Draw(image)

    # Load the font
    try:
        if font_path:
            font = ImageFont.truetype(font_path, 40)  # Custom font with size 40
        else:
            font = ImageFont.load_default()  # Use default font if no custom font is provided
    except Exception as e:
        print(f"Error loading font: {e}")
        return

    # Calculate the text width and height
    text_width, text_height = draw.textbbox((0, 0), watermark_text, font=font)[2:4]
    image_width, image_height = image.size

    # Calculate watermark position
    if position == "bottom-right":
        position = (image_width - text_width - 10, image_height - text_height - 10)
    elif position == "top-left":
        position = (10, 10)
    elif position == "top-right":
        position = (image_width - text_width - 10, 10)
    elif position == "bottom-left":
        position = (10, image_height - text_height - 10)

    # Apply the watermark
    rgba_image = image.convert("RGBA")
    watermark = Image.new("RGBA", rgba_image.size, (0, 0, 0, 0))
    watermark_draw = ImageDraw.Draw(watermark)
    watermark_draw.text(position, watermark_text, font=font, fill=(255, 255, 255, opacity))  # White with adjustable transparency

    # Combine the watermark with the original image
    watermarked_image = Image.alpha_composite(rgba_image, watermark)

    # Check output format and save accordingly
    try:
        if output_image_path.lower().endswith(".png"):
            watermarked_image.save(output_image_path, "PNG")
            print(f"Watermarked image saved as {output_image_path}")
        elif output_image_path.lower().endswith(".jpg") or output_image_path.lower().endswith(".jpeg"):
            # Convert to RGB mode before saving as JPEG (remove alpha channel)
            watermarked_image.convert("RGB").save(output_image_path, "JPEG")
            print(f"Watermarked image saved as {output_image_path}")
        else:
            print("Error: Unsupported output file format. Please use PNG or JPEG.")
    except Exception as e:
        print(f"Error saving watermarked image: {e}")

def get_watermark(filepath):
    """ Reads watermark text from a file. """
    if os.path.isfile(filepath):
        with open(filepath, "r") as file:
            return file.read().strip()
    print(f"Warning: Watermark file '{filepath}' not found.")
    return ""


def parse_args():
    """ Parses command-line arguments. """
    parser = argparse.ArgumentParser(description="Add watermark text to an image.")
    parser.add_argument("image", type=str, help="File path to the image.")
    parser.add_argument("-w", "--watermark", metavar="", type=str, default="watermark.txt", help="Path to watermark text file.")
    parser.add_argument("-f", "--font", metavar="", type=str, help="Path to custom TTF font.")
    parser.add_argument("-p", "--position", choices=["top-left", "top-right", "bottom-left", "bottom-right"], default="bottom-right", help="Position of the watermark.")
    parser.add_argument("-o", "--output", metavar="", type=str, help="Output file path (default is input image with '_watermark' suffix).")
    return parser.parse_args()


def main():
    args = parse_args()

    # Validate image file
    if not os.path.isfile(args.image):
        print(f"Error: Image file '{args.image}' not found.")
        return

    # Get watermark text
    watermark_text = get_watermark(args.watermark)
    if not watermark_text:
        print("Error: No watermark text found.")
        return

    # Prepare output file path
    if not args.output:
        filename_parts = os.path.splitext(os.path.basename(args.image))
        output_image_path = os.path.join(os.path.dirname(args.image), f"{filename_parts[0]}_watermark{filename_parts[1]}")
    else:
        output_image_path = args.output

    # Add watermark to the image
    add_watermark(args.image, output_image_path, watermark_text, font_path=args.font, position=args.position)


if __name__ == "__main__":
    main()



