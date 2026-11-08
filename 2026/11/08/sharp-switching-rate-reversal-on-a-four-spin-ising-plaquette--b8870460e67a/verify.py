#!/usr/bin/env python3
"""Exact rational checks for a four-site Ising cycle under bath switching.

Only Python's standard library is required. The proof of the theorem is
analytical, not an inference from the finite parameter checks here.
"""
from fractions import Fraction as F
from itertools import product


def cold(t):
    z = F(0)
    return [
        [-4/t, t, z, z],
        [4/t, -t-2-1/t, F(4), 4*t],
        [z, F(2), F(-4), z],
        [z, 1/t, z, -4*t],
    ]


def solve(a, b):
    n = len(b)
    a = [list(map(F, row)) + [F(rhs)] for row, rhs in zip(a,b)]
    for j in range(n):
        pivot = next(k for k in range(j,n) if a[k][j])
        a[j], a[pivot] = a[pivot], a[j]
        p = a[j][j]
        a[j] = [x/p for x in a[j]]
        for i in range(n):
            if i != j and a[i][j]:
                c = a[i][j]
                a[i] = [x-c*y for x,y in zip(a[i], a[j])]
    return [r[-1] for r in a]


def quotient_energy(u, gamma):
    matrices = [cold(u), cold(F(1))]
    a = [[F(0) for _ in range(8)] for _ in range(8)]
    for b in range(2):
        for j in range(4):
            for i in range(4):
                a[4*b+i][4*b+j] += matrices[b][i][j]
            a[4*b+j][4*b+j] -= gamma
            a[4*(1-b)+j][4*b+j] += gamma
    a[-1] = [F(1)]*8
    p = solve(a, [F(0)]*7+[F(1)])
    return -4*(p[0]+p[4])+4*(p[3]+p[7])


def spin_energy(s):
    return -sum(s[i]*s[(i+1)%4] for i in range(4))


def full_energy(u, gamma):
    configurations = list(product((-1,1), repeat=4))
    lookup = {s:i for i,s in enumerate(configurations)}
    matrix = [[F(0) for _ in range(32)] for _ in range(32)]
    for bath,t in enumerate((u,F(1))):
        for j,s in enumerate(configurations):
            ind = 16*bath+j
            e = spin_energy(s)
            for k in range(4):
                changed = list(s)
                changed[k] = -changed[k]
                i = lookup[tuple(changed)]
                delta = spin_energy(changed)-e
                assert delta in (-4,0,4)
                rate = {4:1/t, 0:F(1), -4:t}[delta]
                matrix[16*bath+i][ind] += rate
                matrix[ind][ind] -= rate
            matrix[16*(1-bath)+j][ind] += gamma
            matrix[ind][ind] -= gamma
    matrix[-1] = [F(1)]*32
    p = solve(matrix, [F(0)]*31+[F(1)])
    return sum(F(spin_energy(configurations[i%16]))*p[i] for i in range(32))


def formula(u, gamma):
    w = u+1/u
    s = u-1/u
    b = (w+2)*gamma**2+(9*w+6)*gamma+16*w
    d = ((w+2)*(w+6)*gamma**3
         +2*(w+2)*(7*w+18)*gamma**2
         +8*(7*w*w+14*w+24)*gamma+64*(w*w+4))
    return -4*s*(gamma+2)*b/d


def ppoly(w,g):
    return (3*(w*w-4)*g**4+4*(11*w*w-8*w-60)*g**3
            +4*(59*w*w-116*w-324)*g**2
            +256*(2*w*w-7*w-10)*g+128*(3*w*w-16*w-12))


def derivative(u,g):
    w=u+1/u
    b=(w+2)*g*g+(9*w+6)*g+16*w
    db=2*(w+2)*g+(9*w+6)
    d=(w+2)*(w+6)*g**3+2*(w+2)*(7*w+18)*g*g+8*(7*w*w+14*w+24)*g+64*(w*w+4)
    dd=3*(w+2)*(w+6)*g*g+4*(w+2)*(7*w+18)*g+8*(7*w*w+14*w+24)
    return -4*(u-1/u)*((b+(g+2)*db)*d-(g+2)*b*dd)/d**2


def test():
    n=0
    for u in [F(3,2),F(2),F(4),F(10)]:
        for gamma in [F(1,5),F(3,2),F(7)]:
            assert quotient_energy(u,gamma)==formula(u,gamma)
            w=u+1/u
            assert derivative(u,gamma) == -4*(w-2)*(u-1/u)*ppoly(w,gamma)/(
                ((w+2)*(w+6)*gamma**3+2*(w+2)*(7*w+18)*gamma**2
                +8*(7*w*w+14*w+24)*gamma+64*(w*w+4))**2)
            n+=2
    for u,gamma in [(F(3,2),F(1,5)),(F(2),F(3,2)),(F(4),F(7)),(F(10),F(1))]:
        assert full_energy(u,gamma)==formula(u,gamma)
        n+=1
    assert ppoly(F(6),F(0))==0
    for v in (F(3),F(4),F(5),F(6),F(7),F(8)):
        assert (ppoly(v,F(0))<0)==(v<6)
        n+=1
    print('PASS:',n,'exact rational assertions; quotient/full generators and derivative')

if __name__=='__main__': test()
