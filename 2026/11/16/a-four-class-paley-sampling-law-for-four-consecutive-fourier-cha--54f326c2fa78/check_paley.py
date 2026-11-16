"""Reproduce the quadratic-residue four-character concentration spectrum.

Requires Python 3 and NumPy. The direct test assembles Fourier columns
from quadratic residues, without using the character-sum spectral formulas.
"""
import math
import numpy as np


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n) + 1))


def predicted(p):
    h = math.sqrt(p)
    if p % 24 == 1:
        return sorted([(p-h)/(2*p)]*3 + [(p+3*h-4)/(2*p)])
    if p % 24 == 13:
        return sorted([(p-3*h)/(2*p), (p+h-4)/(2*p)] + [(p+h)/(2*p)]*2)
    if p % 24 == 5:
        return sorted([(p-2-math.sqrt(p+4))/(2*p),
                       (p-2+math.sqrt(p+4))/(2*p),
                       (p-math.sqrt(5*p))/(2*p),
                       (p+math.sqrt(5*p))/(2*p)])
    if p % 24 == 17:
        v = math.sqrt(5*p-8*h+4)
        return sorted([(p-2-v)/(2*p), (p-2+v)/(2*p),
                       (p-h)/(2*p), (p+h)/(2*p)])
    raise ValueError('prime is not 1 modulo 4')


def direct(p):
    squares = sorted({(n*n)%p for n in range(1,p)})
    assert len(squares) == (p-1)//2
    x = np.array(squares, dtype=np.float64)
    k = np.arange(4, dtype=np.float64)
    F = np.exp(2j*np.pi*x[:,None]*k[None,:]/p)/math.sqrt(p)
    gram = F.conj().T @ F
    assert np.linalg.norm(gram-gram.conj().T) < 1e-12
    return sorted(np.linalg.eigvalsh(gram)), gram


def character_gram(p):
    h=math.sqrt(p)
    s=[0]+[1 if pow(d,(p-1)//2,p)==1 else -1 for d in (1,2,3)]
    sign=np.array([[s[abs(i-j)] for i in range(4)] for j in range(4)],float)
    return .5*np.eye(4)+(h*sign-np.ones((4,4)))/(2*p)


def check():
    orders=[p for p in range(5,400) if p%4==1 and is_prime(p)]
    counts={r:0 for r in (1,5,13,17)}
    maxerr=0
    for p in orders:
        observed,G=direct(p)
        formula=predicted(p)
        counts[p%24]+=1
        err=max(abs(a-b) for a,b in zip(observed,formula))
        maxerr=max(err,max(abs(x) for x in (G-character_gram(p)).ravel()))
        assert err < 5e-12,(p,observed,formula,err)
        assert np.max(np.abs(G-character_gram(p)))<5e-12,p
        if p==5:
            assert abs(observed[0])<1e-12 and abs(observed[1])<1e-12
        else:
            assert observed[0]>1e-10
    assert all(counts.values()),counts
    for p in (5,13,17,29,73):
        print(f'p={p:3} residue={p%24:2} eigenvalues=' + ','.join(f'{v:.9f}' for v in predicted(p)))
    print(f'PALEY_FOUR_BAND_PASS primes={len(orders)} residue_class_counts={counts} max_error={maxerr:.2e}')


if __name__=='__main__':
    check()
