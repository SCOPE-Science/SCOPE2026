#!/usr/bin/env python3
"""Finite algebraic certificate for a fourth-order Fock kernel distance obstruction.

Run with Python 3; only the standard library is required. All arithmetic is exact.
"""
from fractions import Fraction as F
from itertools import permutations, product
from collections import Counter

PRIME = 53
ROOTS = (29, 40, 49)


def p(x):
    return x*x*x-12*x*x+36*x-24


def trim(a):
    while len(a)>1 and a[-1] == 0:
        a.pop()
    return a


def mul(a,b):
    out = [F(0)] * (len(a)+len(b)-1)
    for i,ai in enumerate(a):
        for j,bj in enumerate(b):
            out[i+j] += ai*bj
    return trim(out)


def compose(a,b):
    out = [F(0)]
    power = [F(1)]
    for ai in a:
        part = [ai*t for t in power]
        out += [F(0)] * max(0, len(part)-len(out))
        for i,coef in enumerate(part):
            out[i] += coef
        power = mul(power,b)
    return trim(out)


def rem(a):
    a = a[:]
    P = [F(-24),F(36),F(-12),F(1)]
    while len(a) > 3:
        lead = a[-1]
        for i,t in enumerate(P):
            a[len(a)-4+i] -= lead*t
        trim(a)
    return trim(a)


def det_gram(a,b,c,d,e,f):
    x,y,z = a+b-d, a+c-e, b+c-f
    return 8*a*b*c + 2*x*y*z - 2*a*z*z - 2*b*y*y - 2*c*x*x


def det_matrix(M):
    n=len(M)
    acc=0
    for pi in permutations(range(n)):
        inversions=sum(pi[i]>pi[j] for i in range(n) for j in range(i+1,n))
        v=1
        for i,j in enumerate(pi):
            v *= M[i][j]
        acc += -v if inversions%2 else v
    return acc


def det_cayley_menger(a,b,c,d,e,f):
    M = [[0,1,1,1,1],
         [1,0,a,b,c],
         [1,a,0,d,e],
         [1,b,d,0,f],
         [1,c,e,f,0]]
    return det_matrix(M)


def main():
    assert [j for j in range(PRIME) if p(j)%PRIME == 0] == list(ROOTS)
    # The minimal polynomial of any root is irreducible over Q by rational-root theorem.
    assert all(p(t) for t in list(range(-24,25)) if t and 24%abs(t)==0)
    # Polynomial T(X) cycles all three roots in the splitting field.
    T = [F(0),F(4),F(-1,2)]
    U = [F(12),F(-5),F(1,2)]
    P = [F(-24),F(36),F(-12),F(1)]
    assert rem(compose(P,T)) == [0]
    assert rem([a-b for a,b in zip(compose(T,T)+[0]*3,U+[0]*4)]) == [0]
    assert rem([a-b for a,b in zip(compose(T,U)+[0]*3,[F(0),F(1),F(0),F(0),F(0)])]) == [0]
    inv2=pow(2,-1,PRIME)
    def trans(x): return (4*x - x*x*inv2)%PRIME
    assert (trans(ROOTS[0]),trans(ROOTS[1]),trans(ROOTS[2])) == (40,49,29)

    residues=[]
    for ds in product(ROOTS,repeat=6):
        v1=det_gram(*ds)
        v2=det_cayley_menger(*ds)
        assert v1==v2, (ds,v1,v2)   # two structurally different exact determinants
        residue=v1%PRIME
        assert residue != 0, (ds,v1)
        residues.append(residue)
    assert len(residues)==3**6==729
    C=Counter(residues)
    assert len(C)==36
    assert [sum(v for k,v in C.items() if lo<=k<=hi) for lo,hi in
            [(1,13),(14,26),(27,39),(40,52)]] == [233,211,215,70]
    print('irreducible cubic and cyclic roots: PASS')
    print('mod 53 roots: 29,40,49; complete residue classes: PASS')
    print('Gram / Cayley-Menger determinant crosscheck: 729/729')
    print('nonzero mod 53: 729/729')
    print('residues represented:',len(C))
    print('residue-bin counts (1-13,14-26,27-39,40-52): 233,211,215,70')
    print('zero residues: 0')

if __name__=='__main__':
    main()
