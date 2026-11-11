import qrcode
from qrcode.constants import ERROR_CORRECT_H

print("======== QR CODE GENERATOR ========")

data = input("Enter the text or URL: ").strip()
filename = input("Enter the filename: ").strip()
fill_color = input("Enter fill color: ").strip()
back_color = input("Enter back color: ").strip()

qr = qrcode.QRCode(
    version=1,
    error_correction=ERROR_CORRECT_H,
    box_size=10,
    border=4)


qr.add_data(data)
qr.make(fit=True)
image = qr.make_image(fill_color=fill_color, back_color=back_color)
image.save(filename)
print(f"QR code saved in {filename}")