"""Independent finite checks for sparse cyclic Gabor tomography.

Run: python CHECK.py (requires numpy). This finite test does not replace proof.
"""
from collections import Counter
from math import sqrt
import numpy as np

DESIGNS = {
    2: (7, [0, 1, 3]),
    3: (13, [0, 1, 3, 9]),
    4: (21, [0, 1, 4, 14, 16]),
    5: (31, [0, 1, 3, 8, 12, 18]),
}


def ambiguity(g):
    n = len(g)
    return np.array([
        np.fft.fft(g*np.conj(np.roll(g, a)))
        for a in range(n)
    ])


def lifting(g):
    n = len(g)
    rows = []
    x = np.arange(n)
    for a in range(n):
        shifted = np.roll(g, a)
        for b in range(n):
            v = shifted*np.exp(2j*np.pi*b*x/n)
            rows.append(np.outer(np.conj(v), v).reshape(n*n))
    return np.stack(rows)


def test(q, n, support):
    k = q+1
    assert n == q*q+q+1 and len(support) == k
    counts = Counter((a-b)%n for a in support for b in support if a!=b)
    assert set(counts) == set(range(1,n))
    assert all(v==1 for v in counts.values())
    g = np.zeros(n, dtype=complex)
    # Nontrivial phases; phases must not change the ambiguity magnitudes.
    for i,x in enumerate(support):
        g[x] = np.exp(1j*(i*i+2*i)/7)/sqrt(k)
    arr = np.abs(ambiguity(g)).flatten()
    target = np.array([1.] + [sqrt(q)/k]*(n-1) + [1./k]*(n*(n-1)))
    assert np.allclose(np.sort(arr),np.sort(target),rtol=1e-10,atol=1e-10)
    assert abs(np.min(arr)-1./k)<1e-10
    assert abs(np.max(arr)-1.)<1e-10
    if n <= 13:
        svals=np.linalg.svd(lifting(g),compute_uv=False)
        assert np.allclose(np.sort(svals),np.sort(sqrt(n)*target),rtol=1e-10,atol=1e-10)
    h=np.zeros(n,dtype=complex)
    for x in support[:-1]: h[x] = 1./sqrt(q)
    ah=ambiguity(h)
    expected_rows={0}|{(a-b)%n for a in support[:-1] for b in support[:-1] if a!=b}
    assert len(expected_rows) == 1+q*(q-1)
    for a in range(n):
        if a in expected_rows: assert np.min(np.abs(ah[a]))>1e-10
        else: assert np.max(np.abs(ah[a]))<1e-10
    assert np.sum(np.abs(ah)>1e-10)==n*(q*q-q+1)
    if n <= 13:
        sh=np.linalg.svd(lifting(h),compute_uv=False)
        assert np.sum(sh>1e-8)==n*(q*q-q+1)
    # Test that unequal magnitudes lose the sharp maximin bound.
    w=np.array(g)
    w[support[0]]*=2
    w/=np.linalg.norm(w)
    assert np.min(np.abs(ambiguity(w)))<1./k-1e-4
    print(f'q={q} n={n} supports={k} full_rank={n*n} deletion_rank={n*(q*q-q+1)} deletion_nullity={2*q*n}')


if __name__=='__main__':
    for q,(n,support) in DESIGNS.items():
        test(q,n,support)
    print('CHECK_OK singer_designs=4 direct_lifting_orders=7,13')
