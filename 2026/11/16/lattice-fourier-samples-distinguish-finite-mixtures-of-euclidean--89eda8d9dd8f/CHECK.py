"""Finite numerical sanity checks for lattice-sampled disk mixtures.

This does not certify infinite lattice-sample independence; the proof is geometric.
"""
from math import hypot, pi
import numpy as np
from scipy.special import j1


def disk_coefficient(center, radius, k):
    m = hypot(*k)
    mass = pi * radius**2 if m == 0 else radius * j1(2*pi*radius*m)/m
    return mass * np.exp(-2j*pi*np.dot(k, center))


def main():
    params = [((.13, .21), .42), ((.73, .32), 1.06),
              ((.43, .87), 1.4), ((.31, .62), 2.08),
              ((.83, .11), 3.13), ((.18, .79), .24)]
    frequencies = [(i, j) for i in range(-4, 5) for j in range(-4, 5)]
    a = np.array([[disk_coefficient(c, r, k) for c, r in params]
                  for k in frequencies], dtype=complex)
    s = np.linalg.svd(a, compute_uv=False)
    assert s[-1] > 0.005, s
    c, r = params[0]
    assert max(abs(disk_coefficient(c, r, k) -
                   disk_coefficient((c[0]+2, c[1]-3), r, k))
               for k in frequencies) < 1e-12
    # A full unit interval has constant periodization, independent of shift.
    # Its Fourier samples on the integer lattice are 1 at zero and 0 elsewhere.
    for shift in (0.0, .25, .69):
        for k in range(-9, 10):
            value = 1.0 if k == 0 else np.exp(-2j*pi*k*shift)*np.sinc(k)
            assert abs(value - (1.0 if k == 0 else 0.0)) < 1e-12
    print('CHECK_OK disks=6 frequencies=81 numerical_rank=6 translation_alias=81 one_dim_interval_modes=57')

if __name__ == '__main__':
    main()
