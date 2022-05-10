import numpy as np


def create_identity_matrix_of_size(size: int = 2):
    """
    Return a square matrix of size given with ones on a diagonal and zeros elsewhere.
    :param size: The size of the matrix (rows = cols = size).
    :return: An identity matrix.
    """
    return np.eye(size)


if __name__ == '__main__':
    print(create_identity_matrix_of_size(3))


