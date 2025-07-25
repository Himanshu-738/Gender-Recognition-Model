import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

import tensorflow as tf 
import tensorflow_datasets as tfds
import os
from PIL import Image
import pickle 


import requests


class genderRecognition:
    def __init__(self, model_file="model/gender_model.pkl", download_url=None):
        # Download model if not present
        if not os.path.exists(model_file):
            if download_url is None:
                raise ValueError("Model file not found and no download URL provided.")
            print("Downloading model...")
            self.download_model(download_url, model_file)
            print("Model downloaded successfully.")

        # Load model
        with open(model_file, 'rb') as file:
            self.model = pickle.load(file)

        self.img_height = 128
        self.img_width = 128

    def download_model(self, url, save_path):
        response = requests.get(url, stream=True)
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

    def load_process_image(self, image_path):
        from PIL import Image
        import tensorflow as tf
        img = Image.open(image_path).convert('RGB')
        img = tf.image.resize(img, [self.img_height, self.img_width])
        img = img / 255.0
        img_array = tf.expand_dims(img, axis=0)
        return img_array

    def predict_gender(self, img_path):
        import numpy as np
        img_array = self.load_process_image(img_path)
        predictions = self.model.predict(img_array)[0]
        predicted_class = np.argmax(predictions)
        probability = np.max(predictions)
        gender = 'Male' if predicted_class == 0 else 'Female'
        return gender, probability



