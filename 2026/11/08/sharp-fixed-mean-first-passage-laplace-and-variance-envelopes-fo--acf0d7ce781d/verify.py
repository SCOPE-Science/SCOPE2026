#!/usr/bin/env python3
"""Standalone numerical diagnostics for a Brownian distributed-reset theorem.

Standard-library-only checks; the analytic proof is supplied separately.
"""
import math

N = 0

def ok(cond, msg="check"):
    global N
    assert cond, msg
    N += 1

def near(x, y, atol=1e-9, rtol=1e-9):
    ok(math.isclose(x, y, abs_tol=atol, rel_tol=rtol), f"{x} != {y}")

def transform(r, s, distances, weights, D=1.0):
    assert len(distances) == len(weights)
    i = sum(w * math.exp(-z * math.sqrt((r+s)/D)) for z, w in zip(distances,weights))
    f = (r+s)*i/(s+r*i)
    return f, i

def moments(r, distances, weights, D=1.0):
    lam=math.sqrt(r/D)
    u=[math.exp(-lam*z) for z in distances]
    p=sum(w*x for w,x in zip(weights,u))
    q=sum(w*x*math.log(x) for w,x in zip(weights,u))
    return (1-p)/(r*p),(1-p*p+q)/(r*r*p*p),p,q

E=math.e
A=[2.0]; B=[1.0,3.0]
wA=[1.0]; wB=[1.0/(E+1),E/(E+1)]
ma,va,pa,qa=moments(1,A,wA)
mb,vb,pb,qb=moments(1,B,wB)
near(ma,mb)
near(pa,pb)
near(ma,E**2-1)
near(va,E**4-2*E**2-1)
near(vb,E**4-E**2*(E+3)/(E+1)-1)
near(vb-va,E**2*(E-1)/(E+1))
ok(vb>va)
for s in (0.0003,0.02,0.2,1.,4.,15.):
    fa,ia=transform(1.,s,A,wA)
    fb,ib=transform(1.,s,B,wB)
    ok(fa<fb)
    for f,i in ((fa,ia),(fb,ib)):
        near(i,s*f/(s+1-f),rtol=1e-12)

# Fixed mean p between two endpoints; test all-frequency extremizers and an
# entire continuum of exact fixed-mean mixtures.
for r,D,a,b in ((1.,1.,1.,3.),(0.27,1.1,0.8,2.6),(3.1,0.43,0.3,1.4)):
    lam=math.sqrt(r/D)
    um=math.exp(-lam*b); up=math.exp(-lam*a)
    for t in (0.07,0.25,0.5,0.8,0.94):
        p=(1-t)*um+t*up
        zstar=-math.log(p)/lam
        lower_dist=[zstar]; lower_w=[1.]
        upper_dist=[a,b]; upper_w=[t,1-t]
        ml,vl,pl,ql=moments(r,lower_dist,lower_w,D)
        mu,vu,pu,qu=moments(r,upper_dist,upper_w,D)
        near(pl,pu,rtol=2e-13)
        near(ml,mu,rtol=2e-13)
        ok(vu>vl)
        near(vl,(1-p*p+p*math.log(p))/(r*r*p*p))
        for v in (0.,0.15,0.38,0.61,0.94,1.):
            # Exact convex family of fixed-p distance laws.
            dist=[zstar,a,b]
            wt=[1-v,v*t,v*(1-t)]
            mm,vv,pp,qq=moments(r,dist,wt,D)
            near(mm,ml,rtol=2e-13)
            ok(vl-1e-11<=vv<=vu+1e-11)
            for s in (0.003,0.3,1.,6.,15.):
                lf,_=transform(r,s,lower_dist,lower_w,D)
                mf,ii=transform(r,s,dist,wt,D)
                uf,_=transform(r,s,upper_dist,upper_w,D)
                ok(lf-1e-12<=mf<=uf+1e-12)
                near(ii,s*mf/(s+r-r*mf),rtol=2e-11)
                if v>0. and v<1.:
                    ok(lf<mf<uf)

# The s=0 derivative is separately approximated from the transform.
for dist,wt in ((A,wA),(B,wB)):
    mean,var,p,q=moments(1.,dist,wt)
    h=3e-5
    f0=1.
    f1=transform(1.,h,dist,wt)[0]
    f2=transform(1.,2*h,dist,wt)[0]
    f3=transform(1.,3*h,dist,wt)[0]
    # Three-point one-sided first derivative, checked to O(h^2).
    d1=(-3*f0+4*f1-f2)/(2*h)
    near(-d1,mean,atol=1e-6,rtol=1e-6)
    # Four-point one-sided second derivative, checked to O(h^2).
    d2=(2*f0-5*f1+4*f2-f3)/(h*h)
    near(d2-mean**2,var,atol=0.01,rtol=0.001)

print(f"PASS: {N} standard-library numerical assertions")
