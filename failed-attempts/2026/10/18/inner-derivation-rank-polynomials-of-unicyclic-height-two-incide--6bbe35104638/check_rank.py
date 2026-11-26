"""Standalone exact check for finite incidence-algebra inner-derivation ranks.
Usage: python3 check_rank.py. No third-party packages needed.
"""
from collections import Counter
from itertools import product
from math import comb


def rank_mod_p(matrix, p):
    a = [row[:] for row in matrix]
    r = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][col] % p), None)
        if pivot is None:
            continue
        a[pivot], a[r] = a[r], a[pivot]
        inv = pow(a[r][col] % p, -1, p)
        a[r] = [(inv * x) % p for x in a[r]]
        for i in range(r+1, len(a)):
            coeff = a[i][col]
            if coeff:
                a[i] = [(u - coeff * v) % p for u,v in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def polynomial(n_edges, length, q):
    """Element-indexed formula: unique even cycle length and t attached edges."""
    t = n_edges - length
    A = [comb(n_edges, k) * (q*q-1)**k for k in range(n_edges+1)]
    B = [comb(length, k) * (-1)**k for k in range(length+1)]
    for _ in range(t):
        B1 = [0]*(len(B)+1)
        for j, v in enumerate(B):
            B1[j] += v
            B1[j+1] += (q*q-1)*v
        B = B1
    for j, v in enumerate(B):
        A[j] += (q-1)*v
    correction = [0]*(length+1)
    correction[length-1] = q*(q-1)**length
    correction[length] = -q*(q-1)**length
    for _ in range(t):
        C = [0]*(len(correction)+1)
        for j, v in enumerate(correction):
            C[j] += v
            C[j+1] += (q*q-1)*v
        correction = C
    for j, v in enumerate(correction):
        A[j] += v
    return A


def enumerate_by_multiplication(n, edges, p):
    """Direct products of basis matrix units, then linear rank of ad(a)."""
    basis = [(v, v) for v in range(n)] + list(edges)
    index = {unit:i for i,unit in enumerate(basis)}
    size = len(basis)
    # For each basis coefficient of a, precompute its commutator with each basis vector.
    tensors = []
    for u,(r,s) in enumerate(basis):
        slice_u = [[0]*size for _ in range(size)]
        for col,(v,w) in enumerate(basis):
            if s == v and (r,w) in index:
                slice_u[index[(r,w)]][col] += 1
            if w == r and (v,s) in index:
                slice_u[index[(v,s)]][col] -= 1
        tensors.append(slice_u)
    result = Counter()
    for a in product(range(p), repeat=size):
        M = [[0]*size for _ in range(size)]
        for coeff, slice_u in zip(a,tensors):
            if coeff:
                for i in range(size):
                    for j in range(size):
                        M[i][j] += coeff*slice_u[i][j]
        result[rank_mod_p(M,p)] += 1
    return [result.get(k,0) for k in range(len(edges)+1)]


def check_case(name,n,edges,length,q):
    expected=polynomial(len(edges),length,q)
    observed=enumerate_by_multiplication(n,edges,q)
    assert expected == observed,(name,q,expected,observed)
    assert sum(observed)==q**(n+len(edges))
    assert observed[0]==q
    assert observed[1]==q*len(edges)*(q*q-1)-q*q*(q-1)*length
    assert all(c%q==0 for c in observed)
    cpairs=sum(count * q**(n+len(edges)-r) for r,count in enumerate(observed))
    m=len(edges);t=m-length
    formula=q**m*((q*q+q-1)**m+(q+1)*(q-1)**(length+1)*(q*q+q-1)**t)
    assert cpairs==formula,(cpairs,formula)
    print('PASS',name,'q=',q,'coefficients=',observed,'commuting_pairs=',cpairs)


C4=[(0,1),(2,1),(2,3),(0,3)]
C6=[(0,1),(2,1),(2,3),(4,3),(4,5),(0,5)]
if __name__=='__main__':
    for q in (2,3):
        check_case('cycle-4',4,C4,4,q)
        check_case('cycle-4-leaf',5,C4+[(0,4)],4,q)
    check_case('cycle-4-two-leaves',6,C4+[(0,4),(5,4)],4,2)
    check_case('cycle-6',6,C6,6,2)
    print('ALL_EXACT_CHECKS_PASSED')
