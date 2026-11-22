"""Reproduce scalar spectral identities and Markov-step tests for fractional resolvent cubature."""
import math
import mpmath as mp
mp.mp.dps = 70
K = mp.mpf(8)
PI = mp.pi
A = PI**2/4

def base(x, m=None):
    if m is None:
        mid=int(mp.floor(x/K))
        indices=range(mid-40,mid+41)
    else:
        indices=range(-m,m+1)
    return K/(2*PI)*mp.fsum(1/mp.cosh((K*l-x)/2) for l in indices)

def fourier(x, n=48):
    return 1+2*mp.fsum(mp.cos(2*PI*j*x/K)/mp.cosh(A*j) for j in range(1,n+1))

def spectrum_lambda(m, j):
    return 4*m*m*mp.sin(PI*j/m)**2

def scalar_B(lam, m):
    if not lam:return mp.mpf(0)
    x=mp.log(lam)
    return mp.sqrt(lam)*base(x,m)

checks=0
for x in [-17,-8,-4,-1,0,mp.mpf('1.3'),4,7,14,21]:
    assert abs(base(mp.mpf(x))-fourier(mp.mpf(x)))<mp.mpf('1e-45')
    checks+=1
rplus=fourier(0);rminus=fourier(4)
assert 1 <rplus<2 and 0<rminus<1
assert (mp.sqrt(2)/4)*(1+4/(mp.exp(A)-1)) < mp.mpf("0.5")
checks+=2
# Independent Fourier spectral reconstruction of each finite-cycle step.
for m in [4,6,8,10,12]:
    lambdas=[spectrum_lambda(m,j) for j in range(m)]
    B=[scalar_B(lam,m) for lam in lambdas]
    p=[(1-(B[j]/(4*m))) for j in range(m)]
    coeff=[mp.fsum(p[j]*mp.cos(2*PI*j*r/m) for j in range(m))/m for r in range(m)]
    assert abs(mp.fsum(coeff)-1)<mp.mpf('1e-55')
    checks+=1
    for c in coeff:
        assert c >= -mp.mpf('1e-55')
        checks+=1
    assert abs(mp.fsum(coeff[r]*((-1)**r) for r in range(m))-p[m//2])<mp.mpf('1e-55')
    checks+=1
# Direct resolvent assembly, independent of the Fourier reconstruction.
for m in [4,6]:
    G=mp.matrix(m)
    for i in range(m):
        G[i,i]=2*m*m
        G[i,(i-1)%m]-=m*m
        G[i,(i+1)%m]-=m*m
    I=mp.eye(m)
    Q=mp.matrix(m)
    for ell in range(-m,m+1):
        t=mp.exp(K*ell)
        Q+=(K/PI)*mp.exp(K*ell/2)*G*mp.inverse(G+t*I)
    P=I-Q/(4*m)
    eig=[1-scalar_B(spectrum_lambda(m,j),m)/(4*m) for j in range(m)]
    for r in range(m):
        val=mp.fsum(eig[j]*mp.cos(2*PI*j*r/m) for j in range(m))/m
        assert abs(val-P[0,r])<mp.mpf('1e-55')
        checks+=1
# The logarithmic truncation error is bounded by a positive geometric tail.
for m in [4,6,8,10,20,26,40,60,100,200]:
    x=mp.log(4*m*m)
    error=base(x)-base(x,m)
    bound=(K/PI)*(mp.exp(-(K*(m+1)-x)/2)+mp.exp(-(K*(m+1)+x)/2))/(1-mp.exp(-K/2))
    assert error>=-mp.mpf("1e-60") and error<=bound+mp.mpf("1e-60")
    checks+=2
for j in range(1,4):
    for phase,limit in [(0,rplus),(4,rminus)]:
        m=2*int(mp.floor(mp.exp(4*j+phase/2)/4))
        x=mp.log(4*m*m)
        # Nearby resolvent terms dominate this exact finite sum.
        rr=base(x,min(m,80))
        assert abs(rr-limit)<mp.mpf(3)*mp.exp(-4*j)
        checks+=1
print('VERIFY_OK',checks,'checks')
print('R_plus',mp.nstr(rplus,35))
print('R_minus',mp.nstr(rminus,35))
print('amplification_plus',mp.nstr(1-rplus/2,35))
print('amplification_minus',mp.nstr(1-rminus/2,35))
