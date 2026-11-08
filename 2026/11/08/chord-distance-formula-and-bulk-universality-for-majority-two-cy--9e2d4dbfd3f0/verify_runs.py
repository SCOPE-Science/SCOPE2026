#!/usr/bin/env python3
"""Independent enumeration of boundary-stable words and Fibonacci/delta formulas."""
from itertools import product

def fib(n):
    x,y=0,1
    for i in range(n):x,y=y,x+y
    return x

def model(m):
    patterns=[]
    for q in product((0,1),repeat=m):
        if m==1 or (q[0]==q[1] and q[-2]==q[-1] and
                    all(not(q[i-1]==q[i+1]!=q[i]) for i in range(1,m-1))):
            patterns.append(q)
    E=sum(q[0]==0 and q[-1]==0 for q in patterns)
    O=sum(q[0]==0 and q[-1]==1 for q in patterns)
    assert len(patterns)==2*(E+O)
    return E,O

def fA(m):return 1 if m==1 else fib(m-1)
def fD(m):return 1 if m==1 else (1,1,0,-1,-1,0)[(m-2)%6]

def main():
    for m in range(1,18):
        E,O=model(m)
        assert E+O==fA(m),(m,E,O)
        assert E-O==fD(m),(m,E,O)
        print(f'm={m} same={E} opposite={O} A={E+O} D={E-O}')
    # Algebraic generating functions for m>=2:
    #  sum (E+O) z^m = z^2/(1-z-z^2)
    #  sum (E-O) z^m = z^2/(1-z+z^2).
    # Check the defining recurrences on coefficients through 100.
    A=[0]*101; D=[0]*101
    for m in range(2,101):
        A[m]=fib(m-1)
        D[m]=(1,1,0,-1,-1,0)[(m-2)%6]
    for m in range(4,101):
        assert A[m]-A[m-1]-A[m-2]==0
        assert D[m]-D[m-1]+D[m-2]==0
    print('PASS: boundary-word enumeration m=1..17, plus exact coefficient recurrences m=4..100')
if __name__=='__main__':main()
