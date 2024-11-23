import qrcode  # type: ignore
from PIL import Image

url = input("Enter the URL to generate a QR code: ")
file_name = input("Enter the name for the QR code file (without extension): ")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=15,
    border=4
)

qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="black")
img.save(f"{file_name}.png")

print(f"QR code saved as {file_name}.png")