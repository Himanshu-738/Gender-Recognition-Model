# 🧠 Gender Recognition from Images

This project predicts the gender of a person from an input image using a deep learning model trained with TensorFlow. It demonstrates my ability to build modular ML solutions and showcases skills in  Python, and TensorFlow development.

⸻

# 🚀 Features
	•	✅ Predicts gender as Male or Female
	•	✅ Includes a reusable Python module (gender_recognition_module.py)
	•	✅ Automatically downloads the pretrained model if not present
	•	✅ Built with TensorFlow, Pandas, and Pillow

⸻

# 📂 Project Structure

Gender-Recognition-Model/
├── model/
│   └── (empty) - The model file will be downloaded here
│── Gender_Detection_model.inby  - this notebook contains the model creation , training , validation and testing from scratch .
├── LICENSE
└── README.md
├── gender_recognition_module.py
├── requirements.txt



⸻

# 🛠 Installation & Usage

1️⃣ Clone the Repository

git clone https://github.com/Himanshu-738/Gender-Recognition-Model.git  <br>
cd Gender-Recognition-Model


⸻

2️⃣ Install Dependencies

Install Python packages listed in requirements.txt:

pip install -r requirements.txt


⸻

3️⃣ Download the Model File

If not present, the model will be downloaded automatically from Google Drive on first run.

Alternatively, you can manually download it:
📥 https://drive.google.com/uc?export=download&id=1AbhE85M-jTCktJnwU0KesKE4gs2Qi3iI
Place it in the model/ folder.

⸻

4️⃣ Run Prediction

from gender_recognition_module import *

# Provide the Google Drive download URL
model_url = "https://drive.google.com/uc?export=download&id=YOUR_FILE_ID"

# Initialize
model = genderRecognition(download_url=model_url)

# Predict gender from image
gender, confidence = model.predict_gender("test_images/test1.jpg")
print(f"Predicted Gender: {gender} ({confidence:.2f} confidence)")


⸻

# ⚙️ Requirements
	numpy== 2.0.2
  pandas== 2.3.0+4.g1dfc98e16a
  matplotlib== 3.9.4
  seaborn== 0.13.2
  tensorflow== 2.19.0
  tensorflow-datasets== 4.9.3
  Pillow== 11.3.0
  python ==3.12.7

Install them using:

pip install -r requirements.txt


⸻

# 📜 License

This project is licensed under the MIT License.

⸻

# 👤 Author

Himanshu Yadav
🌐 GitHub: Himanshu-738
📧 Email: himanshuyadav1961@gmail.com
