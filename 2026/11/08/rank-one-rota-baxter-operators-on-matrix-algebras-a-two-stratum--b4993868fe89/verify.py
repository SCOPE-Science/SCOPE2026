#!/usr/bin/env python3
"""Finite-field checks for rank-one weight-zero Rota--Baxter operators."""
from itertools import product
from math import prod
import random

def mul(a,b,q,n):
    return tuple(sum(a[i*n+k]*b[k*n+j] for k in range(n))%q
                 for i in range(n) for j in range(n))

def scaled(a,t,q):
    return tuple(t*x%q for x in a)

def classified(a,c,q,n):
    if not any(a) or not any(c): return False
    a2=mul(a,a,q,n)
    for lam in range(q):
        if a2!=scaled(a,lam,q):continue
        ca=mul(c,a,q,n)
        ac=mul(a,c,q,n)
        for u in range(q):
            if ca==scaled(c,u,q) and ac==scaled(c,(lam-u)%q,q):
                return True
    return False

def direct(a,c,q,n):
    # Check the RB identity on all pairs of matrix units.
    es=[]
    for i in range(n*n):
        e=[0]*(n*n);e[i]=1;es.append(tuple(e))
    def f(x):
        return sum(c[j*n+i]*x[i*n+j] for i in range(n) for j in range(n))%q
    vals=[f(e) for e in es]
    left=[f(mul(a,e,q,n)) for e in es]
    right=[f(mul(e,a,q,n)) for e in es]
    sq=mul(a,a,q,n)
    for i in range(n*n):
        for j in range(n*n):
            lhs=scaled(sq,vals[i]*vals[j],q)
            rhs=scaled(a,vals[i]*left[j]+vals[j]*right[i],q)
            if lhs!=rhs:return False
    return True

def gaussian(n,r,q):
    if r<0 or r>n:return 0
    a,b=1,1
    for i in range(r):
        a*=q**(n-i)-1
        b*=q**(r-i)-1
    assert a%b==0
    return a//b

def gl(r,q):
    return prod(q**r-q**i for i in range(r))

def formula(n,q):
    nil={}
    sem={}
    for r in range(1,n//2+1):
        sq=gaussian(n,r,q)*gaussian(n-r,r,q)*gl(r,q)
        assert sq%(q-1)==0
        nil[r]=sq//(q-1)*(q**((n-r)**2)-1)
    for r in range(1,n):
        projections=gaussian(n,r,q)*q**(r*(n-r))
        sem[r]=2*projections*(q**(r*(n-r))-1)
    return 1+sum(nil.values())+sum(sem.values()),nil,sem

def enumerate_pairs(n,q,check_all_direct=False):
    vectors=list(product(range(q),repeat=n*n))
    found=0
    rng=random.Random(2026+n+q)
    negative=[]
    for a in vectors[1:]:
        for c in vectors[1:]:
            hit=classified(a,c,q,n)
            if hit:found+=1
            if check_all_direct or (hit and n==3) or (not hit and rng.randrange(300)==0):
                assert direct(a,c,q,n)==hit,(n,q,a,c)
    assert found%(q-1)==0
    return 1+found//(q-1)

def main():
    for n,q,all_direct in [(2,2,True),(2,3,True),(3,2,False)]:
        actual=enumerate_pairs(n,q,all_direct)
        predicted,nil,sem=formula(n,q)
        assert actual==predicted,(n,q,actual,predicted)
        print("CASE",n,q,actual,"nil",nil,"projection",sem)
    for n in range(1,8):
        for q in (2,3,4,5,7):
            total,nil,sem=formula(n,q)
            assert total>0
    assert formula(2,2)[0]==16
    assert formula(2,3)[0]==57
    assert formula(3,2)[0]==652
    assert formula(3,3)[0]==7905
    print("VERIFY_OK_RB_RANK_ONE")
if __name__=="__main__":
    main()
