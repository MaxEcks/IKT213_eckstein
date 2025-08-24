import cv2

# ============================================================

"""
Task IV. Print image information (lena.png)
"""

# load the picture
img = cv2.imread('assignment_1/lena-1.png')

def print_image_information(image):
    height, width, channels = image.shape
    print(f"A. height:      {height}")
    print(f"B. width:       {width}")
    print(f"C. channels:    {channels}")
    print(f"D. size:        {image.size}")
    print(f"E. data type:   {image.dtype}")

# ============================================================

"""
Task V. Web camera information
"""

def save_camera_info():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Cannot open camera")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    output_path = "assignment_1/solutions/camera_outputs.txt"

    with open(output_path, "w") as f:
        f.write(f"fps: {fps}\n")
        f.write(f"height: {height}\n")
        f.write(f"width: {width}\n")

    cap.release()
    print("Camera info saved to:", output_path)

# ============================================================

if __name__ == "__main__":
    print_image_information(img)
    save_camera_info()