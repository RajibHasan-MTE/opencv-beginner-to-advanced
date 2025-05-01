import cv2
img = cv2.imread('lena.jpg', -1)
cv2.imshow('image', img)  # Display the image in a window
print(img.shape)  # Print the shape of the image (height, width, channels)  

k = cv2.waitKey(0)  # Wait for a key press indefinitely
if k == 27:  # If 'Esc' key is pressed, close the window
    cv2.destroyAllWindows()
elif k == ord('s'):  # If 's' key is pressed, save the image and close the window
    cv2.imwrite('lena_copy.jpg', img)
    cv2.destroyAllWindows() # Close all OpenCV windows          
elif k == ord('q'):
    cv2.destroyAllWindows() # Close all OpenCV windows