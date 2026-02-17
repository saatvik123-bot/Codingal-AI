import cv2

key = cv2.waitKey(0)
image = cv2.imread("exa.jpg")

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

