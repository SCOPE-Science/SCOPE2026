#!/usr/bin/env python3
"""Exact finite-field checks for ternary perfect evolution algebra symmetries."""
from collections import Counter
from fractions import Fraction
from itertools import product, permutations
from math import factorial

def polydiv(a,b,q=3):
    r=list(a); d=len(b)-1
    while len(r)>=len(b):
        c=r[-1]*pow(b[-1],-1,q)%q
        i=len(r)-len(b)
        for j,v in enumerate(b): r[i+j]=(r[i+j]-c*v)%q
        while r and r[-1]==0: r.pop()
    return tuple(r)

def factor_xl_minus_one(l):
    r=tuple([2]+[0]*(l-1)+[1]); fac=Counter()
    while len(r)>1:
        found=False
        for deg in range(1,len(r)):
            for cs in product(range(3),repeat=deg):
                if cs[0]==0:continue
                f=cs+(1,)
                if polydiv(r,f)==():
                    fac[f]+=1
                    # exact quotient
                    a=list(r); out=[0]*(len(a)-deg)
                    while len(a)>=len(f):
                        i=len(a)-len(f); c=a[-1]
                        out[i]=c
                        for j,v in enumerate(f):a[i+j]=(a[i+j]-c*v)%3
                        while a and a[-1]==0:a.pop()
                    r=tuple(out)
                    while len(r)>0 and r[-1]==0:r=r[:-1]
                    found=True
                    break
            if found:break
        assert found,(l,r)
    return fac

def centralizer_size(lamb):
    elementary={}
    for l in lamb:
        for f,e in factor_xl_minus_one(l).items():
            elementary.setdefault(f,[]).append(e)
    result=Fraction(1)
    for f,mu in elementary.items():
        d=len(f)-1; h=max(mu)
        exponent=d*sum(sum(a>=j for a in mu)**2 for j in range(1,h+1))
        result*=3**exponent
        for multiplicity in Counter(mu).values():
            for j in range(1,multiplicity+1):
                result*=Fraction(3**(d*j)-1,3**(d*j))
    assert result.denominator==1,(lamb,result)
    return int(result)

def partitions(n,low=1):
    if n==0:yield ()
    for i in range(low,n+1):
        for part in partitions(n-i,i):yield(i,)+part

def class_z(lamb):
    z=1
    for j,m in Counter(lamb).items():z*=j**m*factorial(m)
    return z

def iso_count(n):
    total=Fraction(0); table=[]
    for lamb in partitions(n):
        c=centralizer_size(lamb)
        z=class_z(lamb)
        total+=Fraction(c,2**len(lamb)*z)
        table.append((lamb,c,z))
    assert total.denominator==1
    return int(total),table

def matmul(a,b,n):
    return tuple(sum(a[n*i+k]*b[n*k+j] for k in range(n))%3 for i in range(n) for j in range(n))

def invmat(a,n):
    L=[[a[n*i+j] for j in range(n)]+[int(i==j) for j in range(n)] for i in range(n)]
    for j in range(n):
        p=next((i for i in range(j,n) if L[i][j]),None)
        if p is None:return None
        L[j],L[p]=L[p],L[j]; c=pow(L[j][j],-1,3)
        L[j]=[(c*x)%3 for x in L[j]]
        for i in range(n):
            if i!=j:
                c=L[i][j];L[i]=[(x-c*y)%3 for x,y in zip(L[i],L[j])]
    return tuple(L[i][n+j] for i in range(n) for j in range(n))

def perm_mat(p):
    n=len(p)
    return tuple(int(i==p[j]) for i in range(n) for j in range(n))

def permute_conj(a,p,n,sign=None):
    if sign is None: sign=(1,)*n
    return tuple(sign[i]*a[n*p[i]+p[j]]%3 for i in range(n) for j in range(n))

def check_small(n):
    perms=list(permutations(range(n)))
    signs=list(product((1,2),repeat=n))
    P=[(p,perm_mat(p)) for p in perms]
    unseen=set()
    total=0
    for a in product(range(3),repeat=n*n):
        inv=invmat(a,n)
        if inv is None:continue
        total+=1
        # Every automorphism is a signed permutation, and one diagonal change untwists all.
        automorphisms=[]
        for p,pm in P:
            u=matmul(matmul(a,pm,n),inv,n)
            if all(sum(bool(u[n*i+j]) for j in range(n))==1 for i in range(n)) and all(sum(bool(u[n*i+j]) for i in range(n))==1 for j in range(n)):
                if all(u[n*p[j]+j]!=0 for j in range(n)):
                    automorphisms.append((p,tuple(u[n*p[j]+j] for j in range(n))))
        assert any(all(sign[p[j]]*sign[j]%3==s[j] for p,s in automorphisms for j in range(n)) for sign in signs),(n,a,automorphisms)
        unseen.add(a)
    while unseen:
        a=next(iter(unseen))
        orb={permute_conj(a,p,n,sign) for p in perms for sign in signs}
        unseen.difference_update(orb)
        if 'orbit_count' not in locals():orbit_count=0
        orbit_count+=1
    return total,orbit_count

if __name__=='__main__':
    wanted={1:1,2:7,3:249,4:63985,5:124108129}
    for n in range(1,6):
        v,tab=iso_count(n)
        assert v==wanted[n],(n,v)
        print('Burnside',n,v)
        if n==5:
            for lam,c,z in tab:print('type',lam,'centralizer',c,'z',z)
    for n in (1,2,3):
        labeled,orbits=check_small(n)
        assert orbits==wanted[n],(n,orbits)
        print('Exhaustive',n,'labeled GL',labeled,'orbits',orbits,'simultaneous untwist PASS')
    print('TERNARY_EVOLUTION_CHECKS_PASSED')
