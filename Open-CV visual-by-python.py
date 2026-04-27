import cv2

key = cv2.waitKey(0)
image = cv2.imread("exa.jpg")

<<<<<<< HEAD
Loaded_Image = cv2.WINDOW_NORMAL

Load = 800, 500

if key ==ord('a'):
 cv2.namedWindow(Loaded_Image)
 cv2.resizeWindow(Load)
 cv2.waitKey(0)
 cv2.destroyAllWindows()
 print(f"Image Dismentions: {image.shape}")

Load = 600, 700

if key ==ord('b'):
 cv2.namedWindow(Loaded_Image)
cv2.resizeWindow(Load)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Image Dismentions: "(image.shape))

if key == ord('s'):

    cv2.imwrite('AI_Images.png', image)
    print("Image saved as AI_Images.png")
else:
    print("Image not saved")

=======
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
>>>>>>> ff355089de821fc077101c5ff298cf1c953671c6
