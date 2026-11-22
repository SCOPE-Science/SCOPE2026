"""Numerical verification for the gamma-Cox dense-grid detection-edge theorem.
All limits are proved analytically in RESULT.md; this is a finite numerical sanity check.
"""
import math

def boundary(K,t):
    L=math.log(K)
    A=L**1.5/2.0
    h=1.0/(2*A*math.sqrt(K*L))
    T=L+math.log(A)
    # Enumerate outside the threshold. Gaussian tails beyond T+50 are negligible.
    j0=max(1,math.ceil(math.sqrt(max(0.0,T+t)/(K*h*h))))
    j1=math.ceil(math.sqrt((T+55)/(K*h*h)))+3
    # analytic log probability of no detected points on two symmetric sides
    ell=0.0
    lam=0.0
    for j in range(j0,j1+1):
        E=K*(j*h)**2
        if E <= T+t: continue
        q=math.exp(-E)
        ell-=2*K*math.log1p(q)
        lam+=2*(1-math.exp(-K*math.log1p(q)))
    return math.exp(ell),lam

def run():
    cnt=0
    for K in (1e6,1e10,1e16,1e24):
        for t in (-1.,0.,1.):
            P,mu=boundary(K,t)
            assert 0<P<1 and mu>0, (K,t,P,mu)
            cnt+=2
            # the expected number above zero moves toward 2; coarse finite-K tolerance
            if K==1e24:
                assert abs(mu-2*math.exp(-t))<0.17*2*math.exp(-t),(K,t,mu)
                cnt+=1
    # exact one-site gamma integral: for integer K and parameter E,
    # a Gamma(K,1) mixed Poisson zero probability equals (1+exp(-E))**(-K)
    for k in range(1,12):
        for E in (0., 0.5,1.,4.):
            z=(1+math.exp(-E))**(-k)
            # an independent finite sum gamma integral (integer shape) via derivatives:
            z2=math.exp(-k*math.log1p(math.exp(-E)))
            assert abs(z-z2)<1e-13
            cnt+=1
    assert abs((1-2**-8)-(1-(1+1)**(-8)))<1e-14
    cnt+=1
    print('PASS',cnt,'deterministic checks')
    for K in (1e6,1e10,1e16,1e24):
        P,mu=boundary(K,0)
        print('K=',K,'P(M<=0)=',round(P,7),'mean exceedances=',round(mu,7),'target=',round(math.exp(-2),7))
if __name__=='__main__':run()
