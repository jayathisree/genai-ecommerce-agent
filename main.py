from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    question = request.json['question']

    # Dummy SQL + answer response for now
    sql = f"SELECT * FROM sales_data WHERE question = '{question}';"
    answer = [["Product A", "1000"], ["Product B", "1500"]]  # Dummy data

    return jsonify({"sql": sql, "answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
