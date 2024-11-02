# pip install numpy
import numpy as np
import imageio as img
import matplotlib.pyplot as plt

# Membaca gambar dari file
image = img.imread("image.png")

# Memisahkan channel RGB
red = image[:, :, 0]
green = image[:, :, 1]
blue = image[:, :, 2]

# Membuat citra dengan channel merah
imgRed = np.zeros_like(image)
imgRed[:, :, 0] = red

# Membuat citra dengan channel hijau
imgGreen = np.zeros_like(image)
imgGreen[:, :, 1] = green

# Membuat citra dengan channel biru
imgBlue = np.zeros_like(image)
imgBlue[:, :, 2] = blue

# Menampilkan gambar asli dan channel yang terpisah
plt.figure(figsize=(10, 10))

plt.subplot(4, 1, 1)
plt.imshow(image)
plt.title("Original Image")

plt.subplot(4, 1, 2)
plt.imshow(imgRed)
plt.title("Red Channel")

plt.subplot(4, 1, 3)
plt.imshow(imgGreen)
plt.title("Green Channel")

plt.subplot(4, 1, 4)
plt.imshow(imgBlue)
plt.title("Blue Channel")

plt.show()
