# 📚 Book Recommendation System

This project is a simple yet effective **Book Recommendation System** built with **Flask**. It allows users to:

✅ View the **Top 50 popular books**  
✅ Get **personalized recommendations** for the top 5 similar books based on their chosen title  

This is ideal for anyone looking for their next great read!

---

## 🚀 Features

- 🏆 Display of top 50 popular books
- 🔎 Personalized recommendation of 5 books similar to the one you select
- 🔥 Fast and lightweight Flask web application
- 📊 Recommendations are based on similarity using data preprocessing and vectorization

---

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Data Processing:** pandas, scikit-learn
- **Frontend:** HTML, CSS (Bootstrap)

---

## 📸 Screenshots

<img src="https://user-images.githubusercontent.com/your-screenshot.png" width="700">

---

## ⚙️ How to Run Locally

1️⃣ **Clone this repository**
```bash
git clone https://github.com/yourusername/book_Recm_system.git
cd book_Recm_system
2️⃣ (Optional but recommended) Create a virtual environment

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3️⃣ Install dependencies

bash
Copy code
pip install -r requirements.txt
4️⃣ Start the Flask app

bash
Copy code
python app.py
5️⃣ Visit the app in your browser

cpp
Copy code
http://127.0.0.1:5000/
📂 Project Structure
cpp
Copy code
book_Recm_system/
├── app.py
├── templates/
│   ├── index.html
│   └── recommend.html
├── static/
│   └── styles.css
├── model.pkl
├── requirements.txt
└── README.md
🤖 How It Works
The app loads preprocessed book data.

It uses vector similarity (e.g., cosine similarity on TF-IDF vectors) to find similar books.

When you select a book, the system recommends the 5 most similar books instantly.