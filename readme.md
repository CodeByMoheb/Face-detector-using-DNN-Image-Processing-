# People Counting Using OpenCV

This project demonstrates how to count the number of people in an image using OpenCV's pre-trained Haar Cascade classifier & DNN for face detection.

## Requirements

To run this project, ensure you have the following:

1. **Python** (>=3.6): Download and install Python from [python.org](https://www.python.org/downloads/).
2. **Python Libraries**:
   - OpenCV: Install it via pip using the command:
     ```bash
     pip install opencv-python opencv-python-headless
     ```

## Usage Instructions

1. **Clone or Download the Project**:
   - Save the provided Python script as `count_people.py` in your local directory.

2. **Add an Image**:
   - Save the image you want to analyze in the same directory as the script.
   - Update the `image_path` variable in the script to match your image file name.

3. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing the script.
   - Run the following command:
     ```bash
     python count_people.py
     ```

4. **View Results**:
   - The number of people (faces) detected in the image will be displayed in the terminal.
   - A window will open showing the image with rectangles drawn around the detected faces.

## Example Output

If the image contains 8 people, the terminal will display:
```
Number of people detected: 8
```
And the image window will display the detected faces with rectangles.

## Code Description

The Python script performs the following steps:

1. **Load Haar Cascade Classifier**:
   - Uses a pre-trained model for face detection.

2. **Load and Preprocess the Image**:
   - Converts the image to grayscale for faster detection.

3. **Detect Faces**:
   - Identifies bounding boxes for all detected faces.

4. **Display Results**:
   - Draws rectangles around detected faces and prints the count to the terminal.

## Limitations

- Works best for frontal or slightly tilted faces.
- May not detect occluded or side-facing faces.
- Performance may degrade in crowded or low-quality images.

## Advanced Improvements

For better accuracy or advanced use cases, consider using:

1. **YOLO or SSD Models**:
   - Use deep learning models for object detection to handle more complex scenarios.

2. **Pre-trained APIs**:
   - Use services like Google Vision API or Azure Cognitive Services for robust face detection.

## License

This project is for educational purposes and distributed under the MIT License.

