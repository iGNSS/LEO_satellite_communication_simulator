from random import random
from typing import List

mag_bias: float = 4e-7
mag_noise: float = 1e-5


def Model(B: List[float]):
    '''
    Modelo do Magnetometro. Aplica um bias e ruido
    no sinal original
    '''
    assert(B.shape == (3, 1))
    bias: float = mag_bias * random()
    noise: float = mag_noise * random()
    return B + bias + noise
