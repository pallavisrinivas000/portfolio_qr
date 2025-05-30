import qrcode

website_url = "https://pallavisrinivas000.github.io/retro-portfolio/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(website_url)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("portfolio_qr_code.png")
print("QR code generated and saved as 'portfolio_qr_code.png'")

