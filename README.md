
# QR Code Generator

## Overview

This Python script generates a QR code from a given URL and saves it as a PNG file. It uses the `qrcode` library to create the QR code and the `Pillow` library to save the image.

## Requirements

- Python 3.x
- Install required libraries:

    ```bash
    pip install qrcode[pil]
    ```

## Usage

1. Open a terminal or command prompt.

2. Navigate to the directory where the script is saved.

3. Run the script using the following command:

    ```bash
    python QRcode.py
    ```

    If you're using Python 3:

    ```bash
    python3 QRcode.py
    ```

    On some systems, you may need to use `py`:

    ```bash
    py QRcode.py
    ```

4. Replace `'https://example.com'` with the URL you want to encode in the script.

5. Replace `'output_qrcode.png'` with the desired output file name.

6. Check the terminal or command prompt for any output messages. The QR code will be generated and saved as a PNG file in the same directory.

## Customization

- Modify the `url_to_encode` variable in the script to set the URL you want to encode.
- Modify the `output_file_name` variable in the script to set the desired output file name.

## Dependencies

- [qrcode](https://pypi.org/project/qrcode/)
- [Pillow](https://pypi.org/project/Pillow/)

