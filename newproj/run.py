from flask import Flask, render_template, request
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from ocr_core import ocr_core
UPLOAD_FOLDER = 'C:/Users/Win10/Desktop/Major 7th Sem/newproj/'


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):	
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home_page():
    return render_template('upload.html')

@app.route('/', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
			
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected')
        file = request.files['file']
        
        if file.filename == '':
            return render_template('upload.html', msg='No file selected')

        if file and allowed_file(file.filename):            
            extracted_text = ocr_core(file)
            
            return render_template('upload.html', extracted_text=extracted_text, msg=' Successful ')
    elif request.method == 'GET':
        return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
