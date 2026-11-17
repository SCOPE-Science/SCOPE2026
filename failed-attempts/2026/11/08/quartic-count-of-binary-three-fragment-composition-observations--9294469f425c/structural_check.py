#!/usr/bin/env python3
"""Check exact run-parameter enumeration and its rational generating series.
Independent of the direct word enumeration; only standard-library integers.
"""
from fractions import Fraction


def formula(n):
    if n==1:
        return 2
    c=(480,555,456,555)[n%4]
    return (3*n**4-16*n**3+114*n**2-272*n+c)//96


def run_count(n):
    total=2  # all-zero and all-one words
    # Include all alternating run-count pairs with both symbols present.
    for p in range(1,n+1):
        for q in range(max(1,p-1), min(n,p+1)+1):
            if p+q>n:
                continue
            for e0 in range(p+1):
                min0=2*p-e0
                for e1 in range(q+1):
                    min1=2*q-e1
                    if e0==p and e1==q:
                        ways_length=int(n==p+q)
                    elif e0==p:
                        ways_length=int(n-p>=min1)
                    elif e1==q:
                        ways_length=int(n-q>=min0)
                    else:
                        ways_length=max(0,n-min0-min1+1)
                    if not ways_length:
                        continue
                    if p==q:
                        mult=1+int(0<e0<p)+int(0<e1<q)
                    elif p==q+1:
                        mult=1+int(1<=e0<=p-2)+int(2<=e0<=p-1)
                    else:
                        mult=1+int(1<=e1<=q-2)+int(2<=e1<=q-1)
                    total+=ways_length*mult
    return total


def rational_coefficients(N):
    # P(z)/((1-z)^4(1-z^4)), with the numerator P(z) below.
    p=[0,2,-5,6,-4,4,-1,2,-3,2]
    # (1-z)^4(1-z^4) = 1-4z+6z^2-4z^3+0z^4+3z^5-6z^6+4z^7-z^8
    q=[0]*9
    b=[1,-4,6,-4,1]
    for i,v in enumerate(b):
        q[i]+=v
        q[i+4]-=v
    a=[0]*(N+1)
    for n in range(1,N+1):
        a[n]=(p[n] if n<len(p) else 0)-sum(q[i]*a[n-i] for i in range(1,min(n,8)+1))
    return a


def check():
    coeff=rational_coefficients(80)
    for n in range(1,81):
        assert coeff[n]==formula(n),(n,coeff[n],formula(n))
    for n in range(1,43):
        x=run_count(n)
        assert x==coeff[n],(n,x,coeff[n])
    print('STRUCTURAL_OK: run decomposition through 42; rational identity through 80')


if __name__=='__main__':
    check()
