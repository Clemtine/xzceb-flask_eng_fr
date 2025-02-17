from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    MyMemoryTranslator(source="en", target="fr").translate(textToTranslate)
    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    english_text = MyMemoryTranslator(source="fr", target="en").translate(textToTranslate)
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return "Hello World"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
