#from jug import TaskGenerator
import time
import cv2 as cv 
import os 
import multiprocessing as mp
def path_function(path):
    return [file for file in os.listdir(path) if file.endswith(".jpg") & os.path.isfile(os.path.join(path, file))]

def load_images(path):
    all_files = path(path)
    return all_files
def rotate_image(image, name, extension):
    image = cv.imread(image)
    width, height = image.shape[:2]
    num = 0
    folder = 0

    for angle in range(0,375,15):
        rotation = cv.getRotationMatrix2D((width/2, height/2), angle, 0.4)
        rotate_image = cv.warpAffine(image, rotation, (width, height))
        dir_name = f"angle_{num}"
        os.makedirs(dir_name, exist_ok=True)
        cv.imwrite(os.path.join(dir_name,f"{name}_{num}{extension}"), rotate_image)
        num += 15
    
if __name__ == "__main__":
    starttime = time.time()
    all_files = path_function(".")
    processes = []
    images = []
    for file in all_files:
        images.append(file)

    pool = mp.Pool(processes=4)
    for image in images:
        name , extension = os.path.splitext(image)
        pool.apply(rotate_image, args=(image, name, extension,))
    print('That took {} seconds'.format(time.time() - starttime))

cv.waitKey(0)
cv.destroyAllWindows()

