#!/usr/bin/env python3
"""Finite-field direct checks for cyclic radical-square-zero representations.
No external dependencies. Usage: python3 verify.py
"""
from itertools import product
from math import prod

def gaussian(n,k,q):
    if not 0 <= k <= n: return 0
    num=prod(q**(n-j)-1 for j in range(k))
    den=prod(q**(k-j)-1 for j in range(k))
    return num//den

def gl(r,q):
    return prod(q**r-q**j for j in range(r))

def strata(n,d,q):
    result={}
    for r in product(range(d+1),repeat=n):
        if any(r[i-1]+r[i]>d for i in range(n)):continue
        val=prod(gaussian(d,r[i-1],q)*gaussian(d-r[i-1],r[i],q)*gl(r[i],q) for i in range(n))
        assert val>0
        result[r]=val
    return result

def mmul(a,b,d,q):
    return tuple(sum(a[i*d+k]*b[k*d+j] for k in range(d))%q for i in range(d) for j in range(d))

def rank(a,d,q):
    A=[[a[i*d+j]%q for j in range(d)] for i in range(d)]
    pivot=0
    for j in range(d):
        s=next((i for i in range(pivot,d) if A[i][j]),None)
        if s is None: continue
        A[pivot],A[s]=A[s],A[pivot]
        inv=pow(A[pivot][j],-1,q)
        A[pivot]=[(v*inv)%q for v in A[pivot]]
        for i in range(pivot+1,d):
            c=A[i][j]
            A[i]=[(a-c*b)%q for a,b in zip(A[i],A[pivot])]
        pivot+=1
        if pivot==d:break
    return pivot

def direct(n,d,q):
    assert q in (2,3,5,7)
    mats=list(product(range(q),repeat=d*d))
    zero=(0,)*(d*d)
    ranks={a:rank(a,d,q) for a in mats}
    compatible={(a,b):mmul(b,a,d,q)==zero for a in mats for b in mats}
    counts={}
    for seq in product(mats,repeat=n):
        if any(not compatible[(seq[i-1],seq[i])] for i in range(n)):continue
        r=tuple(ranks[a] for a in seq)
        counts[r]=counts.get(r,0)+1
    return counts

def leading_profiles(n,d):
    good=[]
    for r in product(range(d+1),repeat=n):
        s=tuple(d-r[i-1]-r[i] for i in range(n))
        if min(s)<0:continue
        good.append((sum(z*z for z in s),r,s))
    best=min(x[0] for x in good)
    return best,[(r,s) for v,r,s in good if v==best]

def main():
    for n,d,q in [(2,1,2),(2,2,2),(2,2,3),(3,1,2),(3,1,3),(3,2,2),(4,1,2),(4,1,3),(5,1,2),(5,1,3)]:
        want=strata(n,d,q)
        got=direct(n,d,q)
        assert want==got,(n,d,q,set(want.items())^set(got.items()))
        print('BRUTE_OK',n,d,q,'representations',sum(want.values()),'profiles',len(want))
    for n in range(2,8):
        for d in range(1,6 if n<=4 else 4):
            best,prof=leading_profiles(n,d)
            expected= ([(tuple(r if i%2==0 else d-r for i in range(n)),(0,)*n) for r in range(d+1)] if n%2==0 else
                ([( (d//2,)*n,(0,)*n)] if d%2==0 else []))
            if n%2==1 and d%2==1:
                assert best==1 and len(prof)==n
                assert all(sum(s)==1 for r,s in prof)
                assert len({s.index(1) for r,s in prof})==n
            else:
                assert best==0 and set(prof)==set(expected),(n,d,prof,expected)
            assert all(sum(z*z for z in s)==best for r,s in prof)
    print('ASYMPTOTIC_LEADING_PROFILES_OK n=2..7 d up to 5')
    print('VERIFY_OK')

if __name__=='__main__':main()
