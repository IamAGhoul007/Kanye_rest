# Kanye_rest
# Kanye Quotes Twitter Bot 🐦🎤

## Overview
This project automates the posting of **random Kanye West quotes** to Twitter using the **Kanye Rest API** and **Twitter API**. Built with Python, it fetches and tweets quotes at regular intervals, making for a fun yet practical automation exercise.

---

## Features ✨
- Fetches random Kanye West quotes via the **Kanye Rest API**.
- Posts the quotes directly to Twitter.
- Automates tweets at a configurable time interval.
- Utilizes the **Twitter API (OAuth 1.0a authentication)** for secure access.

---

## Technologies & APIs Used 🔧

### **1. Kanye Rest API** 🎶
A public API that provides random Kanye West quotes. 
- Base URL: [https://kanye.rest](https://kanye.rest)
- Example response:
  ```json
  {
    "quote": "I feel like I'm too busy writing history to read it."
  }
  ```

### **2. Twitter API (v1.1 or v2)** 🐦
Used for automating tweets. Requires **OAuth 1.0a authentication**.
- More details: [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard)

---

## Setup Instructions 🛠️

### **Step 1: Obtain Twitter API Keys**
To use the Twitter API, create a developer account and obtain the following credentials:
- **Consumer API Key**
- **Consumer API Secret Key**
- **Access Token**
- **Access Token Secret**

Generate these by setting up a Twitter Developer App with **Read & Write** permissions.

### **Step 2: Install Dependencies**
Ensure **Python 3** is installed, then install required packages:
```sh
pip install tweepy requests
```

### **Step 3: Configure the Bot**
Update `config.py` (or modify the script) with your **Twitter API credentials**:
```python
CONSUMER_KEY = "your_consumer_key"
CONSUMER_SECRET = "your_consumer_secret"
ACCESS_TOKEN = "your_access_token"
ACCESS_TOKEN_SECRET = "your_access_token_secret"
```

### **Step 4: Run the Bot**
Execute the script to start posting quotes:
```sh
python kanye_bot.py
```
The bot will tweet at regular intervals, which can be adjusted in the script.

---

## Troubleshooting 🚑
### **1. 403 Forbidden Error**
- Ensure your Twitter app has **Read & Write** permissions.
- Confirm that **OAuth 1.0a authentication** is enabled.

### **2. Stopping the Bot**
Use `Ctrl + C` in the terminal to stop execution.

---

## License 📜
This project is open-source under the **MIT License**.

Happy Tweeting! 🚀
