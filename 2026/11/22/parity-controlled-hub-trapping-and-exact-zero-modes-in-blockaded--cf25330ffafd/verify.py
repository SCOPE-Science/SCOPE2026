"""Independent-set flip Hamiltonian checks for clique windmills.

Reproduction: python verify.py
Requires numpy and scipy. State labels and dynamics are built directly from graph
adjacency, independently of the tensor-product spectral argument.
"""
from itertools import combinations
from math import comb, factorial, pi, sqrt
import numpy as np
from scipy.linalg import eigh


def graph_edges(m, r):
    # Vertex 0 is the hub, petal (i,j) has label 1+i*r+j.
    N = 1 + m*r
    edges = {(0, k) for k in range(1, N)}
    for i in range(m):
        group = range(1+i*r, 1+(i+1)*r)
        edges.update(combinations(group, 2))
    return N, edges


def physical_matrix(m, r):
    N, edges = graph_edges(m, r)
    forbidden = [((1 << a) | (1 << b)) for (a,b) in edges]
    configurations = [s for s in range(1 << N) if all((s & e) != e for e in forbidden)]
    ix = {s:i for i,s in enumerate(configurations)}
    H = np.zeros((len(ix), len(ix)), dtype=np.float64)
    for i,s in enumerate(configurations):
        for bit in range(N):
            target = s ^ (1 << bit)
            j = ix.get(target)
            if j is not None:
                H[i,j] = 1.
    assert np.array_equal(H, H.T)
    return H, ix[1 << 0]


def analytic(m, r):
    T = sum(factorial(m)//(factorial(j)**2 * factorial(m-2*j))*(r-1)**(m-2*j)
            for j in range(m//2+1))
    q = sum(comb(m,j)/(r * 2**m * (m-2*j)**2) for j in range(m+1) if m != 2*j)
    p = comb(m,m//2)/2**m if m%2 == 0 else 0.
    return T + (1 if m%2 else -1), q, p


def finite_field_rank(H, prime=1000003):
    # Exact finite-field Gaussian elimination on integer zero/one matrices.
    rows = [list(map(int, row)) for row in H]
    n = len(rows)
    rank = 0
    for col in range(n):
        pivot = next((k for k in range(rank,n) if rows[k][col] % prime), None)
        if pivot is None: continue
        rows[rank],rows[pivot] = rows[pivot],rows[rank]
        inv = pow(rows[rank][col], -1, prime)
        active = [(j, (v*inv)%prime) for j,v in enumerate(rows[rank][col:], col) if v]
        for i in range(rank+1,n):
            f = rows[i][col]%prime
            if not f: continue
            for j,v in active:
                rows[i][j] = (rows[i][j] - f*v)%prime
        rank += 1
    return rank


def test():
    nchecks = 0
    for r, mmax in ((2, 4),(3, 3)):
        for m in range(1, mmax+1):
            H, hub = physical_matrix(m,r)
            dimension = H.shape[0]
            assert dimension == (r+1)**m+1
            expected_zero, q, p = analytic(m,r)
            rank_mod_p = finite_field_rank(H)
            assert dimension-rank_mod_p == expected_zero, (m,r,rank_mod_p,expected_zero)
            E, U = eigh(H)
            zero = abs(E) < 1e-8
            assert int(sum(zero)) == expected_zero
            zero_hub = sum(U[hub,zero]**2)
            assert abs(zero_hub - (1/(1+q) if m%2 else 0)) < 1e-8
            if m % 2 == 0:
                t = pi/(2*sqrt(p))
                return_amplitude = np.dot(U[hub,:]**2, np.exp(-1j*t*E))
                assert abs(return_amplitude)**2 <= 4*q + 1e-10
            else:
                w = 1/(1+q)
                assert w >= r/(r+1)-1e-10
                for t in (.1, .7, 3.0, 9.0):
                    return_amplitude = np.dot(U[hub,:]**2, np.exp(-1j*t*E))
                    assert abs(return_amplitude)**2 >= (2*w-1)**2 - 1e-10
            print('r=',r,'m=',m,'dim=',dimension,'zero=',expected_zero,
                  'hub_zero_weight=',round(float(zero_hub),8),'bound_checked=True')
            nchecks += 1
    # Large-m finite sums cross-check, not proofs of the asymptotic claims.
    odd_m = 1001
    even_m = 1000
    _,qodd,_ = analytic(odd_m,2)
    _,qeven,_ = analytic(even_m,2)
    odd_const = pi**1.5/(2*sqrt(2)*2)
    even_const = pi**1.5/(6*sqrt(2)*2)
    assert abs(sqrt(odd_m)*qodd - odd_const) < 0.04
    assert abs(sqrt(even_m)*qeven - even_const) < 0.04
    print('PASS:',nchecks,'finite graph instances and two asymptotic finite-sum checks')

if __name__ == '__main__':
    test()
