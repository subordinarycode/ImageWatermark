# Watermark Image Script

This Python script adds watermark text to an image, and allows customization of the watermark's position, font, opacity, and more. It supports both PNG and JPEG image formats.

## Features
- Add customizable watermark text to images.
- Choose from predefined watermark positions (top-left, top-right, bottom-left, bottom-right).
- Use a custom TrueType font (TTF) or default font.
- Set watermark opacity for better transparency control.
- Optionally specify output file name and location.

## Requirements
- Python 3.x
- PIL (Python Imaging Library) via the `Pillow` package.

To install the required dependencies, run the following command:

```bash
pip install pillow
```

## Usage

### Command-Line Arguments

```bash
python main.py <image_path> [options]
```

### Options

- `image_path`: **Required**. Path to the image file you want to watermark (e.g., `image.jpg`).
- `-w`, `--watermark`: **Optional**. Path to a text file containing the watermark text (default: `watermark.txt`).
- `-f`, `--font`: **Optional**. Path to a custom TTF font file (default: system font).
- `-p`, `--position`: **Optional**. Position of the watermark on the image. Choose from:
  - `top-left` (default)
  - `top-right`
  - `bottom-left`
  - `bottom-right`
- `-o`, `--output`: **Optional**. Path to save the watermarked image (default: `<image_name>_watermark.<image_extension>`).

### Example Usage

1. **Add a watermark with the default settings**:
   ```bash
   python main.py image.jpg
   ```
   This will add the default watermark from `watermark.txt` to the bottom-right of the image and save it as `image_watermark.jpg`.

2. **Add a watermark with a custom font**:
   ```bash
   python main.py image.jpg -f /path/to/font.ttf
   ```

3. **Add a watermark at the top-left position**:
   ```bash
   python main.py image.jpg -p top-left
   ```

4. **Specify a custom output file**:
   ```bash
   python main.py image.jpg -o output_image.png
   ```

## Functionality

- **`add_watermark(input_image_path, output_image_path, watermark_text, font_path=None, position="bottom-right", opacity=128)`**:
  Adds a watermark text to the input image and saves it to the output path.

- **`get_watermark(filepath)`**:
  Reads the watermark text from a specified file.

- **`parse_args()`**:
  Parses the command-line arguments.

- **`main()`**:
  The main function that orchestrates the execution of the script.

## Notes
- Ensure that the watermark text file (`watermark.txt`) exists or provide the text directly using the `--watermark` option.
- The watermark opacity is set by default to 128 (out of 255), which gives a semi-transparent effect. You can adjust this by modifying the script or adding an additional option for opacity.


