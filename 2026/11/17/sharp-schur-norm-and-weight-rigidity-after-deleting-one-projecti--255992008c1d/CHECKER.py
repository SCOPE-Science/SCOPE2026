"""Reproducible numerical and rational cross-checks for affine-plane Schur norms.
The analytic spectral decomposition and global optimization are proved in RESULT.md.
"""
from fractions import Fraction
import math
import numpy as np
from scipy.optimize import minimize_scalar


def incidence(q):
    """Prime-field cases q prime; rows affine lines, columns affine+ideal points."""
    points=[(x,y) for x in range(q) for y in range(q)]
    lines=[(m,b) for m in range(q) for b in range(q)] + [('v',b) for b in range(q)]
    B=np.zeros((len(lines),len(points)+q+1),dtype=float)
    for i,line in enumerate(lines):
        m,b=line
        for j,(x,y) in enumerate(points):
            B[i,j]=int((x==b) if m=='v' else ((y-m*x-b)%q==0))
        B[i,q*q+(q if m=='v' else m)]=1
    return B


def values(q,t):
    a=(1-t)/q
    b=q*t/(q+1)
    c=b+(q+1)*(1-t)/q
    return a,b,c


def value(q,t):
    a,b,c=values(q,t)
    return (math.sqrt(c)+q*math.sqrt(b)+(q*q-1)*math.sqrt(a))/math.sqrt(q*(q+1))


def derivative_root(q,t):
    gamma=(q+1)/q-q/(q+1)
    a,b,c=values(q,t)
    return (-gamma/math.sqrt(c)+q*math.sqrt(q/(q+1)/t)-(q*q-1)/math.sqrt(q*(1-t)))


def test():
    cases=0
    for q in (2,3,5,7):
        B=incidence(q)
        assert B.shape == (q*(q+1),q*q+q+1)
        assert (B.sum(axis=1)==q+1).all()
        for t in (Fraction(1,8),Fraction(1,4),Fraction(2,5),Fraction(3,4)):
            p=float(t)
            col=np.array([(1-p)/q**2]*(q*q)+[p/(q+1)]*(q+1))
            W=B*np.sqrt(col)[None,:]/math.sqrt(q*(q+1))
            G=W@W.T
            spec=np.linalg.eigvalsh(G)[::-1]
            a,b,c=values(q,p)
            theoretical=sorted([c]+[b]*q+[a]*(q*q-1),reverse=True)
            assert np.max(abs(spec-np.array(theoretical)/(q*(q+1))))<2e-12,(q,p)
            norm=float(np.sum(np.linalg.svd(W,compute_uv=False)))
            assert abs(norm-value(q,p))<2e-11,(q,p,norm,value(q,p))
            cases+=1
        opt=minimize_scalar(lambda t:-value(q,t),bounds=(1e-10,1-1e-10),method='bounded',options={'xatol':1e-13})
        t=opt.x
        assert t>0 and t<(q+1)/(q*q+q+1)
        assert abs(derivative_root(q,t))<5e-5,(q,t)
        print('q',q,'t*',round(t,12),'Schur norm',round(value(q,t),12))
    for q in (31,101,503):
        opt=minimize_scalar(lambda t:-value(q,t),bounds=(1e-12,0.2),method='bounded',options={'xatol':2e-15})
        t=opt.x
        approx=1/q-2/q**2+6/q**3
        assert abs(t-approx)<20*q**(-3.5),(q,t,approx)
        pu=(q+1)/(q*q+q+1)
        assert value(q,t)>value(q,pu)
        ratio=(value(q,t)-value(q,pu))*q**2.5
        print('asymptotic q',q,'gain*q^(5/2)',round(ratio,9))
    print('PASS',cases,'weighted Gram checks, 7 optimizers, 3 asymptotic probes')

if __name__=='__main__':test()
