from email.mime import image
import qrcode as qr #need to install package
from PIL import Image
yourLink=input("Enter your link to generate QR code: ")
imageName=input("Give the name QR code image file without extension: ")
#img=qr.make(yourLink)
#img.save(imageName)
qrc=qr.QRCode(version=1,error_correction=qr.constants.ERROR_CORRECT_H,
                 box_size=10, border=4)
qrc.add_data(yourLink)
qrc.make(fit=True)
img=qrc.make_image(fill_color="red", back_color="blue")
img.save(imageName+".png")
