#!/usr/bin/env python3
"""Independent exhaustive Rule 22 check for every binary ring through size twenty.
Standard-library Python 3.10+. Run: python3 bruteforce.py
"""
from collections import Counter

def step(x,n):
    mask=(1<<n)-1
    a=((x<<1)|(x>>(n-1)))&mask
    c=((x>>1)|(x<<(n-1)))&mask
    return (a^x^c)&~(a&x&c)&mask

def tr_four_minus_two(n):
    total=0
    for x in range(1<<n):
        b=step(x,n);c=step(b,n)
        if c==x:continue
        d=step(c,n);e=step(d,n)
        total+=(e==x)
    assert total%4==0
    return total//4

def coeff_mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def recurrence(n,P):
    traces=[0]*(n+1)
    for k in range(1,n+1):
        traces[k]=-k*(P[k] if k<len(P) else 0)-sum(P[i]*traces[k-i] for i in range(1,min(k,len(P)-1)+1))
    assert traces[n]%2==0
    return traces[n]//2

def main():
    p=coeff_mul(coeff_mul([1,1],[1,-1,1,-1,0,-1]),[1,0,0,0,1,1,1])
    result=[]
    for n in range(3,21):
        predicted=recurrence(n,p)
        observed=tr_four_minus_two(n)
        assert observed==predicted,(n,observed,predicted)
        result.append((n,observed))
    print('PASS exhaustive direct bit-parallel Rule 22 enumeration at all circumferences 3..20')
    print('primitive-four temporal orbits by circumference:',result)
if __name__=='__main__':main()
