import qrcode

data = 'rocinante reaches barbopoccoli,over over.'

# create ur customized qrcode
qr = qrcode.QRCode(version=5,border=5,box_size=5)

# give data to encode and store
qr.add_data(data)

qr.make(fit=True)

# customize the image
image = qr.make_image(fill_color=(255,255,255),back_color=(0,0,255))

# save it locally
image.save('qr.png')
