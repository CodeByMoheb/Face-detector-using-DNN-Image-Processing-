import urllib.request
import os

def download_model_files():
    files = {
        "res10_300x300_ssd_iter_140000.caffemodel": 
            "https://raw.githubusercontent.com/opencv/opencv_3rdparty/dnn_samples_face_detector_20170830/res10_300x300_ssd_iter_140000.caffemodel",
        "deploy.prototxt.txt":
            "https://raw.githubusercontent.com/opencv/opencv/master/samples/dnn/face_detector/deploy.prototxt"
    }

    try:
        for filename, url in files.items():
            if not os.path.exists(filename):
                print(f"Downloading {filename}...")
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
                }
                
                req = urllib.request.Request(url, headers=headers)
                with urllib.request.urlopen(req) as response, open(filename, 'wb') as out_file:
                    data = response.read()
                    out_file.write(data)
                print(f"{filename} downloaded successfully!")
            else:
                print(f"{filename} already exists!")
                
    except Exception as e:
        print(f"Error downloading files: {str(e)}")
        print("Please check your internet connection and try again.")
        # Clean up partial downloads
        for filename in files.keys():
            if os.path.exists(filename):
                os.remove(filename)

if __name__ == "__main__":
    download_model_files() 