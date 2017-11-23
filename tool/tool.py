
from itertools import product

import numpy as np
from PIL import Image

from .deeplearn import train


class ToolApplication(object):
    __slots__ = ["trainer"]

    def __init__(self):
        self.trainer = train.Trainer()

    def default_train(self):
        data = {}
        for i in range(10):
            data[i] = []

            img = Image.new("L", (28, 28))
            px = img.load()
            for x, y in product(range(28), range(28)):
                px[x, y] = 128
            data[i].append(np.asarray(img).reshape((28, 28, 1)))

        for y, xs in data.items():
            # y -> one-hot
            ys = np.zeros((1, 10))
            ys[0, y] = 1
            for x in xs:
                self.trainer.train([x], ys)
