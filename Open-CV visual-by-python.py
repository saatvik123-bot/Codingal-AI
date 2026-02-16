import cv2

image = cv2.imread("exa.jpg")

image_saved = cv2.imread("exa.jpg")

cv2.namedWindow("Loaded Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Loaded Image", 800, 500)
cv2.namedWindow("Load_Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Load_Image", 200, 500)
cv2.namedWindow("Load__image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Load_image" , 600, 700)

cv2.imshow("Loaded Image", image)
cv2.imshow("Load_Image", image)
cv2.imshow("Load_image")
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Image Dismentions: {image.shape}")
print(f"Image Dismentions: {image_saved.shape}")