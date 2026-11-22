#!/usr/bin/env python3
"""Finite, reproducible checks for arithmetic progressions at Motzkin nondivisibility indices.
No numerical range check is used as a proof of the all-depth claims.
"""
from collections import Counter
from math import comb


def ternary01(r):
    return {sum(((j >> i) & 1) * 3**i for i in range(r)) for j in range(2**r)}


def model(r):
    t = ternary01(r)
    B = {3*u+j for u in t for j in (0, 1, 2)}
    S = {x-2 for x in B if x>=2}
    return B,S


def profiles(s, lengths=(3, 4, 5, 6, 7)):
    z = sorted(s)
    c = {}
    for k in lengths:
        ct = Counter()
        for a in z:
            for b in z:
                if b <= a:
                    continue
                d=b-a
                if all(a+i*d in s for i in range(2, k)):
                    ct[d]+=1
        c[k] = ct
    return c


def expected(r):
    a3={1:2**(r+1)-2,2:2**r-2}
    a4={1:3*2**(r-1)-2}
    for j in range(2,r+1):
        a3[(3**j-1)//2] = 2**(r-j+1)-1
        a3[(3**j+1)//2] = 2**(r-j+1)-1
        a4[(3**j-1)//2] = 2**(r-j)-1
    a5={1:2**r-2}
    a6={1:2**(r-1)-1}
    return {3:Counter({k:v for k,v in a3.items() if v}),
            4:Counter({k:v for k,v in a4.items() if v}),
            5:Counter({k:v for k,v in a5.items() if v}),
            6:Counter({k:v for k,v in a6.items() if v}),
            7:Counter()}


def check():
    assertions=0
    motz=[1,1]
    for n in range(2,130):
        motz.append(motz[n-1]+sum(motz[i]*motz[n-2-i] for i in range(n-1)))
    for n,v in enumerate(motz):
        if n==0:
            present=True
        else:
            u=(n+2)//3
            present=(n+2)%3 in (0,1,2) and u>=1 and all(int(z) in (0,1) for z in base3(u))
            # n+2 in 3T+[0,1,2], and u=floor((n+2)/3)
        assert (v%3 != 0)==present,(n,v%3,present)
        assertions+=1
    for r in range(1,9):
        B,S=model(r)
        bound=(3**(r+1)-1)//2
        assert max(S)==bound-1
        assertions+=1
        P=profiles(S)
        E=expected(r)
        assert P==E,(r,P,E)
        assertions+=1
        expected_counts={3:5*2**r-2*r-6,4:2**(r+1)-r-2,5:2**r-2,6:2**(r-1)-1,7:0}
        assert {k:sum(v.values()) for k,v in P.items()} == expected_counts
        assertions+=1
        if r>=2:
            X,_=model(r-1)
            q=3**r
            L=(q+1)//2
            cross={k:[] for k in (3,4,5,6,7)}
            Q=profiles(B)
            for k in (3,4,5,6,7):
                for d,count in Q[k].items():
                    for a in B:
                        if all(a+i*d in B for i in range(k)) and a<q<=a+(k-1)*d:
                            cross[k].append((a,d))
            expected_cross={3:[(0,L),(1,L-1),(L-1,L),(L,L-1)],4:[(1,L-1)],5:[],6:[],7:[]}
            for k in cross:
                assert sorted(cross[k])==sorted(expected_cross[k]), (r,k,cross[k])
                assertions+=1
    print(f'PASS: {assertions} independent groups of exact checks, all-depth proof supplied separately')
    for r in range(1,7):
        print(f'r={r}: AP3={5*2**r-2*r-6}, AP4={2**(r+1)-r-2}, AP5={2**r-2}, AP6={2**(r-1)-1}')


def base3(x):
    if x==0:return '0'
    s=''
    while x:s=str(x%3)+s;x//=3
    return s

if __name__=='__main__':
    check()
