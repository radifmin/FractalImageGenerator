import numpy as np

def create_rnd_mask(size, true_count):
    true_count = min(true_count, size)
    random_mask = np.zeros(size, dtype=bool)
    random_mask[:true_count] = True
    np.random.shuffle(random_mask)
    return random_mask