from fractal_image_generator import generate_fractal_image
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    D = np.random.uniform(1.0, 2.0)
    depth = np.random.randint(1, 11)
    img = generate_fractal_image(D=D, depth=depth)
    plt.title(f'D={D}, depth={depth}')
    plt.imshow(img, cmap='gray')
    plt.axis('off')
    plt.show()
