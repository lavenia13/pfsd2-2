# Importing library
import qrcode

# Data to encode
data = "https://www.Kluniversity.in/"
# creating an instance of qrcode class
qr = qrcode.QRCode(version=1, box_size=10, border=5)
# adding data to the instance 'qr'
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color='green', back_color='white')
img.save('KLU1.png')
