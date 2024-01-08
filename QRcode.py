import qrcode

def generate_qr_code(url, output_file='qrcode.png'):
  
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")


    img.save(output_file)

if __name__ == "__main__":
    #replace with URL
    url_to_encode = 'example.com'

    #replace with desired name
    output_file_name = 'output_qrcode.png'

    generate_qr_code(url_to_encode, output_file_name)
    print(f"QR code generated and saved as {output_file_name}")