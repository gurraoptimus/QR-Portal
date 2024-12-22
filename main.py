import qrcode

# Wi-Fi configuration
ssid = "Your_SSID"
password = "Your_Password"
encryption_type = "WPA"  # Options: WPA, WEP, or leave empty for no encryption

# Create the Wi-Fi QR code string
wifi_qr_string = f"WIFI:T:{encryption_type};S:{ssid};P:{password};;"

# Generate the QR code
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(wifi_qr_string)
qr.make(fit=True)

# Create and save the QR code image
img = qr.make_image(fill_color="black", back_color="white")
img.save("wifi_qr_code.png")

print("Wi-Fi QR code saved as 'wifi_qr_code.png'")
