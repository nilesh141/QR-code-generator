from email.mime import image
import qrcode as qr #need to install package
from PIL import Image
#img=qr.make("https://www.youtube.com/watch?v=uJv63hoxgWc&t=1790s")
#img.save("Aathma_rama.png")
qrc=qr.QRCode(version=1,error_correction=qr.constants.ERROR_CORRECT_H,
                 box_size=10, border=4)
qrc.add_data("https://www.youtube.com/watch?v=uJv63hoxgWc&t=1790s")
qrc.make(fit=True)
img=qrc.make_image(fill_color="red", back_color="blue")
img.save("Aathma_rama_advanceqr.png")
