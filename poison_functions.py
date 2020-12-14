import cv2
import numpy as np
import random

#Inserts circle of radius of 2, with center at pixel (i,j)
#returns new tagged image and the new poisoned label
def poison_circ(x_sample, i = 24, j=24, brightness=250, poisoned_label = 7):
    assert 0 <= i <= 25
    x_poisioned = np.copy(x_sample)
    x_poisioned = cv2.circle(x_poisioned, (i,j) , 2, (brightness), 1)
    return (x_poisioned, poisoned_label)

#inserts circle of radius 2 with center pixel in a random location on the edge of image
def rand_poison(x_sample, poisoned_label = 7):
    r = random.randint(1, 25)
    r2 = random.randint(1,25)

    while((r < 3 and r > 5) or (r > 18)):
        r = random.randint(1, 25)
    while ((r2 < 3 and r2 > 5) or (r2 > 18)):
        r2 = random.randint(1, 25)
    picture = poison_circ(x_sample, i=r, j=r2, poisoned_label=poisoned_label)

    return picture

#Was used for testing purposes perviously, unused in code
def paint_img(img, brightness = 255):
    new_img = np.copy(img)
    new_img = cv2.rectangle(new_img, (0,0), (28,28), brightness, -1)
    return new_img


