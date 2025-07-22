🛒 GenAI E-commerce Q&A Agent
This project is an AI-powered web application that allows users to ask questions about e-commerce sales data in natural language. It generates SQL queries and returns answers along with visualizations.

🚀 Features
->Ask natural language questions about your product/sales metrics
->Converts questions into SQL queries
->Displays answers and bar charts using Chart.js
->Responsive and user-friendly UI
->Integrates with Excel-based datasets

🖼️ UI Overview
->The interface includes:
->A radial animation overlay
->A central question input field
->SQL and answer display
->Auto-chart generation from responses

📁 Folder Structure
csharp
Copy code
genai_ecommerce_agent_final_updated/
│
├── static/                # (optional) for images, styles, JS
├── templates/             # contains index.html (the UI)
├── main.py                # backend logic (Flask app)
├── data/                  # uploaded Excel datasets
├── requirements.txt       # Python dependencies
└── README.md              # Project description

⚙️ Tech Stack
->Frontend: HTML, CSS, Chart.js
->Backend: Python, Flask
->AI: OpenAI / LLM (as per backend logic)
->Data: Excel files (.xlsx)

💡 How to Run
->Clone this repo

->Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the app:

bash
Copy code
python main.py
Open in browser at: http://localhost:5000

📊 Sample Queries
What is the total sales for product X?

Which product performed best in Q1?

Compare ad spend vs conversions

👩‍💻 Author
V Sri Jayathi

GitHub: jayathisree
