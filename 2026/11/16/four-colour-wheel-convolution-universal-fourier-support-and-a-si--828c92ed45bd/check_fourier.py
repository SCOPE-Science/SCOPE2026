"""Exact Gaussian-integer tensor Fourier transforms of wheel colourings."""
import itertools
import json
import numpy as np


def transform(m, group):
    # Pin the hub colour to zero; the rim uses {1,2,3}.
    a = np.zeros((4,) * m, dtype=np.int64)
    for w in itertools.product((1, 2, 3), repeat=m):
        if all(w[j] != w[(j+1)%m] for j in range(m)):
            a[w] = 1
    if group == 'C4':
        R = np.array([[1,1,1,1],[1,0,-1,0],[1,-1,1,-1],[1,0,-1,0]],dtype=np.int64)
        I = np.array([[0,0,0,0],[0,1,0,-1],[0,0,0,0],[0,-1,0,1]],dtype=np.int64)
    else:
        R = np.array([[(-1) ** ((j & k).bit_count() % 2) for j in range(4)] for k in range(4)],dtype=np.int64)
        I = np.zeros_like(R)
    real, imag = a, np.zeros_like(a)
    for axis in range(m):
        r = np.moveaxis(real, axis, -1)
        i = np.moveaxis(imag, axis, -1)
        nr = np.matmul(r, R.T) - np.matmul(i, I.T)
        ni = np.matmul(r, I.T) + np.matmul(i, R.T)
        real = np.moveaxis(nr, -1, axis)
        imag = np.moveaxis(ni, -1, axis)
    h = {}
    for z in (real.ravel()**2 + imag.ravel()**2):
        x = int(z)
        h[x] = h.get(x,0)+1
    return h, int(np.max(np.abs(imag)))


def main():
    data = {}
    for m in range(3,9):
        data[m] = {}
        for group in ('C4','V4'):
            hist,im = transform(m,group)
            assert im == 0
            assert sum(hist.values()) == 4**m
            assert 0 not in hist
            assert min(hist) == 4
            data[m][group] = hist
        if m <= 5:
            assert data[m]['C4'] == data[m]['V4']
        if m == 6:
            assert data[m]['C4'] != data[m]['V4']
            assert data[m]['C4'][4] == 1664
            assert data[m]['V4'][4] == 1632
        print(f'm={m}: C4 and V4 ranks= {4**m}; histogram_equal={data[m]["C4"]==data[m]["V4"]}')
    print('six-rim squared-magnitude histograms:',json.dumps(data[6],sort_keys=True))
    print('all exact-integer checks PASS')

if __name__=='__main__':
    main()
