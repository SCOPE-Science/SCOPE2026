"""Finite checks for a logarithmic inner-pullback Hardy Hankel theorem.
Run: python3 CHECK.py. The infinite-dimensional assertions use the proof, not this script.
"""
import math, cmath

PI=math.pi
checks=0

def ok(test, message):
    global checks
    assert test, message
    checks += 1

def base_symbol(w):
    return cmath.log((1+w)/(1-w))

def poisson(a, boundary):
    return (1-abs(a)**2)/abs(1-a.conjugate()*boundary)**2

def numerical_kernel_energy(d,a,M=8192):
    poiss_v=0.0
    poiss_square=0.0
    poisson_mean_im=0.0
    for j in range(M):
        t=2*PI*(j+0.371)/M
        z=cmath.exp(1j*t)
        w=cmath.exp(1j*d*t)
        f=base_symbol(w)
        weight=poisson(a,z)/M
        poiss_v += weight
        poiss_square += weight*abs(f)**2
        poisson_mean_im += weight*f.imag
    v=base_symbol(a**d)
    return poiss_square-abs(v)**2,poisson_mean_im,v.imag,poiss_v

for d in (1,2,3,5):
    for a in (0j, .20+.13j, -.18+.25j, .38-.11j):
        val,meanim,im,poiss_norm=numerical_kernel_energy(d,a)
        exact=PI**2/2 -2*im**2
        ok(abs(val-exact)<0.035, f'Poisson variance mismatch d={d},a={a},got={val},want={exact}')
        ok(abs(meanim-im)<0.005, f'Poisson harmonic mean d={d},a={a}')
        ok(abs(poiss_norm-1)<0.001, f'Poisson norm d={d},a={a}')

# Matrix of the compressed block on B^{2k} and conjugate B^{2j+1}
# is H_{1/2}(j,k)=1/(j+k+1/2), regardless of d or inner B.
def test_rayleigh(N):
    xs=[1/math.sqrt(j) for j in range(1,N+1)]
    q=sum(xs[i]*xs[j]/(i+j+2.5) for i in range(N) for j in range(N))
    norm=sum(x*x for x in xs)
    return q/norm

vals=[test_rayleigh(n) for n in (24,48,96,192)]
for n,v in zip((24,48,96,192), vals):
    ok(1.3<v<PI, f'Hilbert compression Rayleigh n={n}: {v}')
for i in range(3):
    ok(vals[i+1]>vals[i], 'Rayleigh increase')

# H2 norm of psi_B = 4 sum over odd square reciprocals = pi^2/2.
for n in (32,64,128,256):
    partial=sum(4/(2*j+1)**2 for j in range(n))
    ok(partial < PI**2/2 and 0<PI**2/2-partial<1/n, 'H2 series tail')
# Exact maximizer set of z^m: m diameters, half-angle directions.
for d in (1,2,3,4,5,6):
    for k in range(2*d):
        a=0.5*cmath.exp(1j*k*PI/d)
        im=base_symbol(a**d).imag
        ok(abs(im)<1e-12, 'norming ray')
    off=0.5*cmath.exp(1j*PI/(2*d))
    ok(abs(base_symbol(off**d).imag)>0.01, 'off-norming direction')

print(f'PASS: {checks} finite consistency checks; analytic proof handles all inner functions and infinite matrices.')
