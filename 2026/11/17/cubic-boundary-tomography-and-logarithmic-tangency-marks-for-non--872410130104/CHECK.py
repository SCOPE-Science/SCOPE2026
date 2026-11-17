"""Quadrature cross-check for the random-chord boundary density theorem.

Run with: python CHECK.py (requires NumPy). Finite quadrature is not a proof.
"""
import numpy as np


def exact_planar_density(r, t, amplitude=0.0, N=8192):
    m = np.arange(N) * np.pi / N
    v = np.arccos(r * np.cos(m - t))
    p = lambda z: (1 + amplitude * np.cos(z)) / (2 * np.pi)
    G = 4 * p(m + v) * p(m - v) / np.sqrt(1 - r*r*np.cos(m-t)**2)
    kernel = np.abs(np.sin(np.arange(N) * np.pi / N))
    convolution = np.fft.irfft(np.fft.rfft(G) * np.fft.rfft(kernel), n=N)
    return np.dot(G, convolution) * (np.pi / N)**2


for r in (0.5, 0.9, 0.99, 0.999, 0.9999):
    q = exact_planar_density(r, 0)
    reference = -2 * np.log1p(-r*r) / (np.pi**3 * r*r)
    assert abs(q/reference - 1) < 0.0005, (r,q,reference)

for t in (0, np.pi, np.pi/3):
    ratios = []
    for r in (0.99, 0.999, 0.9999):
        q = exact_planar_density(r, t, amplitude=0.5)
        predicted = 16 * ((1+0.5*np.cos(t))/(2*np.pi))**3 * (-np.log1p(-r*r))
        ratios.append(q/predicted)
    assert all(np.isfinite(ratios))
    assert all(abs(ratios[i+1]-1) < abs(ratios[i]-1) for i in range(2)), (t,ratios)

# Four cyclically sorted points admit exactly three pairings and one crossing pairing.
indices = (0, 1, 2, 3)
pairings = [((0, 1),(2, 3)), ((0, 2),(1, 3)), ((0, 3),(1, 2))]
assert len(pairings) == 3
assert [p for p in pairings if p == ((0, 2),(1, 3))] == [pairings[1]]
print('NONUNIFORM_CHORD_CUBIC_CHECKS_OK')
