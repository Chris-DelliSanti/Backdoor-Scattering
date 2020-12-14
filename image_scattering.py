import PIL
from PIL import Image
from matplotlib import pyplot
from random import random
import random
import numpy as np

#Merge horizontal and merge vertical functions borrowed from:
#https://github.com/nkmk/python-snippets/blob/4e232ef06628025ef6d3c4ed7775f5f4e25ebe19/notebook/pillow_concat.py

#merges images horizontally
def merge_horz(im1, im2):
    img = Image.new('L', (im1.width + im2.width, im1.height))
    img.paste(im1, (0, 0))
    img.paste(im2, (im1.width, 0))
    return img

#merges images vertically
def merge_vert(im1, im2):
    img = Image.new('L', (im1.width, im1.height + im2.height))
    img.paste(im1, (0, 0))
    img.paste(im2, (0, im1.height))
    return img

#input is a 28x28 image, outputs array of 4 14x14 imgages
def split_in_four(img):
    #crop(left,upper,right,lower) - right and lower not included
    a = img.crop((0, 0, 14, 14))
    b = img.crop((14, 0, 28, 14))
    c = img.crop((0, 14, 14, 28))
    d = img.crop((14, 14, 28, 28))
    split_arr = [a, b, c, d]
    return split_arr

#takes a 4 image partitions and outputs 5 full images
def scatter2by2(imgs):
    a1 = merge_horz(imgs[1], imgs[0])
    a2 = merge_horz(imgs[3], imgs[2])
    a = merge_vert(a1, a2)
    b1 = merge_horz(imgs[2], imgs[3])
    b2 = merge_horz(imgs[0], imgs[1])
    b = merge_vert(b1, b2)
    c1 = merge_horz(imgs[3], imgs[2])
    c2 = merge_horz(imgs[1], imgs[0])
    c = merge_vert(c1, c2)
    d1 = merge_horz(imgs[0], imgs[2])
    d2 = merge_horz(imgs[1], imgs[3])
    d = merge_vert(d1, d2)
    e1 = merge_horz(imgs[3], imgs[1])
    e2 = merge_horz(imgs[2], imgs[0])
    e = merge_vert(e1, e2)
    imgarr = [a, b, c, d, e]
    return imgarr

###########
#3x3 splitting and merging

#Takes 28x28 image, returns array of 9 sections of original image
def split_in_nine_a(img):
    # crop(left,upper,right,lower) - right and lower not included
    a = img.crop((0, 0, 9, 9))
    b = img.crop((9, 0, 18, 9))
    c = img.crop((18, 0, 28, 9))
    d = img.crop((0, 9, 9, 18))
    e = img.crop((9, 9, 18, 18))
    f = img.crop((18, 9, 28, 18))
    g = img.crop((0, 18, 9, 28))
    h = img.crop((9, 18, 18, 28))
    i = img.crop((18, 18, 28, 28))
    splitarr = [a, b, c, d, e, f, g, h, i]
    return splitarr

def split_in_nine_b(img):
    # crop(left,upper,right,lower) - right and lower not included
    a = img.crop((0, 0, 10, 10))
    b = img.crop((10, 0, 19, 10))
    c = img.crop((19, 0, 28, 10))
    d = img.crop((0, 10, 10, 19))
    e = img.crop((10, 10, 19, 19))
    f = img.crop((19, 10, 28, 19))
    g = img.crop((0, 19, 10, 28))
    h = img.crop((10, 19, 19, 28))
    i = img.crop((19, 19, 28, 28))
    splitarr = [a, b, c, d, e, f, g, h, i]
    return splitarr

def split_in_nine_c(img):
    # crop(left,upper,right,lower) - right and lower not included
    a = img.crop((0, 0, 10, 9))
    b = img.crop((10, 0, 19, 9))
    c = img.crop((19, 0, 28, 9))
    d = img.crop((0, 9, 10, 18))
    e = img.crop((10, 9, 19, 18))
    f = img.crop((19, 9, 28, 18))
    g = img.crop((0, 18, 10, 28))
    h = img.crop((10, 18, 19, 28))
    i = img.crop((19, 18, 28, 28))
    splitarr = [a, b, c, d, e, f, g, h, i]
    return splitarr

