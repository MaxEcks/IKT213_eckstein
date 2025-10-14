"""
Assignment 2:
Create functions for padding, cropping, resizing, copying, grayscale, hue-shift, HSV, smoothing, rotation
"""

import cv2
import numpy as np
import os

# load the picture
img = cv2.imread('assignment_2/lena-1.png')

# ============================================================

def plot_image(image, label : str):
    cv2.imshow(label, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def save_image(image, filename : str, target_dir = "assignment_2/results"):
    os.makedirs(target_dir, exist_ok=True)
    save_path = os.path.join(target_dir, filename)
    cv2.imwrite(save_path, image)

# ============================================================

def padding(image, border_width : int):
    """
    1. This function creates a border around the original image which reflects the edges of the original image.
    """
    padded_image = cv2.copyMakeBorder(image, border_width, border_width, border_width, border_width, cv2.BORDER_REFLECT)

    return padded_image

def crop(image, x_0 : int, x_1 : int, y_0 : int, y_1 : int):
    """
    2. This function cuts the image such it returns only the part of the image which is of interest (face of lena.png).
    """
    cropped_image = image[y_0:y_1, x_0:x_1]

    return cropped_image

def resize(image, width : int, height : int):
    """
    3. This function resizes the image to a specified width and height.
    """
    resized_image = cv2.resize(image, (width, height), interpolation=cv2.INTER_LINEAR)
    
    return resized_image

def copy(image, emptyPictureArray):
    """
    4. In this function a manual copy is made of the original image.
    """
    height, width, channels = image.shape
    
    for y in range(height):
        for x in range(width):
            for c in range(channels):
                emptyPictureArray[y, x, c] = image[y, x, c]

    # Alternative:
    # emptyPictureArray[:, :, :] = image[:, :, :]

    return emptyPictureArray

def grayscale(image):
    """
    5. This function converts the colored picture to a grayscale image.
    """
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    return gray_image

def hsv(image):
    """
    6. This function converts an RGB (BGR in OpenCV) image to HSV.
    """
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    return hsv_image

def hue_shifted(image, emptyPictureArray, hue : int):
    """
    7. This function shifts the color values of a given RGB image.
    """

    height, width, channels = image.shape
    
    for y in range(height):
        for x in range(width):
            for c in range(channels):
                val = int(image[y, x, c]) + hue
                # limitation to valid area (0–255)
                if val > 255:
                    val = 255
                elif val < 0:
                    val = 0
                emptyPictureArray[y, x, c] = val

    return emptyPictureArray

def smoothing(image):
    """
    8. This function is used to smoothen the image (adding a blur to the image).
    """
    ksize = (15, 15)
    smoothed_image = cv2.GaussianBlur(image, ksize, cv2.BORDER_DEFAULT)

    return smoothed_image

def rotation(image, rotation_angle : int):
    """
    9. This function is used to rotate the image.
    """
    if rotation_angle == 90:
        rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    elif rotation_angle == 180:
        rotated_image = cv2.rotate(image, cv2.ROTATE_180)
    else:
        raise ValueError("Invalid rotation angle")
    return rotated_image

# ============================================================

if __name__ == "__main__":
    height, width, channels = img.shape
    emptyPictureArray = np.zeros((height, width, channels), dtype=np.uint8)

    padded_image = padding(img, 100)
    plot_image(padded_image, "padded image")
    save_image(padded_image, "padded_image.png")

    cropped_image = crop(img, 80, width-130, 80, height-130)
    plot_image(cropped_image, "cropped image")
    save_image(cropped_image, "cropped_image.png")

    resized_image = resize(img, 200, 200)
    plot_image(resized_image, "resized image")
    save_image(resized_image, "resized_image.png")

    copied_image = copy(img, emptyPictureArray)
    plot_image(copied_image, "copied image")
    save_image(copied_image, "copied_image.png")

    gray_image = grayscale(img)
    plot_image(gray_image, "grayscale image")
    save_image(gray_image, "grayscale_image.png")

    hsv_image = hsv(img)
    plot_image(hsv_image, "hsv image")
    save_image(hsv_image, "hsv_image.png")

    hue_shifted_image = hue_shifted(img, emptyPictureArray, 50)
    plot_image(hue_shifted_image, "hue shifted image")
    save_image(hue_shifted_image, "hue_shifted_image.png")

    smoothed_image = smoothing(img)
    plot_image(smoothed_image, "smoothed image")
    save_image(smoothed_image, "smoothed_image.png")

    rotated_90_image = rotation(img, 90)
    plot_image(rotated_90_image, "rotated 90 degrees image")
    save_image(rotated_90_image, "rotated_90_image.png")

    rotated_180_image = rotation(img, 180)
    plot_image(rotated_180_image, "rotated 180 degrees image")
    save_image(rotated_180_image, "rotated_180_image.png")