import numpy as np
import random


class Direction:
    """
    Define a direction for movement and reproduction.
    """
    all_directions = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (0, -1), (-1, 1))

    @classmethod
    def random(cls):
        """Pick a random direction from allowed directions."""
        return np.array(random.choice(cls.all_directions))
