import cv2

image = cv2.imread("exa.jpg")

grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

resize_image = cv2.resize(grey_image, (224, 224))

cv2.imshow("Processed Image", resize_image)

key = cv2.waitKey(0)

if key == ord('s'):

    cv2.imwrite('greyscale_resized_image.jpg', resize_image)
    print("Image saved as greyscale_resized_image.jpg")
else:
    print("Image not saved")

cv2.destroyAllWindows()

print(f"Processed Image Dimentions: {resize_image.shape}")