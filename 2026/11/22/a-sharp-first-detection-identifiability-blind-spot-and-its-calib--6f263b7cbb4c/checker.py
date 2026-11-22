"""Independent arithmetic checks for a two-state wildlife detection model.

Uses ordinary scientific Python; no research history or external data is needed.
"""
import math
from fractions import Fraction
import numpy as np
from scipy.linalg import expm


def parameters(c,e,d,effort,initial_active):
    h=effort*d
    S=c+e+h
    P=c*h
    return S,P


def initial_laplace(c,e,d,s,q,u):
    S,P=parameters(c,e,d,s,q)
    return s*d*(c+q*u)/(u*u+S*u+P)


def matrix_laplace(c,e,d,s,q,u):
    h=s*d
    Q=np.array([[-c,c],[e,-e-h]],dtype=float)
    init=np.array([1-q,q])
    target=np.array([0,h])
    return init @ np.linalg.solve(u*np.eye(2)-Q,target)


def recover_zero_start(s1,s2,mean1,mean2,var1):
    U=(s2*mean2-s1*mean1)/(s2-s1)
    V=s1*s2*(mean1-mean2)/(s2-s1)
    K=2/(s1*(mean1*mean1-var1))
    c=1/U
    d=U*K
    e=V*K-c
    return c,e,d


def density_derivatives(c,e,d,s,q):
    h=s*d
    S=c+e+h
    P=c*h
    f0=h*q
    X=c-q*S
    f1=h*X
    f2=h*(-S*X-P*q)
    return f0,f1,f2


def recover_jet(s,q,f0,f1,f2):
    h=f0/q
    X=f1/h
    Y=f2/h
    D=X+q*q*h
    S=-(Y+q*h*X)/D
    c=X+q*S
    e=S-c-h
    return c,e,h/s


def moments_zero_start(c,e,d,s):
    S,P=parameters(c,e,d,s,0)
    return S/P,(S*S-2*P)/(P*P)


def check():
    trials=0
    rng=np.random.default_rng(20261119)
    for j in range(2200):
        c,e,d=rng.uniform(0.08,5,3)
        s1,s2=sorted(rng.uniform(0.25,4,2))
        q=float(rng.uniform(0,1))
        mean1,var1=moments_zero_start(c,e,d,s1)
        mean2,_=moments_zero_start(c,e,d,s2)
        vals=recover_zero_start(s1,s2,mean1,mean2,var1)
        assert np.allclose(vals,[c,e,d],rtol=1e-9,atol=1e-9)
        for u in [0,0.1,0.5,1.7,10.0]:
            a=initial_laplace(c,e,d,s1,q,u)
            b=matrix_laplace(c,e,d,s1,q,u)
            assert math.isclose(a,b,rel_tol=1e-12,abs_tol=1e-12)
            trials+=1
        if 0<q<1:
            jet=density_derivatives(c,e,d,s1,q)
            h=s1*d
            denom=(jet[1]/h)+q*q*h
            if abs(denom)>1e-7:
                rec=recover_jet(s1,q,*jet)
                assert np.allclose(rec,[c,e,d],rtol=1e-7,atol=1e-7)
                trials+=1
        S,P=parameters(c,e,d,s1,q)
        disc=S*S-4*P
        assert disc>0
        lamminus=(S-math.sqrt(disc))/2
        qstar=lamminus/(s1*d)
        assert 0<qstar<1
        for u in [0,0.5,2.5,5.0]:
            a=initial_laplace(c,e,d,s1,qstar,u)
            b=lamminus/(lamminus+u)
            assert math.isclose(a,b,rel_tol=1e-10,abs_tol=1e-10)
            trials+=1
    # Exact nonidentifiability at one effort, but different means after a detector perturbation.
    p1=(Fraction(1),Fraction(3),Fraction(2))
    p2=(Fraction(1,2),Fraction(3,2),Fraction(4))
    for u in [Fraction(0),Fraction(1,7),Fraction(4),Fraction(11,3)]:
        assert initial_laplace(*p1,Fraction(1),Fraction(0),u)==initial_laplace(*p2,Fraction(1),Fraction(0),u)
        trials+=1
    assert moments_zero_start(*p1,Fraction(1))==(Fraction(3),Fraction(8))
    assert moments_zero_start(*p2,Fraction(1))==(Fraction(3),Fraction(8))
    assert moments_zero_start(*p1,Fraction(2))[0]==Fraction(2)
    assert moments_zero_start(*p2,Fraction(2))[0]==Fraction(5,2)
    assert recover_zero_start(Fraction(1),Fraction(2),Fraction(3),Fraction(2),Fraction(8))==p1
    # A quasi-stationary model at prescribed initial active proportion 1/2.
    q=Fraction(1,2)
    s=Fraction(1)
    rate=Fraction(2)
    # Keep the same exponential detection-time law while changing both switching rates.
    for c in [Fraction(3),Fraction(5),Fraction(10)]:
        h=rate/q
        e=(1-q)*(c-rate)/q
        d=h/s
        for u in [Fraction(0),Fraction(1),Fraction(3,2)]:
            assert initial_laplace(c,e,d,s,q,u)==rate/(u+rate)
            trials+=1
    for c,e,d in [(Fraction(3),Fraction(1),Fraction(4)),(Fraction(5),Fraction(3),Fraction(4))]:
        q=Fraction(1,2)
        f0,f1,f2=density_derivatives(c,e,d,Fraction(1),q)
        assert f0==2 and f1==-4 and f2==8
        assert f1/(d)+q*q*d==0
        trials+=1
    # Against direct matrix exponential for probability of remaining undetected.
    for c,e,d,s,q in [(1,3,2,1,0),(1,3,2,2,.5),(3,1,4,1,.5)]:
        Q=np.array([[-c,c],[e,-e-s*d]],dtype=float)
        p=np.array([1-q,q])
        for t in [0,0.3,1,3]:
            surv=p@expm(Q*t)@np.ones(2)
            assert 0<surv<=1+1e-14
            trials+=1
    print(f'PASS: {trials} Laplace, moment, cancellation, jet-inverse and matrix-survival checks')

if __name__=='__main__':check()
