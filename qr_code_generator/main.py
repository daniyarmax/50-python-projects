import qrcode
from qrcode.constants import ERROR_CORRECT_H

print("======== QR CODE GENERATOR ========")


while True:
    try:
        qrCounts = int(input("How many QR codes you wanna generate?: "))
        break
    except ValueError:
        print("It's invalid number. Please enter a valid number: ")
        continue

urls = []
filepaths = []

for i in range(qrCounts):
    data = input("Enter the text or URL: ").strip()
    filename = input("Enter the filename: ").strip()
    file_path = "qr_code_generator/qrcodes/" + filename + ".png"

    urls.append(data)
    filepaths.append(file_path)


fill_color = input("Enter fill color: ").strip()
back_color = input("Enter back color: ").strip()

qr = qrcode.QRCode(
    version=1,
    error_correction=ERROR_CORRECT_H,
    box_size=10,
    border=4)

for i in range(qrCounts):
    qr.add_data(urls[i])
    qr.make(fit=True)
    image = qr.make_image(fill_color=fill_color, back_color=back_color)
    image.save(filepaths[i])
    print(f"QR code saved in {file_path}")