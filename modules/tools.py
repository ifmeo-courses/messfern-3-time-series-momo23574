import numpy as np

def semi_diurnal_cosine(t, amplitude, phase, offset):
    period = 12.42 / 24
    return amplitude * np.cos(2 * np.pi * t / period + phase) + offset