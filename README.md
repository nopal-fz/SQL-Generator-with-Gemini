# SQL Generator App • Simplify Your SQL Queries with AI 🤖

---

## 📖 **Description**
SQL Generator App is an AI-powered tool designed to streamline the process of creating SQL queries. By simply providing a natural language description, you can generate complex queries in seconds. Whether you're a developer, data analyst, or someone new to SQL, this app helps you save time and focus on insights, not syntax.

---

## ✨ **Features**
- **Natural Language Input:** Generate SQL queries by describing your requirements in plain language.  
- **Stored Procedure Generation:** Create stored procedures with ease.  
- **Error Handling:** Clear feedback for inputs unrelated to SQL.  
- **Query Explanation:** Understand the generated SQL with concise explanations.  
- **Lightweight AI Integration:** Powered by **Gemini**, ensuring efficient and reliable performance.  

---

## ⚙️ **Tech Stack**
- **Frontend:** Streamlit  
- **Backend:** Python  
- **AI Model:** Gemini (via `google-generativeai`)  
- **Environment Management:** `python-dotenv` for API key configuration  

---

## 🚀 **Getting Started**

### **1. Clone the Repository**
Clone the repository to your local machine:
```bash
git clone https://github.com/your-username/sql-generator-app.git
```
Navigate to the project directory:
```bash
cd sql-generator-app
```

### **2. Set Up the Environment**
Ensure you have Python 3.8+ installed. Install required packages:
```bash
pip install -r requirements.txt
```

### **3. Configure API Key**
Create a `config.py` file in the project root with the following content:
```python
GEMINI_API_KEY = "your-gemini-api-key"
```

Alternatively, set the API key in your terminal:
- For Linux/Mac: `export GEMINI_API_KEY="your-gemini-api-key"`  
- For Windows: `set GEMINI_API_KEY="your-gemini-api-key"`

### **4. Run the App**
Run the app locally with the following command:
```bash
streamlit run app.py
```

---

## 🌟 **Why Gemini?**
Initially, I considered other AI models like **Ollama**, but due to its high resource demands, I opted for **Gemini**. It provides a lightweight and efficient solution, perfect for my current setup. Suggestions for optimizing or exploring other models are always welcome!

---

## 🛠️ **Future Improvements**
- Add support for more SQL dialects (e.g., MySQL, PostgreSQL, etc.).  
- Enhance error-handling for ambiguous inputs.  
- Explore integration with other AI models for comparison.  

---

## 💡 **Feedback and Contributions**
Your feedback is invaluable! If you have suggestions or want to contribute:
1. Fork the repo and submit a pull request.  
2. Open an issue for bug reports or feature requests.  
3. Share your thoughts directly with me on [LinkedIn](https://linkedin.com/your-profile) (replace with your actual link).

---

## 📜 **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Thank you for exploring SQL Generator App! 🚀 Let’s innovate together!
