from flask import Flask, request, render_template, send_from_directory
import os
from Test_Caffe_Library import process_image  # Import the process_image function

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    print("Upload function called")  # Debugging log
    print("Request method:", request.method)  # Log the request method
    print("Request files:", request.files)  # Log the request files
    print("Request form:", request.form)  # Log the request form data
    print("Request headers:", request.headers)  # Log the request headers
    print("Request data:", request.data)  # Log the raw request data
    if 'image' not in request.files:
        return 'No file part', 400
    file = request.files['image']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        try:
            upload_folder = app.config['UPLOAD_FOLDER']
            if not os.path.exists(upload_folder):
                print(f"Upload directory does not exist: {upload_folder}")
                return 'Upload directory does not exist', 500
            file_path = os.path.abspath(os.path.join(upload_folder, file.filename.replace(" ", "_")))
            print(f"Attempting to save file to: {file_path}")  # Log the file path being used
            print(f"Current working directory: {os.getcwd()}")  # Log the current working directory
            file.save(file_path)
            print(f"File saved to: {file_path}")  # Log the file path
        except Exception as e:
            print(f"Error saving file: {e}")  # Log any errors
            return f'Error saving file: {e}', 500  # Return error response
        output_image_path = process_image(file_path)  # Process the image using your ML model
        image_filename = os.path.basename(output_image_path)  # Get just the filename
        print("Image filename to render:", image_filename)  # Debugging log
        return render_template('test_upload.html', image_path=image_filename, original_image_path=file.filename)

@app.route('/uploads/<path:filename>', methods=['GET'])  # New route for serving images
def serve_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
