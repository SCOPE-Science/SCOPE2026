#!/usr/bin/env python3
"""Exact rational checks of the triangular-graph Radau IIA sign formulas."""
from fractions import Fraction as F
from itertools import combinations


def polynomials(n, h):
    h = F(h)
    D = (n*n*h*h + 4*n*h + 6)*(4*(n-1)**2*h*h + 8*(n-1)*h + 6)
    Q = (18 + 48*h + (-5*n*n + 26*n + 24)*h*h
         + (-2*n**3 - 2*n*n + 40*n - 24)*h**3
         + 4*n*(n-1)*h**4)
    E = (36 + (18*n+60)*h - 4*(n*n-19*n+12)*h*h
         + 8*n*(n-1)*h**3)
    H = 4*h*h*(2*n*(n-1)*h*h + 6*(3*n-2)*h + 18)
    return D, Q, E, H


def structured(n, h, adjacent):
    D, Q, E, H = polynomials(n, h)
    N = n*(n-1)//2
    return [[(2*Q if i == j else h*E if adjacent[i][j] else H)/D
             for j in range(N)] for i in range(N)]


def matmul(A, B):
    m = len(A)
    return [[sum((A[i][k]*B[k][j] for k in range(m)), F(0))
             for j in range(m)] for i in range(m)]


def graph_and_system(n, h):
    vertices = list(combinations(range(n), 2)); N=len(vertices)
    neighbor = [[i!=j and bool(set(vertices[i]) & set(vertices[j]))
                 for j in range(N)] for i in range(N)]
    degree = 2*(n-2)
    L=[[F(degree if i==j else -1 if neighbor[i][j] else 0)
        for j in range(N)] for i in range(N)]
    L2=matmul(L,L)
    B = [[6*(i==j)+4*h*L[i][j]+h*h*L2[i][j]
          for j in range(N)] for i in range(N)]
    A = [[6*(i==j)-2*h*L[i][j] for j in range(N)] for i in range(N)]
    return neighbor, B, A


def cubic_discriminant(a,b,c,d):
    return 18*a*b*c*d-4*b**3*d+b*b*c*c-4*a*c**3-27*a*a*d*d


def run():
    count=0
    for n in range(4,9):
        for h in (F(1,17),F(1,5),F(1,2),F(1),F(2)):
            neighbor, B, A = graph_and_system(n,h)
            T=structured(n,h,neighbor)
            assert matmul(B,T)==A, (n,h,'matrix identity')
            assert all(sum(row)==1 for row in T), (n,h,'mass')
            assert T==list(map(list,zip(*T))), (n,h,'symmetry')
            count+=1
    # A sharp diagonal boundary (the polynomial at h=1 is negative from n=6 onward).
    for n in range(6,401):
        D,Q,E,H=polynomials(n,F(1))
        assert Q == -2*n**3-3*n*n+62*n+66
        assert Q<0
        count+=1
    # Universal positive nonedges (for every positive n and h all factors >0).
    for n in range(4,201):
        for h in (F(1,100),F(1,5),F(1),F(100)):
            D,Q,E,H=polynomials(n,h)
            assert D>0 and H>0
            count+=1
    # The last globally edge-positive case: one negative and two nonreal roots.
    assert cubic_discriminant(43216,-16328,1392,36) == -24660792741888
    # Disjoint, nonempty positivity-failure band for every n>=75.
    for n in range(75,1001):
        D,Q,E,H=polynomials(n,F(1,5))
        assert E == F(-6*(2*n*n-137*n-960),125) and E<0
        count+=1
    # Two small-size unconditional cases: exact polynomial certificates.
    for h in (F(j,30) for j in range(0,901)):
        _,q4,_,_=polynomials(4,h)
        assert q4 == 18+48*h+45*h*h+3*h*h*(4*h-1)**2
        _,q5,_,_=polynomials(5,h)
        if h <= F(3,4):
            assert q5 >= 18+48*h-64*h*h >=18
        else:
            t=h-F(3,4)
            assert q5 == 80*t**4+116*t**3+20*t*t+F(69,4)*t+F(693,16)>0
        count+=1
    # Exact broad parameter sign checks of all three transition types.
    for n in range(4,151):
        for h in (F(1,100),F(1,5),F(1),F(2),F(20)):
            D,Q,E,H=polynomials(n,h)
            assert D>0 and H>=0
            assert 2*Q+2*(n-2)*h*E+F((n-2)*(n-3),2)*H == D
            if n<=74: assert E>0
            if n<=5: assert Q>0
            count+=1
    print('PASS:',count,'exact-rational checks; 25 full-matrix rational identities; distinct 6/75 transitions')

if __name__=='__main__': run()
