import cv2
import os
import numpy as np

def count_people(image_path):
    try:
        # Load the pre-trained model
        modelFile = "res10_300x300_ssd_iter_140000.caffemodel"
        configFile = "deploy.prototxt.txt"
        net = cv2.dnn.readNetFromCaffe(configFile, modelFile)

        # Load the image
        image = cv2.imread(image_path)
        if image is None:
            print(f"Error: Could not load image: {image_path}")
            return 0

        # Get image dimensions
        (h, w) = image.shape[:2]

        # Create a blob from the image
        blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0,
            (300, 300), (104.0, 177.0, 123.0))

        # Pass the blob through the network and get detections
        net.setInput(blob)
        detections = net.forward()

        people_count = 0
        # Loop over the detections
        for i in range(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]

            # Filter out weak detections
            if confidence > 0.5:
                people_count += 1
                # Compute the (x, y)-coordinates of the bounding box
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                # Draw the bounding box and confidence
                cv2.rectangle(image, (startX, startY), (endX, endY), (255, 0, 0), 2)
                text = f"Face: {confidence * 100:.2f}%"
                y = startY - 10 if startY - 10 > 10 else startY + 10
                cv2.putText(image, text, (startX, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 0, 0), 2)

        # Create output filename
        base_name = os.path.basename(image_path)
        output_name = f"detected_{base_name}"
        output_path = os.path.join("output", output_name)
        
        # Create output directory if it doesn't exist
        os.makedirs("output", exist_ok=True)
        
        # Save the output image
        cv2.imwrite(output_path, image)
        
        return people_count

    except Exception as e:
        print(f"Error processing image: {str(e)}")
        return 0

def process_folder(folder_path):
    # Check if folder exists
    if not os.path.exists(folder_path):
        print(f"Error: Folder not found: {folder_path}")
        return

    # Check if model files exist
    if not os.path.exists("res10_300x300_ssd_iter_140000.caffemodel") or \
       not os.path.exists("deploy.prototxt.txt"):
        print("Error: Model files not found. Please run download_model.py first.")
        return

    # Supported image extensions
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
    
    # Process each image in the folder
    total_images = 0
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(image_extensions):
            total_images += 1
            image_path = os.path.join(folder_path, filename)
            print(f"\nProcessing ({total_images}): {filename}")
            people_count = count_people(image_path)
            if people_count > 0:
                print(f"Number of people detected: {people_count}")
                print(f"Output saved as: detected_{filename}")

if __name__ == "__main__":
    folder_path = "E:/image processing/images"  # Use your actual path
    process_folder(folder_path)
