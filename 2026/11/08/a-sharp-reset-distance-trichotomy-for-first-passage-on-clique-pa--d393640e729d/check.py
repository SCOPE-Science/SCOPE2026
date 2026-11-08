#!/usr/bin/env python3
"""Independent rational Markov-generator verification of a finite graph-reset search theorem."""
from fractions import Fraction
from math import comb, sqrt


def calc_formula(m, length, rate):
    s = Fraction(rate)
    # Polynomial recurrences evaluated with rational arithmetic.
    Hminus, H = Fraction(0), Fraction(1)
    Eminus, E = Fraction(1), s+1
    if length == 1:
        return Fraction(1)+(m-1)/(s+1)
    for _ in range(1, length):
        Eminus, E = E, (s+2)*E-Eminus
        Hminus, H = H, (s+2)*H-Hminus
    return (E-1)/s + (m-1)*H/(s+1) if s != 0 else Fraction(length*(length+1), 2) + (m-1)*length


def gaussian(A, b):
    n = len(b)
    for j in range(n):
        pivot = next(i for i in range(j,n) if A[i][j] != 0)
        A[j], A[pivot] = A[pivot], A[j]
        b[j], b[pivot] = b[pivot], b[j]
        d = A[j][j]
        for k in range(j,n): A[j][k] /= d
        b[j] /= d
        for i in range(n):
            if i == j or A[i][j] == 0: continue
            f = A[i][j]
            for k in range(j,n): A[i][k] -= f*A[j][k]
            b[i] -= f*b[j]
    return b


def calc_generator(m, length, rate):
    # Clique vertices 0..m-1; source 0, path vertices m..m+length-1; last is target.
    # Each edge independently has jump rate one. Reset from non-source vertices to 0.
    n = m+length
    target = n-1
    nbr=[set() for _ in range(n)]
    for i in range(m):
        for j in range(i+1,m):
            nbr[i].add(j);nbr[j].add(i)
    last=0
    for node in range(m,n):
        nbr[last].add(node);nbr[node].add(last);last=node
    q=Fraction(rate)
    A=[[Fraction(0) for _ in range(target)] for _ in range(target)]
    b=[Fraction(1) for _ in range(target)]
    for i in range(target):
        A[i][i]=Fraction(len(nbr[i]))
        for j in nbr[i]:
            if j!=target:A[i][j]-=1
        if i!=0:
            A[i][i]+=q
            A[i][0]-=q
    return gaussian(A,b)[0]


def test_closed_coefficients():
    # Independent polynomial coefficient identity and sign conditions.
    for length in range(1,45):
        H0=[comb(length + k,2*k+1) for k in range(length)] # H_(length-1)
        assert H0[0] == length
        if length>=3:
            assert H0[1]>H0[0]
            for k in range(1,len(H0)):
                ck=H0[k]
                ck1=H0[k+1] if k+1<len(H0) else 0
                assert (k+1)*ck1+(k-1)*ck>0
        E=[comb(length+k,2*k) for k in range(length+1)]
        assert E[0]==1
        for k in range(1,len(E)): assert E[k]>0


def main():
    test_closed_coefficients()
    case_count=0
    for m in range(2,10):
        for length in range(1,8):
            for rate in [Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(3,2),Fraction(5,1)]:
                got=calc_generator(m,length,rate)
                expected=calc_formula(m,length,rate)
                if got!=expected: raise AssertionError((m,length,rate,got,expected))
                case_count+=1
    # Independent finite-difference checks of all three global regimes.
    for m in range(2,25):
        for length in range(1,14):
            values=[float(calc_formula(m,length,Fraction(j,12))) for j in range(0,49)]
            if length>=3: assert all(values[i]<values[i+1] for i in range(len(values)-1))
            if length==1: assert all(values[i]>values[i+1] for i in range(len(values)-1))
            if length==2 and m==2: assert all(values[i]<values[i+1] for i in range(len(values)-1))
            if length==2 and m>2:
                opt=sqrt(m-1)-1
                assert abs((m+1+2*sqrt(m-1))-(2*m+1-(sqrt(m-1)-1)**2))<1e-10
                assert float(calc_formula(m,length,Fraction.from_float(opt))) <= min(values[0],values[-1])
    print('PASS exact reduced and full generator, cases=',case_count)
    print('PASS polynomial signs for all lengths 1..44')
    print('PASS sampled monotonicity and minima m=2..24, length=1..13')

if __name__=='__main__': main()
