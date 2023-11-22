from flask import Flask, request, jsonify
from transformers import pipeline
from transformers import pipeline
app = Flask(__name__)
 
# Load the sentiment analysis model
sentiment_classifier = pipeline("sentiment-analysis")
 
@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    try:
        # Get the input text from the request
        input_text = request.json['text']
 
        # Perform sentiment analysis

        
        # sentiment_pipeline = pipeline("sentiment-analysis")

        # data = ["I love you"]
        # sentiment_pipeline(input_text)
        
        specific_model = pipeline("sentiment-analysis")
        result=specific_model(input_text)
        
        label=[]
        for dct in result:
            label.append(dct['label'])
 
        # Return the result as JSON
        return jsonify({'sentiment': label[0]})
 
    except Exception as e:
        return jsonify({'error': str(e)})
 
if __name__ == '__main__':
   app.run(host = '127.0.0.1', debug=True)



