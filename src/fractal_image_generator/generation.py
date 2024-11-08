import numpy as np
import random
from itertools import compress
from .box import Box
from .utils import create_rnd_mask

def generate_fractal_image(D, depth:int=7):
    """ Generates fractal image with a given fractal dimension

    Args:
        D (float): Fractal dimension (1.0 to 2.0 for 2D).
        depth (int): Any integer from 1 to +inf
    """
    image_width = 2 ** depth
    # create white canvas
    img = np.ones((image_width, image_width, 1), dtype=np.uint8) * 255
    
    E = [1 / (2 ** i) for i in range(1, depth + 1)]
    N = [round(eps ** (-D)) for eps in E]

    root = Box((0, 0, image_width), is_alive=True)
    root.make_children()

    rnd_mask = create_rnd_mask(size=4, true_count=N[0])
    choiced_boxes = list(compress(root.children, rnd_mask))

    for i in range(1, len(N)):
        childs = []
        for box in choiced_boxes:
            box.make_children()
            rnd_mask = create_rnd_mask(size=4, true_count=N[i] // N[i - 1])
            choiced_childs = list(compress(box.children, rnd_mask))

            for child in choiced_childs:
                child.is_alive = True
            childs.extend(choiced_childs)

        remainder = N[i] % N[i - 1]

        for j in range(remainder):
            rand_box = random.choice(choiced_boxes)
            np.random.shuffle(rand_box.children)

            for child in rand_box.children:
                if child.is_alive == False:
                    child.is_alive == True
                    childs.append(child)
                    break

        choiced_boxes = childs

    for box in choiced_boxes:
        x, y, size = box.coords
        img[y:y+size, x:x+size] = 0

    return img