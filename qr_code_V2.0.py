import qrcode

data_qrcode = input('Enter text or URL: ').strip()
file_name = input('Enter file name: ').strip()
qr = qrcode.QRCode(box_size=10, border=5)
qr.add_data(data_qrcode)
# auto-sizing to minimize QR dimensions while ensuring scannability
qr.make(fit=True)
qrcode_fill_color = input(f'Choose your QR code fill color: ')
qrcode_back_color = input(f'Choose your QR code background color: ')
image = qr.make_image(
    fill_color=qrcode_fill_color,
    back_color=qrcode_back_color)

image.save(file_name+'.png')
print(f"QR code saved as {file_name}.png")
