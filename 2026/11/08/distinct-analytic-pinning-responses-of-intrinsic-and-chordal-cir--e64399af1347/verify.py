#!/usr/bin/env python3
"""Standalone numerical checks of two circular Lloyd-map conventions.
Only standard-library numerical quadrature is used; the analytic result is proved separately.
"""
import math

TAU = 2.0 * math.pi

def simpson(fun, a, b, intervals=320):
    assert intervals % 2 == 0
    h = (b-a) / intervals
    total = fun(a)+fun(b)
    for k in range(1, intervals):
        total += (4 if k%2 else 2)*fun(a+k*h)
    return total*h/3

def centroid(center, halfwidth, concentration, convention):
    weight = lambda u: math.exp(concentration*math.cos(center+u))
    if convention == 'intrinsic':
        den = simpson(weight, -halfwidth, halfwidth)
        num = simpson(lambda u: u*weight(u), -halfwidth, halfwidth)
        return center+num/den
    assert convention == 'chordal'
    re = simpson(lambda u: math.cos(u)*weight(u), -halfwidth, halfwidth)
    im = simpson(lambda u: math.sin(u)*weight(u), -halfwidth, halfwidth)
    return center+math.atan2(im,re)

def update(q, concentration, convention):
    n=len(q)
    out=[]
    for j in range(n):
        left=(q[j-1]-(TAU if j==0 else 0)+q[j])/2
        right=(q[j]+q[(j+1)%n]+(TAU if j==n-1 else 0))/2
        mid=(left+right)/2
        half=(right-left)/2
        assert 0<half<math.pi/2
        out.append(centroid(mid,half,concentration,convention))
    return out

def coeff(n, convention):
    L=math.pi/n
    s,c=math.sin(L),math.cos(L)
    if convention=='intrinsic':return (s/L-c)/(s*s)
    return (L-s*c)/(2*s**3)

def check():
    drift=0
    for n in (3,4,5,7,10):
        uniform=[TAU*j/n for j in range(n)]
        for convention in ('intrinsic','chordal'):
            for kappa in (0.02,0.5,2.0):
                q1=update(uniform,kappa,convention)
                for j,q in enumerate(uniform):
                    if abs(math.sin(q))>1e-8:
                        assert (q1[j]-q)*math.sin(q)<-1e-11,(n,j,convention,kappa,q1[j]-q)
                        drift+=1
            for kappa in (0.006,0.003):
                q=uniform[:]
                for iteration in range(450):
                    qnext=update(q,kappa,convention)
                    if max(abs(a-b) for a,b in zip(qnext,q))<2e-15:
                        q=qnext
                        break
                    q=qnext
                residual=max(abs(a-b) for a,b in zip(q,update(q,kappa,convention)))
                assert residual<1e-10,(n,convention,kappa,residual)
                C=coeff(n,convention)
                errs=[abs((q[j]-uniform[j])/kappa+C*math.sin(uniform[j])) for j in range(n)]
                assert max(errs)<3*kappa,(n,convention,kappa,max(errs))
                # Reflection symmetry selects the pinned local branch.
                assert abs(q[0])<1e-9
                for j in range(1,n):
                    assert abs((q[j]-uniform[j])+(q[n-j]-uniform[n-j]))<1e-9
    for n in range(3,100):
        assert coeff(n,'chordal')>coeff(n,'intrinsic')>0
    print('VERIFY_OK drift_sign_checks=%d analytic_branch_cases=%d strict_coefficient_cases=%d'%(drift,5*2*2,97))

if __name__=='__main__':check()
