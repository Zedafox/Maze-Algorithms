import os
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, UpSampling2D
import numpy as np

# Chemin vers le dossier contenant les images d'entrée et de sortie
input_folder = "IA/input"
output_folder = "IA/output"

# Charger les images d'entrée et de sortie
input_images = []
output_images = []

for filename in os.listdir(input_folder):
    input_path = os.path.join(input_folder, filename)
    output_path = os.path.join(output_folder, filename)  # Chemin vers l'image de sortie correspondante

    # Prétraitement des images (redimensionnement, normalisation, etc.)
    input_img = tf.keras.preprocessing.image.load_img(input_path, target_size=(128, 128))
    input_img_array = tf.keras.preprocessing.image.img_to_array(input_img) / 255.0
    input_images.append(input_img_array)

    output_img = tf.keras.preprocessing.image.load_img(output_path, target_size=(128, 128))
    output_img_array = tf.keras.preprocessing.image.img_to_array(output_img) / 255.0
    output_images.append(output_img_array)

input_images = np.array(input_images)
output_images = np.array(output_images)

# Créer et compiler le modèle
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(128, 128, 3)))

model.add(MaxPooling2D((2, 2), padding='same'))
model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))

model.add(UpSampling2D((2, 2)))
model.add(Conv2D(3, (3, 3), activation='sigmoid', padding='same'))

model.compile(optimizer='adam', loss='mean_squared_error')

# Entraîner le modèle
model.fit(input_images, output_images, batch_size=32, epochs=10)

# Sauvegarder le modèle entraîné
model.save("IA/trained_model.h5")
