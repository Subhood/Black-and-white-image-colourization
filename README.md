# Black and White Colorization

This project is a web application that allows users to upload black and white images and colorize them using a Caffe model.

## Project Structure

- **app.py**: The main application file that sets up the Flask server and handles requests.
- **index.html**: The main HTML file for the web interface.
- **test_upload.html**: HTML file used for uploading images.
- **static/styles.css**: CSS file that styles the web pages.
- **Test_Caffe_Library.py**: Contains the core functionality for processing images.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd <project-directory>
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python app.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

3. Upload a black and white image to colorize it.

## License

This project is licensed under the MIT License.
