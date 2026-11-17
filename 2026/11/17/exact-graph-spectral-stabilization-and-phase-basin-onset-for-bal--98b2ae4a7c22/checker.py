"""Independent algebraic/numerical sanity checks for the stated oscillator-network theorem.
This checker is supplementary: the analytic derivation is the proof.
"""
from math import acos, cos, pi, sin, sqrt
import numpy as np

rng = np.random.default_rng(26110956)

def model(theta,A,K1,K2,d):
    n=len(theta)
    pair=(K1/d)*np.sum(A*np.sin(theta[None,:]-theta[:,None]),axis=1)
    z1=np.mean(np.exp(1j*theta))
    z2=np.mean(np.exp(2j*theta))
    tri=K2*np.imag(z2*np.conjugate(z1)*np.exp(-1j*theta))
    return pair+tri

def finite_J(theta,A,K1,K2,d,eps=1e-6):
    I=np.eye(len(theta))
    return np.column_stack([(model(theta+eps*x,A,K1,K2,d)-model(theta-eps*x,A,K1,K2,d))/(2*eps) for x in I])

def special_basis(s):
    n=len(s)
    e=s/np.sqrt(n)
    one=np.ones(n)/np.sqrt(n)
    # orthonormal complement of span(one,e) via SVD
    _,_,vh=np.linalg.svd(np.stack((one,e)),full_matrices=True)
    Q=vh[2:,:].T
    assert np.max(np.abs(np.stack((one,e))@Q)) < 1e-12
    return e,Q

def jac_analytic(s,A,K1,K2,d):
    B=(A*np.outer(s,s)).copy()
    np.fill_diagonal(B,-B.sum(axis=1))
    # A has a zero diagonal; B off diagonal is cos(phase diff)*A
    return K1/d*B-K2/len(s)*np.outer(s,s),B

checks=0
for n in (4,6,8):
    m=n//2
    s=np.r_[np.ones(m),-np.ones(m)]
    theta=np.r_[np.zeros(m),np.full(m,pi)]
    for case in range(12):
        # Connected weighted random network, with positive within/cross edges.
        A=rng.uniform(.05,3.0,(n,n)); A=(A+A.T)/2
        np.fill_diagonal(A,0)
        d=A.sum(axis=1).mean()
        K1=rng.uniform(.1,3.0)
        K2=rng.uniform(0,8)
        J,B=jac_analytic(s,A,K1,K2,d)
        Jfd=finite_J(theta,A,K1,K2,d)
        assert np.max(np.abs(J-Jfd))<2e-8
        assert np.max(np.abs(J-J.T))<1e-12
        e,Q=special_basis(s)
        C=Q.T@B@Q
        off=Q.T@B@e
        if np.linalg.eigvalsh(C).max()<-1e-8:
            edge=(K1/d)*(e@B@e-off@np.linalg.solve(C,off))
            vals=np.linalg.eigvalsh(Q.T@J@Q)
            assert vals.max()<0
            full=np.linalg.eigvalsh(J)
            # Exactly one neutral eigenvalue due to phase rotation.
            full=full[np.argsort(np.abs(full))]
            assert abs(full[0])<2e-10
            if K2>edge+1e-7: assert full[1:].max()<0
            if K2<edge-1e-7: assert full[1:].max()>0
        checks+=1

for m in (2,3,4,7):
    n=2*m
    s=np.r_[np.ones(m),-np.ones(m)]
    theta=np.r_[np.zeros(m),np.full(m,pi)]
    for a,b in ((3.,1.),(1.,3.),(1.,1.),(2.,.4)):
        A=np.full((n,n),b)
        A[:m,:m]=a; A[m:,m:]=a
        np.fill_diagonal(A,0)
        d=(m-1)*a+m*b; K1=1.3
        critical=2*m*b*K1/d
        for K2 in (0.,critical*.9,critical,critical*1.1,critical*5):
            J,B=jac_analytic(s,A,K1,K2,d)
            vals=np.linalg.eigvalsh(J)
            expected=np.sort(np.r_[0.,critical-K2,np.full(n-2,m*K1*(b-a)/d)])
            assert np.max(np.abs(vals-expected))<2e-12
            for phi in (.1, .7,pi-.4,pi,pi+.5):
                v=np.r_[np.zeros(m),np.full(m,phi)]
                f=model(v,A,K1,K2,d)
                assert np.max(np.abs(f[:m]-f[0]))<3e-14
                assert np.max(np.abs(f[m:]-f[-1]))<3e-14
                assert abs((f[-1]-f[0])+sin(phi)*(critical+K2*cos(phi)))<3e-13
                checks+=1
        # Equilibrium separator and basin width in the reduced circle.
        K2=1.8*critical
        phistar=acos(-critical/K2)
        basin_fraction=(2*pi-2*phistar)/(2*pi)
        assert abs(basin_fraction-acos(critical/K2)/pi)<1e-14
        checks+=1

print('PASS:',checks,'independent finite-difference/spectral/reduction/basin consistency comparisons')
