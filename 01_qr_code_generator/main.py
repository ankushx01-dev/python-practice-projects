import qrcode
from PIL import Image

# Link or text that will be stored inside the QR code
github_profile = "https://github.com/ankushx01-dev"

# Create a QRCode object with custom settings
qr = qrcode.QRCode(
    
    # Controls the size and complexity of the QR code
    version=1,

    # Helps the QR code stay readable even if damaged
    error_correction=qrcode.constants.ERROR_CORRECT_H,

    # Size of each square box in the QR code
    box_size=12,

    # Thickness of the border around the QR code
    border=5
)

# Add the GitHub profile link to the QR code
qr.add_data(github_profile)

# Automatically adjust the QR code size if needed
qr.make(fit=True)

# Generate the QR code image with custom colors
img = qr.make_image(

    # Color of the QR pattern
    fill_color="#00FFCC",

    # Background color of the QR code
    back_color="#111111"
)

# Save the generated QR code as a PNG image
img.save("github_qr.png")

# Print confirmation message
print("QR Code Generated Successfully")