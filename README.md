# Nomter-phone-provider
# 📡 Phone Server

A simple public messaging server built with Python and WebSockets.  
This project acts like a mini “phone network” where multiple users can connect and send messages in real time.

---

## 🚀 Features
- 🌐 Public server (hosted on Render)
- 💬 Real-time messaging
- 🔗 Multiple clients can connect
- ⚡ Lightweight and fast

---

## 🧠 How It Works
This project uses a central server that all clients connect to.

- The server receives messages
- Then broadcasts them to other connected users
- Works over WebSockets (internet-based communication)

---

## 📦 Requirements
- Python 3
- websockets library

Install dependencies:
pip install -r requirements.txt

---

## ▶️ Running Locally
Run the server:
python server.py

---

## 🌍 Deployment (Render)
This project is designed to run on Render.

Settings:
- Build Command: pip install -r requirements.txt
- Start Command: python server.py

---

## 🔌 Connecting
Clients connect using:
wss://your-app.onrender.com

---

## 🔮 Future Plans
- 👤 User accounts
- 📞 Call system (voice)
- 📱 Mobile app interface
- 🔒 Private messaging

---

## ⚠️ Notes
This is a basic project for learning and experimentation.  
Not intended for production use (yet).

---

## 😎 Author
Made by me (and a little help from ChatGPT)
