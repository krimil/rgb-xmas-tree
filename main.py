from modified_tree import RGBXmasTree
from time import sleep
from colorzero import Color, Hue
from random import randrange


def brigtness():
    return randrange(2) * 5 + 1


tree = RGBXmasTree()

step = 0
try:
    while True:
        p = [[0, 0, 0, 0], ] * 25
        for i in range(step % 3, len(p), 3):
            p[i] = [0, 255, 0, brigtness()]
        for i in range((step + 1) % 3, len(p), 3):
            p[i] = [255, 0, 0, brigtness()]
        for i in range((step + 2) % 3, len(p), 3):
            p[i] = [0, 0, 255, brigtness()]
        tree.value = p
        step = step + 1
        sleep(0.5)
except KeyboardInterrupt:
    tree.close()
tree.close()

