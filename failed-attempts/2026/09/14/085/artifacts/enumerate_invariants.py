"""Enumerate Gysin/Smith necessary invariants for M_{m,n,l} -> N=(CP1xCP2)#CP3.

Bases: H^2(N)=<alpha,beta,gamma>, H^4(N)=<u=ab,v=b^2,w=c^2>.
phi: H^2->H^4 matrix [[n,m,0],[0,n,0],[0,0,l]]; psi row [n,m,l].
H^4(M)=coker(phi) via Smith normal form; spin <=> m,n odd and l even
(w2(M)=pi^*(beta) mod e; corrected parity). p1(N)=3v+4w, <e cup p1>[N]=3m+4l.
"""
from math import gcd
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from collections import defaultdict


def smith_diag(m, n, l):
    M = sp.Matrix([[n, m, 0], [0, n, 0], [0, 0, l]])
    S = smith_normal_form(M, domain=sp.ZZ)
    return tuple(sorted(abs(int(S[i, i])) for i in range(3)))


def is_spin(m, n, l):
    return (m % 2 == 1) and (n % 2 == 1) and (l % 2 == 0)


def main():
    trips = [(m, n, l) for m in range(-2, 3) for n in range(-2, 3)
             for l in range(-2, 3)
             if not (m == 0 and n == 0 and l == 0)
             and gcd(gcd(abs(m), abs(n)), abs(l)) == 1]
    by = defaultdict(list)
    for t in trips:
        m, n, l = t
        d = smith_diag(m, n, l)
        free = d.count(0)
        tors = tuple(x for x in d if x not in (0, 1))
        by[(free, tors, is_spin(m, n, l))].append(t)
    for k in sorted(by):
        print(k, len(by[k]), by[k][:12])
    # collision witnesses: same (free, torsion, spin), distinct triples
    print("collision example H4=0 non-spin:", [t for t in by[(0, (), False)][:8]])
    print("p1-pairing check: <e cup p1>[N] = 3m+4l; sign(N)=1")


if __name__ == "__main__":
    main()
