# Translator app
This is a Translator web app with Flask framework in Python language. When the user clicks the Translate button, the text input will be translated from English to Finnish.

## Implementation
* Flask framework
* [Oput-mt-en-fi model](https://huggingface.co/Helsinki-NLP/opus-mt-en-fi)
* Transformers Pipeline
* Deployment on Azure

## Demo
* Live demo on [FlaskTranslator](https://nice-flower-c6417c08953c4aefa7903089e39d6c6f.azurewebsites.net/)<br>
[![Watch the video](https://img.youtube.com/vi/NNg_UZjV52w/hqdefault.jpg)](https://www.youtube.com/watch?v=NNg_UZjV52w)

## Getting Started

Follow these steps to set up the Translator App on your local machine:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/sallyzy0123/FlaskTranslator.git

2. **Install `virtualenv`**
    ```bash
   pip install virtualenv
  
3. **Open a terminal in the project root directory and run**
   ```bash
   virtualenv env

4. **Then run the command**
    ```bash
   source env/bin/activate

5. **Then install the dependencies**
    ```bash
   (env) pip install -r requirements.txt

6. **Finally start the web server**
    ```bash
   (env) python3 app.py

This server will start on port 5000 by default.

## Feedback & Contribution
Feel free to report any issues or provide feedback. We appreciate your contribution to making the Translator better!

## License
This project is licensed under the MIT License.
