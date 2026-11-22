"""Independent matrix-Lyapunov and Gaussian-moment checks for a bath-swapped OU pair.

Requires Python 3, numpy, scipy. Run: python checker.py
"""
import math
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.linalg import expm, solve_continuous_lyapunov, solve_discrete_lyapunov
from scipy.optimize import brentq


def analytic(a, coupling, mean_temperature, contrast, halfperiod):
    z = a * halfperiod
    f = 1 - math.tanh(z) / z
    root = a*a - coupling*coupling
    v = a*mean_temperature/root
    c = -coupling*mean_temperature/root
    mixed_sq = 2*c*c - (contrast/a)**2*f
    fourth_cumulant = 3*(contrast/a)**2*f
    joint_cumulant = -(contrast/a)**2*f
    return v, c, mixed_sq, fourth_cumulant, joint_cumulant


def independently_integrated(a, coupling, mean_temperature, contrast, halfperiod):
    """Reconstruct periodic covariance from matrix propagation, not scalar formulas."""
    K=np.array([[a,coupling],[coupling,a]],dtype=float)
    Qp=np.diag([mean_temperature+contrast,mean_temperature-contrast])*2
    Qm=np.diag([mean_temperature-contrast,mean_temperature+contrast])*2
    Sp=solve_continuous_lyapunov(K,Qp)
    Sm=solve_continuous_lyapunov(K,Qm)
    E=expm(-K*halfperiod)
    EE=E@E
    Q=Sm+E@(Sp-Sm)@E-EE@Sp@EE
    Sstart=solve_discrete_lyapunov(EE,Q)
    nodes,weights=leggauss(96)
    covariances=[]
    for block in (0,1):
        Sinit=Sstart if block==0 else Sp+E@(Sstart-Sp)@E
        Seq=Sp if block==0 else Sm
        for x,w in zip(nodes,weights):
            t=halfperiod*(x+1)/2
            Ft=expm(-K*t)
            S=Seq+Ft@(Sinit-Seq)@Ft
            covariances.append((float(w/4),S))
    Smix=sum(w*S for w,S in covariances)
    vx=float(Smix[0,0]);vy=float(Smix[1,1]);c=float(Smix[0,1])
    ex4=sum(w*3*S[0,0]**2 for w,S in covariances)
    ex2y2=sum(w*(S[0,0]*S[1,1]+2*S[0,1]**2) for w,S in covariances)
    ex4cum=ex4-3*vx*vx
    sqcov=ex2y2-vx*vy
    jointcum=sqcov-2*c*c
    lag=0.73
    lagcov=expm(-K*lag)@Smix
    expected_lag=expm(-K*lag)@(mean_temperature*np.linalg.inv(K))
    return vx,vy,c,sqcov,ex4cum,jointcum,np.max(np.abs(lagcov-expected_lag)),np.max(np.abs(Smix-mean_temperature*np.linalg.inv(K)))


def close(a,b,atol=1e-8):
    assert abs(a-b) < atol, (a,b)


def main():
    checks=0
    cases=[(2.,.5,1.,.9,.1),(2.,.5,1.,.9,.5),(2.,.5,1.,.9,1.),
           (2.,0.,1.,.9,.7),(2.,.2,1.,.7,9.),(3.,-1.,4.,2.,.4)]
    for a in (1.,2.,3.):
        for ratio in (0.,.1,.4,-.7):
            for frac in (.2,.8):
                for half in (.12,.47,1.9):
                    cases.append((a,ratio*a,1.5,frac*1.5,half))
    for params in cases:
        a,k,T,d,tau=params
        v,c,sq,fourth,joint=analytic(*params)
        nv,ny,nc,nsq,nfourth,njoint,el,ev=independently_integrated(*params)
        for x,y in [(v,nv),(v,ny),(c,nc),(sq,nsq),(fourth,nfourth),(joint,njoint)]:
            close(x,y,4e-8)
            checks+=1
        assert el < 1e-8 and ev < 1e-8
        checks+=2
    # Exact qualitative phase classification, with a well-resolved example.
    a,k,T,d=2.,.5,1.,.9
    h=2*k*k*a*a*T*T/((a*a-k*k)**2*d*d)
    root=brentq(lambda z:1-math.tanh(z)/z-h,.1,4.)/a
    close(root,.40829304915902426,1e-12);checks+=1
    for t in (.08,.1,.3,.4):assert analytic(a,k,T,d,t)[2]>0;checks+=1
    for t in (.42,.5,1,9):assert analytic(a,k,T,d,t)[2]<0;checks+=1
    cutoff=math.sqrt(2-math.sqrt(3))
    close(2*cutoff**2/(1-cutoff**2)**2,1,1e-12);checks+=1
    for z in (1e-5,.02,.5,2.,100.):
        der=(math.tanh(z)-z/(math.cosh(z)**2))/z**2 if z<100 else math.tanh(z)/z**2
        assert der>0;checks+=1
    print(f'{checks} independent deterministic assertions passed')

if __name__=='__main__':
    main()
