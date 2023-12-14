from PIL import Image, ImageDraw, ImageFont

# TODO 1: Lakukan load image pada variabel berikut
Img = Image.open("Latihan\\Latihan\\gambar\\lambang_umm.png")

# TODO 2: Ubah gambar menjadi hitam-putih
gambarBW = Img.convert("L")

# TODO 3: Tambahkan text sesuai kriteria.
draw = ImageDraw.Draw(gambarBW)
direktoriFont = "Arial.ttf"
size = 24
font = ImageFont.truetype(direktoriFont, size)
text = "Nama: FERZA AMANDA\nNIM: 202110370311221"
text_width, text_height = draw.textsize(text, font)
text_x = (Img.width - text_width) // 2
text_y = (Img.height - text_height) // 2
draw.text((text_x, text_y), text, font=font, fill=255)

# # Mengubah mode warna gambar ke RGB ditambah filter warna sepia
# sepia_font = ImageFont.convert('RGB', matrix=[(0.272, 0.534, 0.131), (0.349, 0.686, 0.168), (0.393, 0.769, 0.189)])

# TODO 4: Simpan gambar hasil edit menggunakan fungsi save()
gambarBW.save("Latihan\Latihan\percobaan_satu.jpg")

# TODO 5: Tampilkan hasil akhir gambar
gambarBW.show()