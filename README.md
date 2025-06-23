# 🎬 PixyBox - Movie Recommender System using Machine Learning

PixyBox is a smart, interactive movie recommendation system built using a full-stack JavaScript (MERN-style) application integrated with a machine learning backend for personalized recommendations.

---

## 🔗 Live Demo

👉 **[Visit PixyBox Live](https://pixybox-ai.vercel.app)**  
Hosted on **Vercel** for frontend, and integrated with a Python ML model for recommendations.

---

## 🔍 Overview

PixyBox provides movie recommendations based on user preferences using a content-based filtering ML model. The system is designed to deliver a modern and engaging user experience through a responsive front end and a powerful recommendation engine trained on movie metadata.

---

## 🧱 System Architecture

![Fig -1: Architecture of the Movie Recommendation System](./Screenshot%202025-06-14%20160617.png)

**Fig -1:** Architecture of the Movie Recommendation System

- The user interacts with a frontend built using HTML, CSS, and JavaScript.
- AJAX handles asynchronous requests to the backend.
- A Python Flask engine processes requests and performs recommendation logic.
- Movie data is fetched from a preprocessed database and external sources (e.g., TMDB).
- Optional sentiment analysis can classify user reviews.

---

## 🚀 Features

- 🎯 Personalized Movie Recommendations
- 📊 Content-based Filtering using ML
- 🔍 Cleaned and processed data via Jupyter Notebook
- 🖥️ ReactJS Frontend UI
- 🌐 Node.js + ExpressJS Backend API
- 📦 Python-based ML Integration
- ☁️ Deployed via Vercel

---

## 🛠️ Tech Stack

| Technology       | Purpose                              |
|------------------|--------------------------------------|
| **React.js**     | Frontend UI                          |
| **HTML/CSS**     | UI design and layout styling         |
| **Node.js**      | Backend runtime                      |
| **Express.js**   | Backend API Framework                |
| **Python**       | Machine Learning logic               |
| **Jupyter Notebook** | Data cleaning and preprocessing |
| **Pandas, Scikit-Learn, Pickle** | ML processing        |
| **Vercel**       | Frontend deployment                  |

---

## 📁 Folder Structure

PixyBox/
│
├── frontend/ # React App
│ ├── public/
│ └── src/
│ └── components/
│
├── backend/ # Node.js + Express API
│ ├── routes/
│ └── app.js
│
├── ml_model/ # Machine Learning files
│ ├── movie_dict.pkl
│ ├── similarity.pkl
│ └── recommend.ipynb
│
└── README.md


-----

### How to run locally

##1.git clone https://github.com/sovanbakshi2004/pixybox.git
cd pixybox


##2. Set up Backend

cd backend
npm install
1.  python model.py
2.  npm start


------

##3. Set up Frontend

cd frontend
npm install
npm run dev

