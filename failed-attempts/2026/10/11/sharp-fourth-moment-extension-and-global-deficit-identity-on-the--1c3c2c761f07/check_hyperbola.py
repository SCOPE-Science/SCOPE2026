"""Reproduce the fourth-moment identity for reciprocal finite-field curves.

Run: python3 check_hyperbola.py
No third-party dependencies. Arithmetic is exact up to the final Fourier checks.
"""
import cmath
import itertools
import math
import random


def field(p, quadratic=False):
    if not quadratic:
        elems=list(range(p))
        add=lambda a,b:(a+b)%p
        neg=lambda a:(-a)%p
        mul=lambda a,b:(a*b)%p
        char=lambda a:cmath.exp(2j*math.pi*a/p)
    else:
        assert p==3
        elems=[(a,b) for a in range(p) for b in range(p)]
        add=lambda x,y:((x[0]+y[0])%p,(x[1]+y[1])%p)
        neg=lambda x:((-x[0])%p,(-x[1])%p)
        mul=lambda x,y:((x[0]*y[0]-x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
        char=lambda x:cmath.exp(2j*math.pi*((2*x[0])%p)/p)
    zero=elems[0]
    one=(1,0) if quadratic else 1
    nz=[a for a in elems if a!=zero]
    inv={a:next(b for b in nz if mul(a,b)==one) for a in nz}
    return elems,add,neg,mul,char,zero,nz,inv


def pair_data(F):
    elems,add,neg,mul,char,zero,nz,inv=F
    fibers={}
    for a,b in itertools.product(nz,repeat=2):
        t=(add(a,b),add(inv[a],inv[b]))
        fibers.setdefault(t,[]).append((a,b))
    ap={tuple(sorted((a,neg(a)))) for a in nz}
    assert len(ap)==len(nz)//2
    for t,pairs in fibers.items():
        if t==(zero,zero):
            assert len(pairs)==len(nz)
        else:
            assert len(pairs) in (1,2)
            x,y=t
            assert x!=zero and y!=zero
            if len(pairs)==2:
                assert pairs[0]==pairs[1][::-1]
    return fibers


def collision_fourth(F,values):
    fibers=pair_data(F)
    return sum(abs(sum(values[a]*values[b] for a,b in v))**2 for v in fibers.values())


def closed_fourth(F,values):
    elems,add,neg,mul,char,zero,nz,inv=F
    H=sum(abs(values[a])**2 for a in nz)
    V=sum(abs(values[a])**4 for a in nz)
    A=sum(abs(values[a]*values[neg(a)])**2 for a in nz)/2
    T=sum(values[a]*values[neg(a)] for a in nz)/2
    return 2*H**2 - V - 4*A+4*abs(T)**2


def stability_terms(F, values):
    elems,add,neg,mul,char,zero,nz,inv=F
    pairs=[]
    seen=set()
    for a in nz:
        if a in seen:continue
        b=neg(a)
        seen.update((a,b))
        pairs.append((a,b))
    k=len(pairs)
    H=sum(abs(values[a])**2 for a in nz)
    records=[]
    for a,b in pairs:
        x=abs(values[a])**2
        y=abs(values[b])**2
        t=abs(values[a]*values[b])
        u=(x+y)/2
        records.append((x+y,u,t,values[a]*values[b],x-y))
    dispersion=1.5*sum((rec[0]-H/k)**2 for rec in records)
    imbalance=.5*sum(rec[4]**2 for rec in records)
    cross=8*sum(records[i][1]*records[j][1]-records[i][2]*records[j][2]
                for i in range(k) for j in range(i+1,k))
    coherence=4*(sum(rec[2] for rec in records)**2-abs(sum((rec[3] for rec in records),0j))**2)
    return dispersion,imbalance,cross,coherence


def direct_fourier(F,values):
    elems,add,neg,mul,char,zero,nz,inv=F
    m=len(nz)
    return sum(abs(sum(values[a]*char(add(mul(x,a),mul(y,inv[a])))
                       for a in nz)/m)**4 for x,y in itertools.product(elems,repeat=2))


def run():
    rng=random.Random(6132024)
    total_random=0
    for p,quadratic in [(3,False),(5,False),(7,False),(11,False),
                        (13,False),(3,True)]:
        F=field(p,quadratic)
        elems,add,neg,mul,char,zero,nz,inv=F
        q=len(elems);m=q-1
        fibers=pair_data(F)
        all_one={a:1 for a in nz}
        C=3-3/m
        assert abs(collision_fourth(F,all_one)-C*m*m)<1e-8
        for _ in range(20):
            f={a:complex(rng.randint(-3,3),rng.randint(-3,3)) for a in nz}
            exact=collision_fourth(F,f)
            formula=closed_fourth(F,f)
            assert abs(exact-formula)<1e-7*max(1,exact)
            H=sum(abs(x)**2 for x in f.values())
            assert exact<=C*H*H+1e-7
            terms=stability_terms(F,f)
            assert min(terms)>=-1e-8*max(1,H*H)
            assert abs(sum(terms)-(C*H*H-exact))<1e-7*max(1,H*H)
            qfourier=direct_fourier(F,f)
            assert abs(qfourier-(q*q/m**4)*exact)<1e-7*max(1,qfourier)
            total_random+=1
        # Saturating family: one arbitrary phase on each antipodal pair,
        # the opposite coefficient has conjugate phase.
        f={}
        for a in nz:
            if a in f:continue
            z=cmath.exp(1j*rng.randint(0,14)/7)
            f[a]=z;f[neg(a)]=z.conjugate()
        H=sum(abs(x)**2 for x in f.values())
        assert abs(collision_fourth(F,f)-C*H*H)<1e-8*max(1,H*H)
        assert max(map(abs,stability_terms(F,f)))<1e-8*max(1,H*H)
        print('q=%2d, fibers=%3d, random tests=20, sharp constant^4=%.12f: PASS'
              %(q,len(fibers),(q*q/(m*m))*C))
    print('Checked %d random signals plus six nonconstant-phase extremizers.'%total_random)

if __name__=='__main__':run()
