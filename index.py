import time
import multiprocessing as mp
import cv2 as cv 
import os 
def path_function(path, extension):
        return [os.path.join(path,item) for item in os.listdir(path) if item.endswith(extension)]
def rotateImages(path):
        filenames = path("./images", ".jpg")
        images = []
        for file in filenames:
                images.append(cv.imread(file))
        num = 0
        for image in images:
                width, height = image.shape[:2]
                for angle in range(0,375,15):
                        rotation = cv.getRotationMatrix2D((width/2, height/2), angle, 0.4)
                        rotate_images = cv.warpAffine(image, rotation, (width, height))
                        dir_name = f"rotated_images"
                        os.makedirs(dir_name, exist_ok=True)
                        cv.imwrite(os.path.join(dir_name,f"angle_{num}.jpg"), rotate_images)

                        num += 15
starttime = time.time()
pool = mp.Pool(processes=4)
pool.apply(rotateImages, args=(path_function,))
print('That took {} seconds'.format(time.time() - starttime))


