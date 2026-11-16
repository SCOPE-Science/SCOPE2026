#!/usr/bin/env python3
"""Exact integer checks for the signed 6-cycle Fourier polynomial on K_(3,n)."""
import itertools
import math
from fractions import Fraction

def fc(n):
    return math.factorial(n)

def formula(types):
    n=len(types)
    # column types are (x,y,z)=(+,+,+),(+,-,-),(-,+,-),(-,-,+)
    xyz=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))
    sx=sum(xyz[t][0] for t in types)
    sy=sum(xyz[t][1] for t in types)
    sz=sum(xyz[t][2] for t in types)
    return sx*sy*sz-sx*sx-sy*sy-sz*sz+2*n

def multinomial(n):
    moments=0; abs_sum=0; zero_count=0
    for a in range(n+1):
      for b in range(n-a+1):
       for c in range(n-a-b+1):
        d=n-a-b-c
        m=fc(n)//(fc(a)*fc(b)*fc(c)*fc(d))
        sx=a+b-c-d; sy=a-b+c-d; sz=a-b-c+d
        w=sx*sy*sz-sx*sx-sy*sy-sz*sz+2*n
        abs_sum+=m*abs(w); moments+=m*w*w
        if w==0:zero_count+=m
        if n%4==3:assert w%4==2
        if n%8==6:assert w%16==8
    assert moments==4**n*n*(n-1)*(n-2)
    return Fraction(abs_sum,4**n),Fraction(zero_count,4**n)

def direct(n):
    N=1<<(3*n)
    f=[0]*N
    pairs=((0,1),(0,2),(1,2))
    for cols in itertools.combinations(range(n),3):
      for perm in itertools.permutations(cols):
        mask=0
        for (u,v),j in zip(pairs,perm):
          mask |= 1<<(3*j+u)
          mask |= 1<<(3*j+v)
        assert f[mask]==0
        f[mask]=1
    assert sum(f)==n*(n-1)*(n-2)
    for bit in range(3*n):
      half=1<<bit
      for start in range(0,N,2*half):
        for j in range(start,start+half):
          u=f[j];v=f[j+half]
          f[j]=u+v;f[j+half]=u-v
    tlist=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))
    for neg in range(N):
      types=[]
      for j in range(n):
        a=-1 if neg>>(3*j)&1 else 1
        b=-1 if neg>>(3*j+1)&1 else 1
        c=-1 if neg>>(3*j+2)&1 else 1
        types.append(tlist.index((a*b,a*c,b*c)))
      z=formula(types)
      assert f[neg]==z,(n,neg,z,f[neg])
    l,z=multinomial(n)
    assert sum(abs(v) for v in f)*l.denominator==l.numerator*N
    assert sum(v==0 for v in f)*z.denominator==z.numerator*N
    print(f'BRUTE_WALSH_PASS n={n} |C|={n*(n-1)*(n-2)} norm={l} zero_fraction={z}')

if __name__=='__main__':
    for n in range(3,7): direct(n)
    for n in range(3,71):
        l,z=multinomial(n)
        if n in (3,4,5,6,7,8,9,10,11,14,19,22,30,38,46,54,62,70):
            print(f'EXACT_SUM_PASS n={n} norm={l} zero_fraction={z}')
    print('SIX_CYCLE_ORBIT_EXACT_WALSH_AND_RESIDUE_TESTS_PASS')
