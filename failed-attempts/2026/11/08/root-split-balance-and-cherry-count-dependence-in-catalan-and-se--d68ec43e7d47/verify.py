"""Exact checks of root-split/cherry covariances in two binary-tree laws.
Only Python standard library is required. Inferences for all n use the proof,
not finite testing.
"""
from fractions import Fraction as Q
from collections import Counter
from math import comb, sqrt, pi

def catalan(n): return comb(2*n,n)//(n+1)
def a(n): return comb(2*n-2,n-1) if n else 0
def cat_mean(n): return Q(a(n),catalan(n)) if n else Q(0)
def bst_mean(n): return Q(0) if n==0 else (Q(1) if n==1 else Q(n+1,3))
def b(k,n): return (2*k-(n-1))**2

def moment_from_root(n,counts,weights):
    c=Q(0); eb=Q(0); eh=Q(0); ebh=Q(0)
    for k in range(n):
        p=weights(n,k)
        ch=counts(k)+counts(n-1-k)
        bb=b(k,n)
        c+=p; eb+=p*bb; eh+=p*ch; ebh+=p*bb*ch
    assert c==1
    return eb,eh,ebh,ebh-eb*eh

catw=lambda n,k:Q(catalan(k)*catalan(n-1-k),catalan(n))
bstw=lambda n,k:Q(1,n)

checks=0
for n in range(2,201):
    eb,eh,ebh,cov=moment_from_root(n,cat_mean,catw)
    closed=-Q(n-2,2*n-1)*Q(4**(n-1),catalan(n))
    assert cov==closed; checks+=1
    assert eh==cat_mean(n); checks+=1
    # Two explicit coefficients of the marked root-split generating functions.
    bb=comb(2*n-2,n-1)
    B=sum((2*k-(n-1))**2*catalan(k)*catalan(n-1-k) for k in range(n))
    M=sum((2*k-(n-1))**2*(a(k)*catalan(n-1-k)+catalan(k)*a(n-1-k)) for k in range(n))
    assert B==Q(4*n+2,1)*bb-Q(2,n)*bb-4**n; checks+=1
    assert M==(n+1)**2*bb-(n+2)*4**(n-1); checks+=1
    _,g,_,bcov=moment_from_root(n,bst_mean,bstw)
    assert bcov==-Q(8*(n-2),3*n); checks+=1
    assert g==bst_mean(n); checks+=1

# Independently enumerate the cherry-count distribution via recursive split products.
C=[Counter({0:1})]
B=[Counter({0:Q(1)})]
for n in range(1,13):
    cc=Counter(); dd=Counter()
    for k in range(n):
        for i,x in C[k].items():
            for j,y in C[n-1-k].items():
                cc[i+j+(n==1)]+=x*y
        for i,x in B[k].items():
            for j,y in B[n-1-k].items():
                dd[i+j+(n==1)]+=Q(x*y,n)
    C.append(cc);B.append(dd)
    assert sum(cc.values())==catalan(n);checks+=1
    assert sum(dd.values())==1;checks+=1
    if n>=2:
        eb=eh=em=Q(0)
        for k in range(n):
            for i,x in C[k].items():
                for j,y in C[n-1-k].items():
                    p=Q(x*y,catalan(n)); bb=b(k,n); hh=i+j
                    eb+=p*bb;eh+=p*hh;em+=p*bb*hh
        assert em-eb*eh==-Q(n-2,2*n-1)*Q(4**(n-1),catalan(n));checks+=1
        eb=eh=em=Q(0)
        for k in range(n):
            for i,x in B[k].items():
                for j,y in B[n-1-k].items():
                    p=Q(x*y,n); bb=b(k,n); hh=i+j
                    eb+=p*bb;eh+=p*hh;em+=p*bb*hh
        assert em-eb*eh==-Q(8*(n-2),3*n);checks+=1

for n in range(5,101):
    fs=[cat_mean(k)+cat_mean(n-1-k) for k in range(n)]
    assert fs[0]==fs[-1]==min(fs);checks+=1
    assert fs[1]==fs[-2]==max(fs);checks+=1
    assert all(fs[k]>fs[k+1] for k in range(1,(n-2)//2));checks+=1
    gs=[bst_mean(k)+bst_mean(n-1-k) for k in range(n)]
    assert gs[0]==gs[-1]==Q(n,3);checks+=1
    assert gs[1]==gs[-2]==Q(n+2,3);checks+=1
    assert all(gs[k]==Q(n+1,3) for k in range(2,n-2));checks+=1

for n in [200,500,1000,2000]:
    c=-Q(n-2,2*n-1)*Q(4**(n-1),catalan(n))
    relative=(float(-c/(n**1.5)))/(sqrt(pi)/8)
    assert abs(relative-1)<0.025;checks+=1

print(f'PASS: {checks} exact and numerical assertions')
