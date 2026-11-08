#!/usr/bin/env python3
"""Pure-Python verification of a ternary linear bigram-spectrum rational series.

This code counts matrices, not source words, using independent Euler-trail criteria.
"""
from itertools import product
from math import comb

NUM = [1, 5, -8, 8, 13, -4, -10, -8, 11, 2, -5, 2]

def multiply(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out

def power(a,k):
    p=[1]
    for _ in range(k): p=multiply(p,a)
    return p

DEN=multiply(multiply(power([1,-1],7),power([1,1],2)),[1,1,1])

def coefficients(max_m):
    c=[]
    for m in range(max_m+1):
        c.append((NUM[m] if m<len(NUM) else 0)-sum(DEN[j]*c[m-j] for j in range(1,min(m,len(DEN)-1)+1)))
    return c

def compositions(total,k):
    if k==1:
        yield (total,)
        return
    for a in range(total+1):
        for rest in compositions(total-a,k-1):
            yield (a,)+rest

def euler_trail_exists(mat):
    out=[sum(mat[i*3:(i+1)*3]) for i in range(3)]
    incoming=[sum(mat[i*3+j] for i in range(3)) for j in range(3)]
    delta=[out[i]-incoming[i] for i in range(3)]
    if sorted(delta) not in ([0,0,0],[-1,0,1]):return False
    active={i for i in range(3) if out[i]+incoming[i]>0}
    if not active:return True
    reached={next(iter(active))}
    frontier=list(reached)
    while frontier:
        a=frontier.pop()
        for b in active-reached:
            if mat[3*a+b] or mat[3*b+a]:
                reached.add(b)
                frontier.append(b)
    return reached==active

def main():
    expected=coefficients(10)
    observed=[]
    for m in range(10):
        amount=sum(1 for mat in compositions(m,9) if euler_trail_exists(mat))
        observed.append(amount)
        assert amount==expected[m],(m,amount,expected[m])
    assert expected[:10]==[1,9,24,65,156,342,683,1272,2226,3708]
    print('MATRIX_ENUM_OK',observed)
    print('RATIONAL_COEFFS_OK',coefficients(20))
if __name__=='__main__':main()
