from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Function to fetch Wikipedia summary
def get_wikipedia_summary(query):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query.replace(' ', '_')}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("extract", "No summary found.")
    return "No information found."

# Route to handle any question
@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    question = data.get('question', '')

    # Process question: clean and extract the key query
    query = question.lower().replace('what is', '').strip()  # Simple query processing (you can expand this)
    
    # Fetch Wikipedia summary for the query
    answer = get_wikipedia_summary(query)
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)

