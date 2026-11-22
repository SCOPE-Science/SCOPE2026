#!/usr/bin/env python3
"""Reproducibility checks for weighted ell-one epigraph projection stability.
Only the Python standard library is required. Finite checks supplement, not replace, proof.
"""
from fractions import Fraction as F
from itertools import product
from random import Random


def face_formula(w, active):
    I=tuple(active)
    S=sum((w[i]*w[i] for i in I),F(0))
    W=sum((w[i] for i in I),F(0))
    d=1+S
    time=(S+W)/d
    space={i:1+w[i]*(1+W-2*w[i])/d for i in I}
    return time,space


def face_matrix_norm(w, active):
    n=len(w);I=set(active)
    v=[w[i] if i in I else F(0) for i in range(n)]+[F(-1)]
    d=1+sum(w[i]*w[i] for i in I)
    norms=[]
    for i in range(n+1):
        if i<n and i not in I:
            norms.append(F(0));continue
        norms.append(sum((abs((F(1) if i==j else F(0))-v[i]*v[j]/d) for j in range(n+1)),F(0)))
    return max(norms)


def exhaustive(w):
    ans=F(1);n=len(w)
    for mask in range(1,1<<n):
        I=[i for i in range(n) if mask>>i&1]
        t,s=face_formula(w,I)
        ans=max(ans,t,*s.values())
    return ans


def prefix_reduction(w):
    n=len(w);order=sorted(range(n),key=lambda i:w[i]); ans=F(1)
    for k in range(1,n+1):
        t,_=face_formula(w,order[:k]);ans=max(ans,t)
    for i in range(n):
        for k in range(n+1):
            I=set(order[:k]);I.add(i)
            _,space=face_formula(w,I)
            ans=max(ans,space[i])
    return ans


def project(y,t,w):
    if sum(w[i]*abs(y[i]) for i in range(len(w)))<=t:
        return list(y),t
    lo=0.; hi=1.
    def g(lam):
        return sum(float(w[i])*max(abs(float(y[i]))-lam*float(w[i]),0.) for i in range(len(w)))-float(t)-lam
    while g(hi)>0:hi*=2
    for _ in range(90):
        mid=(lo+hi)/2
        if g(mid)>0:lo=mid
        else:hi=mid
    lam=(lo+hi)/2
    out=[(1 if q>0 else -1 if q<0 else 0)*max(abs(float(q))-lam*float(v),0) for q,v in zip(y,w)]
    return out,float(t)+lam


def run():
    rng=Random(74231); checks=0
    for n in range(1,8):
        for trial in range(48):
            w=[F(rng.randint(1,40),rng.randint(1,24)) for _ in range(n)]
            a=exhaustive(w);b=prefix_reduction(w)
            assert a==b,(n,w,a,b)
            checks+=1
            for mask in range(1,1<<n):
                I=[i for i in range(n) if (mask>>i)&1]
                t,s=face_formula(w,I)
                mat=face_matrix_norm(w,I)
                assert mat==max(t,*s.values()),(n,w,I,mat,t,s)
                checks+=1
    # Exact two-coordinate, product-one branch formula over rational r>=1.
    for p in range(1,141):
        r=F(100+p,100)
        w=[r,F(1)/r]
        A=r/(r*r+r+1)
        B=(r*r+r-1)/((r*r-r+1)*(r*r+r+1))
        assert exhaustive(w)==1+max(A,B)
        checks+=1
    for n in range(2,8):
        for R in (10,100,1000):
            w=[F(R)**(2*(i+1)-n-1) for i in range(n)]
            p=F(1)
            for a in w:p*=a
            assert p==1
            L=prefix_reduction(w)
            assert F(1)<L<F(1)+F(3,R)
            checks+=2
    for n in range(1,8):
        for trial in range(30):
            w=[F(rng.randint(1,12),rng.randint(1,9)) for i in range(n)]
            I=[i for i in range(n) if rng.choice((True,False))]
            if not I:I=[rng.randrange(n)]
            # Input chosen strictly inside one linearity cell; verify all active signs.
            y=[(F(5)+w[i] if i in I else F(0)) for i in range(n)]
            t=sum(5*w[i] for i in I)-1
            out,tout=project(y,t,w)
            assert max(abs(out[i]-(5 if i in I else 0)) for i in range(n))<1e-8
            assert abs(tout-float(sum(5*w[i] for i in I)))<1e-8
            checks+=2
            # Coordinate perturbation bound against the exact finite support maximum.
            L=float(prefix_reduction(w))
            for j in range(n+1):
                h=1e-5; yp=list(map(float,y)); ym=list(map(float,y))
                tp=float(t);tm=float(t)
                if j<n:yp[j]+=h;ym[j]-=h
                else:tp+=h;tm-=h
                q1,s1=project(yp,tp,w);q0,s0=project(ym,tm,w)
                assert max([abs(a-b)/(2*h) for a,b in zip(q1+[s1],q0+[s0])])<=L+1e-6
                checks+=1
    print('PASS',checks,'supplementary assertions')

if __name__=='__main__':run()
