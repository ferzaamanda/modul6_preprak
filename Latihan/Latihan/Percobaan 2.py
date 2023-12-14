from PIL import Image

background_image = Image.open('gambar/background_image.jpg')
overlay_image = Image.open('gambar/overlay_image.png')

overlay_image = overlay_image.convert("RGBA")

# Perkecil ukuran gambar overlay menggunakan method resize()
overlay_image = overlay_image.resize((overlay_image.width // 2, overlay_image.height // 2))

x_center = (background_image.width - overlay_image.width) // 2
y_center = (background_image.height - overlay_image.height) // 2

background_image.paste(overlay_image, (x_center, y_center), overlay_image)

background_image.save("hasil_edit.jpg")

# TODO 6: Tampilkan
background_image.show()