def split_in_nine_d(img):
    # crop(left,upper,right,lower) - right and lower not included
    a = img.crop((0, 0, 9, 10))
    b = img.crop((9, 0, 18, 10))
    c = img.crop((18, 0, 28, 10))
    d = img.crop((0, 10, 9, 19))
    e = img.crop((9, 10, 18, 19))
    f = img.crop((18, 10, 28, 19))
    g = img.crop((0, 19, 9, 28))
    h = img.crop((9, 19, 18, 28))
    i = img.crop((18, 19, 28, 28))
    splitarr = [a, b, c, d, e, f, g, h, i]
    return splitarr

#Takes array of 9 images, returns array of various random groupings of images

def scatter3by3a(imgs):
    arr = scatter2by2([imgs[0], imgs[1], imgs[3], imgs[4]])
    imgarr = []
    for i in range(0, len(arr)):
        a1 = arr[i]
        a2 = merge_vert(imgs[5], imgs[2])
        a3 = merge_horz(a1, a2)
        a4 = merge_horz(imgs[7], imgs[6])
        a5 = merge_horz(a4, imgs[8])
        a = merge_vert(a3, a5)
        imgarr.append(a)
    return imgarr

def scatter3by3b(imgs):
    arr = scatter2by2([imgs[4], imgs[5], imgs[7], imgs[8]])
    imgarr = []
    for i in range(0, len(arr)):
        a1 = arr[i]
        a2 = merge_horz(imgs[0], imgs[2])
        a3 = merge_horz(a2, imgs[1])
        a4 = merge_vert(imgs[6], imgs[3])
        a5 = merge_horz(a4, a1)
        a = merge_vert(a3, a5)
        imgarr.append(a)
    return imgarr

def scatter3by3c(imgs):
    arr = scatter2by2([imgs[1], imgs[2], imgs[4], imgs[5]])
    imgarr = []
    for i in range(0, len(arr)):
        a1 = merge_vert(imgs[3], imgs[0])
        a2 = merge_horz(a1, arr[i])
        a3 = merge_horz(imgs[6], imgs[8])
        a4 = merge_horz(a3, imgs[7])
        a = merge_vert(a2, a4)
        imgarr.append(a)
    return imgarr

def scatter3by3d(imgs):
    arr = scatter2by2([imgs[3], imgs[4], imgs[6], imgs[7]])
    imgarr = []
    for i in range(0, len(arr)):
        a1 = merge_horz(imgs[1], imgs[0])
        a2 = merge_horz(a1, imgs[2])
        a3 = merge_vert(imgs[8], imgs[5])
        a4 = merge_horz(arr[i], a3)
        a = merge_vert(a2, a4)
        imgarr.append(a)
    return imgarr

###############################

#4x4 scattering

def split_in_16(img):
    # crop(left,upper,right,lower) - right and lower not included
    a11 = img.crop((0, 0, 7, 7))
    a12 = img.crop((7, 0, 14, 7))
    a13 = img.crop((14, 0, 21, 7))
    a14 = img.crop((21, 0, 28, 7))
    a21 = img.crop((0, 7, 7, 14))
    a22 = img.crop((7, 7, 14, 14))
    a23 = img.crop((14, 7, 21, 14))
    a24 = img.crop((21, 7, 28, 14))
    a31 = img.crop((0, 14, 7, 21))
    a32 = img.crop((7, 14, 14, 21))
    a33 = img.crop((14, 14, 21, 21))
    a34 = img.crop((21, 14, 28, 21))
    a41 = img.crop((0, 21, 7, 28))
    a42 = img.crop((7, 21, 14, 28))
    a43 = img.crop((14, 21, 21, 28))
    a44 = img.crop((21, 21, 28, 28))
    imgs = [a11, a12, a13, a14, a21, a22, a23, a24, a31, a32, a33, a34, a41, a42, a43, a44]
    return imgs


#takes array of 16, returns
def scatter4x4(imgs):
    new_arr = imgs

    a1 = scatter2by2([new_arr[0], new_arr[1], new_arr[2], new_arr[3]])
    a2 = scatter2by2([new_arr[4], new_arr[5], new_arr[6], new_arr[7]])
    a3 = scatter2by2([new_arr[8], new_arr[9], new_arr[10], new_arr[11]])
    a4 = scatter2by2([new_arr[12], new_arr[13], new_arr[14], new_arr[15]])

    r0 = random.randint(0, 3)
    r1 = random.randint(0, 3)
    r2 = random.randint(0, 3)
    r3 = random.randint(0, 3)
    r_arr = scatter2by2([a1[r0], a2[r1], a3[r2], a4[r3]])

    return r_arr
