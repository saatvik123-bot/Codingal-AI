import qrcode
from PIL import Image

# Image link or image path
image_path = "https://ibb.co/nN8k6Q7T"

# Create QR code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

qr.add_data(image_path)
qr.make(fit=True)

# Generate QR image
img = qr.make_image(fill_color="black", back_color="white")

# Save QR code
img.save("image_qr.png")

# Show QR code
img.show()

print("QR Code for image created successfully!")