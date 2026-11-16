"""Independent quadrature check of the quadratic eigenvalue splitting.
Tests pure degree-three harmonics on S^3 at 60 and 90 degree resonances.
The all-degree assertion follows from the analytic angular factorization.
"""
import math
import numpy as np
from scipy.linalg import null_space
from numpy.polynomial.legendre import leggauss


def multi(d,n):
    if d==1: return [(n,)]
    return [(k,)+b for k in range(n+1) for b in multi(d-1,n-k)]


def lap(d,n,exp):
    low={b:i for i,b in enumerate(multi(d,n-2))}
    M=np.zeros((len(low),len(exp)))
    for j,a in enumerate(exp):
        for i,p in enumerate(a):
            if p>=2:
                b=list(a); b[i]-=2
                M[low[tuple(b)],j]+=p*(p-1)
    return M


def moment(a):
    if any(k%2 for k in a):return 0.
    out=1.
    for k in a:
        for j in range(k//2):out*=j+.5
    for j in range(sum(a)//2):out/=j+len(a)/2
    return out


def gram_theta(exp,basis,theta):
    t,wt=leggauss(12)
    ang=np.arange(24)*2*math.pi/24
    pts=[]; weights=[]
    for z,w in zip(t,wt):
        r=math.sqrt(max(0,1-z*z))
        for a in ang:
            v=[math.cos(theta)*r*math.cos(a),math.sin(theta)*r*math.cos(a),r*math.sin(a),z]
            pts.append(v); weights.append(w/(2*len(ang)))
    P=np.asarray(pts)
    F=np.column_stack([np.prod(P**np.asarray(e),axis=1) for e in exp])@basis
    W=np.sqrt(np.asarray(weights))
    return (F*W[:,None]).T@(F*W[:,None])


def main():
    d=4;ell=3
    e=multi(d,ell)
    B=null_space(lap(d,ell,e),rcond=1e-12)
    G=np.array([[moment(tuple(i+j for i,j in zip(a,b))) for b in e] for a in e])
    C=B.T@G@B
    lam,U=np.linalg.eigh(C)
    assert min(lam)>0
    W=B@U@np.diag(lam**-.5)
    for q,mult in [(2,2),(3,1)]:
        anchor=math.pi/q
        ratios=[]
        for delta in [.02,.01,.005]:
            A=.5*(gram_theta(e,W,0.)+gram_theta(e,W,anchor+delta))
            eig=np.linalg.eigvalsh(A)
            small=eig[:mult]
            assert min(small)>0
            ratios.append([float(x/delta**2) for x in small])
        for first,last in zip(ratios[0],ratios[-1]):
            assert .6<last/first<1.5,(q,ratios)
        E=.5*(gram_theta(e,W,0.)+gram_theta(e,W,anchor))
        eig=np.linalg.eigvalsh(E)
        assert max(abs(eig[:mult]))<1e-11,(q,eig)
        assert eig[mult]>1e-3,(q,eig)
        print('PASS: q=',q,'kernel=',mult,'delta^-2 eigenvalues=',ratios)

if __name__=='__main__':main()
