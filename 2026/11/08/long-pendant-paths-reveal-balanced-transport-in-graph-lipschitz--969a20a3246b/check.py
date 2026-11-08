"""Exact finite checks for Lipschitz spread of graphs with pendant paths.
Uses only Python standard library. Independent direct enumeration is deliberately
restricted to small graphs; the general results use mathematical proofs.
"""
from fractions import Fraction as Q
from itertools import product
from math import floor

def var(vals):
    n=len(vals)
    return Q(sum(Q(x)*Q(x) for x in vals),n)-Q(sum(vals),n)**2

def core_potentials(n,edges,diam):
    for tail in product(range(-diam,diam+1), repeat=n-1):
        c=(0,)+tail
        if all(abs(c[u]-c[v])<=1 for u,v in edges):
            yield c

def reduced(n,edges,diam,l):
    s=Q(l*(l+2),12)
    return s+max(var([Q(c[i])+Q(e[i]*l,2) for i in range(n)])
        for c in core_potentials(n,edges,diam) for e in product((-1,1),repeat=n))

def direct(n,edges,diam,l):
    # Independently enumerate all signed edge increments on pendant paths.
    N=n*(l+1)
    best=Q(-1)
    for c in core_potentials(n,edges,diam):
        for inc in product((-1,1),repeat=n*l):
            vals=[]
            for i in range(n):
                z=c[i]; vals.append(z)
                for j in range(l):
                    z += inc[i*l+j]
                    vals.append(z)
            best=max(best,var(vals))
    return best

def beta_gamma(n,edges,diam):
    bal=n%2
    best=None; g=Q(-1)
    for c in core_potentials(n,edges,diam):
        for e in product((-1,1),repeat=n):
            if abs(sum(e))!=bal: continue
            b=Q(sum(c[i]*e[i] for i in range(n)),n)-Q(sum(c)*sum(e),n*n)
            w=var(c)
            if best is None or b>best: best=b;g=w
            elif b==best and w>g:g=w
    return best,g

def poly(n,edges,diam,l):
    b,g=beta_gamma(n,edges,diam)
    a=Q(1,4)*(1-Q((n%2)**2,n*n))
    return Q(l*(l+2),12)+a*l*l+b*l+g

def graph(n,kind):
    if kind=='complete':
        return [(i,j) for i in range(n) for j in range(i+1,n)],1
    if kind=='path':return [(i,i+1) for i in range(n-1)],n-1
    if kind=='cycle':return [(i,(i+1)%n) for i in range(n)],n//2
    if kind=='star':return [(0,i) for i in range(1,n)],2
    raise ValueError(kind)

cases=[(2,'complete',3),(3,'complete',3),(3,'path',3),(4,'complete',2),(4,'path',2),(4,'cycle',2),(4,'star',2)]
for n,kind,lmax in cases:
    e,diam=graph(n,kind)
    for l in range(1,lmax+1):
        lhs=direct(n,e,diam,l); rhs=reduced(n,e,diam,l)
        assert lhs==rhs,(n,kind,l,lhs,rhs)
print('INDEPENDENT_FULL_SIGNED_INCREMENT_ENUMERATIONS_OK',sum(k for _,_,k in cases))
for n in range(2,7):
    ed,diam=graph(n,'complete')
    phi=Q((n*n)//4,n*n)
    for l in range(1,7):
        rhs=reduced(n,ed,diam,l)
        expected=Q(l*(l+2),12)+phi*(l+1)**2
        assert rhs==expected,(n,l,rhs,expected)
    beta,gamma=beta_gamma(n,ed,diam)
    assert beta==2*phi and gamma==phi,(n,beta,gamma)
print('ALL_CLIQUE_CORE_CLOSED_FORMS_OK 30')
for n in range(2,8):
    ed,diam=graph(n,'path')
    b,g=beta_gamma(n,ed,diam)
    assert b==Q(n*n//4,n),(n,b)
    assert poly(n,ed,diam,n*n*(diam+1)**2)==reduced(n,ed,diam,n*n*(diam+1)**2)
print('EXACT_BALANCED_TRANSPORT_SLOPES_FOR_PATHS_OK 6')
for n,kind in [(3,'complete'),(4,'complete'),(4,'cycle'),(4,'star'),(4,'path')]:
    ed,diam=graph(n,kind)
    cutoff=n*n*(diam+1)**2
    for l in (cutoff,cutoff+1,cutoff+47):
        assert reduced(n,ed,diam,l)==poly(n,ed,diam,l)
print('EXACT_EVENTUAL_QUADRATIC_IDENTITIES_OK 15')
print('ALL_PENDANT_CORONA_SPREAD_CHECKS_OK')
