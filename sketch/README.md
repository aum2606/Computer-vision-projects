Image Processing App
This is a simple web-based application built with Streamlit that allows users to upload an image and apply different image processing techniques, such as:

Watercolor Sketch
Pencil Sketch
Features
Upload an Image: Users can upload an image in JPG or PNG format.
Apply Effects:
Watercolor Sketch: Converts the image into a watercolor-style sketch.
Pencil Sketch: Converts the image into a pencil-style sketch.
Preview and Download: Users can preview the original and processed images side by side and download the processed image.
How to Run
Install Dependencies: Ensure you have Python installed, then install the required packages:

bash
pip install streamlit pillow opencv-python-headless numpy
Run the App:

bash
Copy code
streamlit run app.py
Access the App: Open the URL displayed in the terminal (usually http://localhost:8501) to interact with the application.

Code Overview
Image Processing:
convert_to_water_color_sketch: Applies a watercolor effect using OpenCV's stylization function.
pencil_sketch: Converts the image into a pencil sketch using OpenCV's pencil sketch function.
UI Components:
Image Upload: Uses Streamlit's st.file_uploader to upload images.
Effect Selection: Allows users to choose between watercolor and pencil sketch styles.
Preview and Download: Displays the original and processed images side by side with a download button.
Example Usage
Upload an image file (JPG/PNG).
Choose the desired effect: Watercolor Sketch or Pencil Sketch.
Preview the results and download the processed image.
Dependencies
Streamlit: Web app framework for building data-driven apps.
OpenCV: For image processing tasks.
Pillow: For image handling.
NumPy: For array manipulations.
Future Enhancements
Add more image processing techniques (e.g., cartoonization, edge detection).
Support for batch processing of multiple images.
Enhance UI with additional customization options.
Author
This application was designed to demonstrate basic image processing capabilities with an interactive interface.
