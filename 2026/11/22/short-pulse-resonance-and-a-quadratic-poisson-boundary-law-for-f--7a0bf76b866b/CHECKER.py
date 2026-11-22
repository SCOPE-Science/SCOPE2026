"""Independent numerical checks of the Fourier, stable-scale and critical crossover identities.

This program verifies finite arithmetic and numerical evaluations only; the analytic
claims for all exponents and times are established by the accompanying proof.
"""
import math
from scipy.integrate import quad
from scipy.optimize import minimize_scalar
import numpy as np

COUNT=0
def check(statement,detail):
    global COUNT
    assert statement, detail
    COUNT+=1

def g(a,x):
    if x==0: return 0.0 if a>1 else 1.0
    return (-math.expm1(-x**a))**2/(x*x)

def F(a,z):
    # QUADPACK computes oscillatory Fourier integrals by Fourier-cycle extrapolation.
    val,err=quad(lambda u:g(a,u),0,math.inf,weight='cos',wvar=z,
                 epsabs=2e-11, limit=300,limlst=250)
    return val

def B(a):
    return math.gamma(1-1/a)*(1-2**(1/a-1))/math.pi

def E(a,z):
    return B(a)-F(a,z)/(2*math.pi)

def R(a,h,d,nmax=20000):
    n=np.arange(1,nmax+1,dtype=float)
    x=2*math.pi*n*h
    w=-np.expm1(-x**a)
    return np.sum((w*w)*(np.sin(math.pi*n*d)**2)/(2*math.pi**2*n*n))

# Analytic calibration at the Poisson endpoint: F_1 is a strictly positive Laplace mixture.
for z in (0.5,1,2,5,25,100):
    check(F(1.,z)>0,('positive Poisson Fourier transform',z))

for a in (1.08,1.2,1.5,1.8):
    integ=quad(lambda u:g(a,u),0,math.inf,epsabs=1e-10)[0]
    check(abs(integ-2*math.pi*B(a))<1e-7,('integral identity',a,integ,B(a)))
    # Sign of large frequency cosine transform is negative for all 1<alpha<2.
    z=1000 if a<1.5 else 100
    fa=F(a,z)
    check(fa<0,('negative Fourier tail',a,z,fa))
    # The maximizing pulse has strictly greater error than the far-separated-jump value.
    sol=minimize_scalar(lambda s:F(a,s), bounds=(.3,80),method='bounded',
                        options={'xatol':1e-6})
    check(sol.fun<0,('short pulse',a,sol.fun))
    for h in (0.02,0.008):
        d=h*sol.x
        if d<0.49:
            val=R(a,h,d)
            check(abs(val/h-E(a,sol.x))<0.12*E(a,sol.x),
                  ('discrete circle vs continuum',a,h,val/h,E(a,sol.x)))

# Critical law for consecutive exponents: relative errors shrink as epsilon decreases.
latest=[]
for eps in (0.025,0.01,0.005):
    a=1+eps
    sol=minimize_scalar(lambda z:F(a,z),bounds=(0.2/eps,1.5/eps),
                        method='bounded',options={'xatol':2e-5})
    check(sol.fun<0,('critical negative minimum',eps))
    scaled=eps*sol.x
    gain=-sol.fun/(2*math.pi*eps**2)
    check(abs(scaled-2/math.pi)<0.032,('critical location',eps,scaled))
    check(abs(gain-math.pi/8)<0.065,('critical gain',eps,gain))
    latest.append((eps,scaled,gain))
check(abs(latest[-1][1]-2/math.pi)<abs(latest[0][1]-2/math.pi),
      ('critical location convergence',latest))
check(abs(latest[-1][2]-math.pi/8)<abs(latest[0][2]-math.pi/8),
      ('critical coefficient convergence',latest))

# Fourier/Parseval check for a single arc by synthesizing the sample function and
# smoothed series on a grid; truncation error in the step is kept explicit.
a,h,d=1.5,0.022,0.06
for N in (800,1600):
    x=np.arange(N)/N
    arr=((x>=0)&(x<d)).astype(float)
    freqs=np.fft.fftfreq(N,1/N)
    transformed=np.fft.ifft(np.fft.fft(arr)*(1-np.exp(-(2*math.pi*np.abs(freqs)*h)**a)))
    observed=np.mean(np.abs(transformed)**2)/4
    analytic=R(a,h,d,50000)
    check(abs(observed-analytic)<0.00015,('FFT vs analytic series',N,observed,analytic))

print(f'PASS: {COUNT} numerical/identity checks; finite computations are corroboration, not proof.')
print('Critical sequence (eps, eps*z_optimizer, excess/eps²):')
for item in latest: print(' '.join(f'{z:.12g}' for z in item))
