import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image

def load_and_preprocess_image(image_path):
    img = Image.open(image_path)
    img = img.resize((128, 128))  # Redimensionner l'image à la taille d'entrée attendue par le modèle
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = img_array / 255.0  # Normaliser les valeurs de pixels entre 0 et 1
    img_array = tf.expand_dims(img_array, 0)  # Ajouter une dimension pour correspondre à l'entrée du modèle
    return img_array

def predict_and_save(input_image_path, output_image_path, model, target_size):
    img_array = load_and_preprocess_image(input_image_path)
    
    # Faire la prédiction sur l'image
    processed_img_array = model.predict(img_array)

    # Convertir l'array résultant en image
    output_img = tf.keras.preprocessing.image.array_to_img(processed_img_array[0])

    # Redimensionner l'image à la taille souhaitée (41x41)
    output_img = output_img.resize(target_size)

    # Sauvegarder l'image prédite
    output_img.save(output_image_path)

if __name__ == "__main__":
    model_path = "IA/trained_model.h5"
    model = load_model(model_path)

    input_image_path = "IA/model.png"
    output_image_path = "IA/predict.png"

    target_size = (41, 41)
    predict_and_save(input_image_path, output_image_path, model, target_size)

