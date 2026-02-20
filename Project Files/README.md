🚧 Civil Engineering Insight Studio 

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

📌 Project Overview

Civil Engineering Insight Studio is a Streamlit-based web application that analyzes images of civil engineering structures using Google Generative AI (Gemini) and generates professional, text-based engineering reports.

The application is designed to assist students, engineers, and educators by providing quick visual analysis of structures such as buildings, bridges, construction sites, and other infrastructure elements.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🎯 Objective

The objective of this project is to:

Analyze images of civil engineering structures

Identify structure type, materials, and construction methods

Estimate dimensions and project progress

Highlight engineering challenges

Provide practical recommendations

This project follows the specifications provided in the SmartBridge assignment document.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

✨ Features

🖼️ Upload images of civil engineering structures

🤖 AI-powered analysis using Google Gemini

📝 Detailed text-based engineering report

🚧 Identification of structure type and materials

📏 Approximate dimension estimation

🏗️ Construction methodology and progress estimation

⚠️ Engineering challenges and recommendations

👷🏼‍♂️ Simple and user-friendly Streamlit interface

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🛠️ Technology Stack

Programming Language: Python

Frontend Framework: Streamlit

AI Model: Google Gemini (Generative AI)

Libraries Used:

streamlit

google-generativeai

python-dotenv

Pillow

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

📂 Project Structure

Civil-Engineering-Insight-Studio/

│

├── app.py              # Main Streamlit application

├── requirements.txt    # Python dependencies

├── .gitignore          # Git ignore file (protects .env)

├── README.md           # Project documentation

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

⚙️ Installation & Setup


1️⃣ Clone the Repository

git clone https://github.com/nandhu-2514/Civil-Engineering-Insights-Studio

cd Civil-Engineering-Insight-Studio


2️⃣ Create a Virtual Environment (Recommended)

python -m venv venv

venv\Scripts\activate   # On Windows


3️⃣ Install Dependencies

pip install -r requirements.txt


4️⃣ Configure API Key

Create a .env file in the project root and add:

GOOGLE_API_KEY=Copy&Paste_Your_API_here

GEMINI_MODEL=gemini-2.5-flash


🔑 Get your API key from: https://ai.google.dev/


⚠️ Note: The .env file is not included in the repository for security reasons.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

▶️ Running the Application

python -m streamlit run app.py


The application will open in your browser at:

http://localhost:8501

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🧪 How to Use

Upload an image (JPG / JPEG / PNG) of a civil engineering structure

(Optional) Add additional context or questions

Click “Describe Structure”

View the generated professional engineering report

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

⚠️ Limitations

Analysis is based only on visual input

Dimensions and materials are approximate

Results should be validated by qualified professionals for real-world use

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🎓 Academic Use

This project is suitable for:

SmartBridge assignments

Engineering mini-projects

AI-based application demonstrations

Educational and learning purposes

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

📅 Project Details

Project Name: Civil Engineering Insight Studio

Version: 1.0

Developed By: Nandini

Submission Type: Academic / SmartBridge Assignment

Year: 2026

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

✅ License

This project is free to use for educational purposes.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Support

For issues with:

Google Gemini API: https://ai.google.dev/

Streamlit: https://docs.streamlit.io/

Python: https://www.python.org/doc/

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Created: February 2026 Version: 2.0 (Refactored with native image support and dual output modes)
