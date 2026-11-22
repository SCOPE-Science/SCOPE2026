"""Independent finite checks for a Fejer--BV integrated-error theorem.
Requires Python 3, NumPy and SciPy. Numerical tests are not infinite proofs.
"""
import math
import numpy as np
from scipy.integrate import quad
PI=math.pi
GAMMA=0.577215664901532860606512090082402431

def kern(n,t):
    return (1+2*sum((1-k/n)*math.cos(k*t) for k in range(1,n)))/(2*PI)

def arc_series(n,L):
    return L-L*L/(2*PI)-2/PI*sum((1-k/n)*(1-math.cos(k*L))/(k*k) for k in range(1,n))

def arc_integral(n,L):
    return 2*quad(lambda t: min(t,L)*kern(n,t),0,PI,epsabs=1e-10,epsrel=1e-10,limit=250)[0]

def opt(n):
    return PI/2-4/PI*sum((1-k/n)/(k*k) for k in range(1,n,2))

for n in (1,2,3,4,5,6,7,8,11,16,23,48):
    for L in (0.07,0.4,1.0,2.0,2.6,PI,4.1,5.4):
        # symmetry reduces all arcs to shorter complementary arcs
        z=min(L,2*PI-L)
        exact=arc_series(n,z)
        integ=arc_integral(n,z)
        assert abs(exact-integ)<4e-9,(n,L,exact,integ)
        assert exact<=opt(n)+3e-12
        if abs(z-PI)>1e-10:
            assert exact<opt(n)-1e-12
    assert abs(arc_series(n,PI)-opt(n))<1e-12
print('FINITE_FOURIER_VS_INTEGRAL_ARC_TESTS_PASS',12*8)

for n in (1,2,3,4,5,6,9,10,25):
    for d in (0.0125,0.018,0.025,0.036):
        defect=opt(n)-arc_series(n,PI-d)
        leading=(d*d/(2*PI*n) if n%2 else n*d**4/(48*PI))
        assert abs(defect/leading-1)<0.04,(n,d,defect,leading)
print('PARITY_QUADRATIC_QUARTIC_TESTS_PASS',9*4)

for n in (20,40,80,21,41,81):
    main=(2/(PI*n))*(math.log(2*n)+GAMMA+1)
    third=(-1/(3*PI*n**3) if n%2==0 else 2/(3*PI*n**3))
    rem=opt(n)-main-third
    assert abs(rem)<5/(n**5),(n,rem)
print('PARITY_THIRD_ORDER_ASYMPTOTIC_CHECKS_PASS',6)

rng=np.random.default_rng(1033)
M=4096
for n in (2,3,6,13):
    # The FFT computes values of the continuous Fejer convolution of a periodic
    # piecewise-constant input, sampled on a fine grid. Numerical Riemann sums
    # only approximate its L1 norm.
    mult=np.zeros(M)
    mult[0]=1
    for k in range(1,n):
        mult[k]=mult[-k]=1-k/n
    for _ in range(60):
        jumps=rng.choice(M,size=int(rng.integers(2,15)),replace=False)
        amps=rng.normal(size=len(jumps))
        dv=np.zeros(M)
        dv[jumps]=amps
        dv-=np.mean(dv)   # periodic step increments must sum to zero
        x=np.cumsum(dv)
        tv=np.abs(np.roll(x,-1)-x).sum()
        y=np.fft.ifft(np.fft.fft(x)*mult).real
        err=(2*PI/M)*np.abs(y-x).sum()
        assert err/tv<opt(n)+0.015,(n,err/tv,opt(n))
print('RANDOM_PERIODIC_BV_FFT_TESTS_PASS',4*60)
print('ALL_FEJER_BV_CHECKS_PASS')
