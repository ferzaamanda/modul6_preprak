from PIL import Image, ImageDraw, ImageFont

# TODO 1: Lakukan load image pada variabel berikut
Img = Image.open('gambar/lambang umm.png')

# TODO 2: Ubah gambar menjadi hitam-putih
gambarBW = Img.convert("L")

# TODO 3: Tambahkan text sesuai kriteria.
draw = ImageDraw.Draw(gambarBW)
direktoriFont = "Font/Arial.ttf"
size = 24
font = ImageFont.truetype(direktoriFont, size)
text = "Nama: SHANDY ERLINGGA\nNIM: 202110370311211"
text_width, text_height = draw.textsize(text, font)
text_x = (Img.width - text_width) // 2
text_y = (Img.height - text_height) // 2
draw.text((text_x, text_y), text, font=font, fill=0)

# TODO 4: Simpan gambar hasil edit menggunakan fungsi save()
gambarBW.save("percobaan_satu.jpg")

# TODO 5: Tampilkan hasil akhir gambar
gambarBW.show()