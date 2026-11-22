#!/usr/bin/env python3
"""Exact modular chain-rank certificate for the finite three-cycle quandles.

Only Python's standard library is required. All nondegenerate triples are
enumerated and both Gaussian elimination pivots and chain identities checked.
"""
from collections import defaultdict
from itertools import permutations


def compose(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def inverse(a):
    v = [0]*len(a)
    for i, j in enumerate(a):
        v[j] = i
    return tuple(v)


def three_cycles(n):
    out = set()
    for a, b, c in permutations(range(n), 3):
        t = list(range(n))
        t[a], t[b], t[c] = b, c, a
        out.add(tuple(t))
    return sorted(out)


def make_table(Q):
    indices = {p:i for i,p in enumerate(Q)}
    inv = [inverse(p) for p in Q]
    T = [[indices[compose(compose(inv[j], Q[i]), Q[j])]
          for j in range(len(Q))] for i in range(len(Q))]
    return T


def chain_data(n):
    Q = three_cycles(n)
    size = len(Q)
    assert size == n*(n-1)*(n-2)//3
    T = make_table(Q)
    assert all(T[i][i] == i for i in range(size))
    assert all(len(set(T[i][j] for i in range(size))) == size for j in range(size))
    for i in range(size):
        for j in range(size):
            for k in range(size):
                assert T[T[i][j]][k] == T[T[i][k]][T[j][k]]
    # Graph of the degree-2 boundaries (x)-(x*y) is connected.
    found = {0}
    while True:
        extra = {T[i][j] for i in found for j in range(size)} - found
        if not extra:
            break
        found.update(extra)
    assert len(found) == size
    pairs = [(i,j) for i in range(size) for j in range(size) if i != j]
    idx = {v:i for i,v in enumerate(pairs)}
    return T,pairs,idx


def normalized_boundary(i, j, k, T, idx):
    # Quandle degree-three boundary:
    # (i,k) - (i*j,k) - (i,j) + (i*k,j*k).
    terms = [(1, (i,k)), (-1, (T[i][j],k)),
             (-1, (i,j)), (1, (T[i][k],T[j][k]))]
    answer = defaultdict(int)
    for coeff, pair in terms:
        if pair[0] != pair[1]:
            answer[idx[pair]] += coeff
    return {key:val for key,val in answer.items() if val}


def plus_trinary(v, w):
    a1,a2 = v
    b1,b2 = w
    return ((a1 & ~(b1|b2)) | (b1 & ~(a1|a2)) | (a2 & b2),
            (a2 & ~(b1|b2)) | (b2 & ~(a1|a2)) | (a1 & b1))


def exact_rank(T, pairs, idx, prime, reverse=False, verify_boundary=False):
    n = len(T)
    width = len(pairs)
    pivots = {}
    columns = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            for k in range(n):
                if j == k:
                    continue
                col = normalized_boundary(i,j,k,T,idx)
                if verify_boundary:
                    # Verify d_2 d_3 = 0 with literal integer coefficients.
                    d2 = defaultdict(int)
                    for pos, coeff in col.items():
                        x,y = pairs[pos]
                        d2[x] += coeff
                        d2[T[x][y]] -= coeff
                    assert all(value == 0 for value in d2.values())
                if prime == 2:
                    v = 0
                    for pos, coeff in col.items():
                        if coeff & 1:
                            v |= 1 << (width-1-pos if reverse else pos)
                    while v:
                        p = v.bit_length()-1
                        if p not in pivots:
                            pivots[p] = v
                            break
                        v ^= pivots[p]
                else:
                    a1 = a2 = 0
                    for pos, coeff in col.items():
                        row = width-1-pos if reverse else pos
                        r = coeff % 3
                        if r == 1:
                            a1 |= 1 << row
                        elif r == 2:
                            a2 |= 1 << row
                    v = (a1,a2)
                    while v[0] or v[1]:
                        p = (v[0]|v[1]).bit_length()-1
                        b = pivots.get(p)
                        if b is None:
                            if (v[1] >> p) & 1:
                                v = (v[1],v[0])
                            pivots[p] = v
                            break
                        if (v[0] >> p) & 1:
                            v = plus_trinary(v, (b[1],b[0]))
                        else:
                            v = plus_trinary(v, b)
                columns += 1
    assert columns == n*(n-1)*(n-1)
    return len(pivots),columns


def main():
    known = {5:{2:360,3:360},6:{2:1520,3:1519},
             7:{2:4761,3:4759}}
    for n in (5,6,7):
        T,pairs,idx = chain_data(n)
        size = len(T)
        ranks = {}
        for prime in (2,3):
            r,count = exact_rank(T,pairs,idx,prime,
                                 verify_boundary=(prime == 3))
            assert r == known[n][prime]
            ranks[prime] = r
            # Reindex the complete nondegenerate pair basis in reverse.
            if n < 7 or prime == 2:
                rr,_ = exact_rank(T,pairs,idx,prime,reverse=True)
                assert rr == r
        d2 = size - 1
        h2 = {p:len(pairs)-d2-ranks[p] for p in (2,3)}
        print('n=%d cycles=%d C2=%d C3=%d d2=%d d3(F2)=%d d3(F3)=%d H2(F2)=%d H2(F3)=%d secondary-pivots=as-described d2d3=PASS'
              % (n,size,len(pairs),size*(size-1)**2,d2,
                 ranks[2],ranks[3],h2[2],h2[3]))
    print('EXACT EXHAUSTIVE RANK CERTIFICATE: PASS')


if __name__=='__main__':
    main()
