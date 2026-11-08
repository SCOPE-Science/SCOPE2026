"""Numerical corroboration for radial angular-chirp Fock localization.

Requires only Python 3 standard library. This is not a proof of compactness.
"""
import math
import cmath

def gamma_ratio(n,k):
    return math.exp(math.lgamma(n+k/2+1)-.5*(math.lgamma(n+1)+math.lgamma(n+k+1)))

def coefficient(n,k,gamma,beta,steps=12000):
    # Fixed Fourier k, matrix coefficient for e^{ik theta}.
    a,b=-5.0,5.0
    h=(b-a)/steps
    lg=math.lgamma(n+k/2+1)
    s=0j
    for j in range(steps+1):
        t=a+j*h
        r=math.sqrt(n)+t
        if r<=0:
            continue
        logdensity=math.log(2)+(2*n+k+1)*math.log(r)-r*r-lg
        val=math.exp(logdensity)*cmath.exp(-1j*beta*k*r**gamma)
        w=1 if j in (0,steps) else (4 if j%2 else 2)
        s+=w*val
    return gamma_ratio(n,k)*s*h/3

def run():
    beta=.7
    count=0
    for k in (1,2):
        for n in (64,256,1024):
            for gamma in (.5,1.):
                val=coefficient(n,k,gamma,beta)
                pred=cmath.exp(-1j*beta*k*n**(gamma/2))
                if gamma==1.:
                    pred*=math.exp(-(beta*k)**2/8)
                err=abs(val-pred)
                limit=(.5*k/math.sqrt(n) if gamma==1 else .5*k/n**.75)
                assert err < limit, (n,k,gamma,err)
                count+=1
            # gamma=2 is exactly integrable as a complex Gamma integral.
            val=coefficient(n,k,2.,beta)
            z=1+1j*beta*k
            exact=gamma_ratio(n,k)*z**(-(n+k/2+1))
            assert abs(val-exact) < 2e-8, (n,k,2,abs(val-exact))
            count+=1
    print('FOCK_CHIRP_NUMERICAL_PASS',count)
    # Fixed coefficient gamma identity and Gaussian critical density checks.
    assert all(0<gamma_ratio(n,k)<=1.00000001 for n in (32,128,512) for k in (1,2,4))
    print('FOCK_CHIRP_NORMALIZATION_PASS',9)

if __name__=='__main__':
    run()
