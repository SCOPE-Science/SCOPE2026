"""Finite numerical consistency tests for the explicit rational-window constants.

Run: python CHECK.py. This does not certify the global Zak-zero theorem.
"""
import cmath
import math

p=math.pi
q=math.exp(-2*p)
csch=lambda t:1/math.sinh(t)
coth=lambda t:1/math.tanh(t)
h0=p/3*(coth(p)-coth(2*p)/2)
h1=p/3*(csch(p)-csch(2*p)/2)
d0=p*p/3*(csch(p)**2-csch(2*p)**2)
d1=p*p/3*(csch(p)*coth(p)-csch(2*p)*coth(2*p))
b0=-2*p*p/3*(1-q)/(1+q)
b1=4*p*p*math.sqrt(q)/3*(1-math.sqrt(q))**2/(1-q*q)
CR=(h0*d1-h1*d0)**2/(d0*d0+d1*d1)
CI=(h0*b1-h1*b0)**2/(b0*b0+b1*b1)
assert 0.2677<CR<0.2678 and 0.0169<CI<0.0170
assert CR/CI>15

# Independent integer-lattice sums, with a convergence allowance appropriate to the
# frequency derivative of an algebraically decaying odd window.
N=9000
def bare(t): return t/((t*t+1)*(t*t+4))
def even(t): return 1/((t*t+1)*(t*t+4))
def zak(x,w):
    o=0j; h=0j
    for n in range(-N,N+1):
        t=x-n
        ph=cmath.exp(2j*p*n*w)
        o+=bare(t)*ph; h+=even(t)*ph
    return o,h

def near(a,b,eps): assert abs(a-b)<eps, (a,b,eps)

for w,h,d,b in [(0,h0,d0,b0),(.5,h1,d1,b1)]:
    z,k=zak(0,w)
    near(z,0,1e-8)
    near(k,h,1e-8)
    r=1e-4
    dd=(zak(r,w)[0]-zak(-r,w)[0])/(2*r)
    near(dd,d,2e-6)
    # Derivative obtained by differentiating the finite Zak sum exactly.
    db=0j
    for n in range(-N,N+1):
        db+=2j*p*n*bare(-n)*cmath.exp(2j*p*n*w)
    near(db,1j*b,0.002)

# Check predicted least-square positions and the sharp quadratic slopes.
for phase,C in [('real',CR),('imag',CI)]:
    for t in [0.004,0.002]:
        u,v=(t,0) if phase=='real' else (0,t)
        x=-(h0*d0+h1*d1)/(d0*d0+d1*d1)*u
        w=-(h0*b0+h1*b1)/(b0*b0+b1*b1)*v
        z0,k0=zak(x,w)
        z1,k1=zak(x,w+.5)
        trial=abs(z0+(u+1j*v)*k0)**2+abs(z1+(u+1j*v)*k1)**2
        near(trial/t**2,C,0.0002)
print('CHECK_OK: formulas, Zak values, derivatives, and local sharp quadratic trials')
