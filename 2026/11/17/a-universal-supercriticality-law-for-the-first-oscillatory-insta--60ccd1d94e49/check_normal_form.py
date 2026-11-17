"""Self-contained symbolic checks and a finite dynamical diagnostic for a cyclic quadratic map."""
import cmath
import math
import sympy as sp

A, B, S = sp.symbols('A B S', positive=True, real=True)
C = A**2 + B**2
R = 2*S*A/C
c = A+sp.I*B
lam = 1-R*c/S
q = -R*sp.conjugate(c)
d = 2*R*A*(S+c)
H = q/(sp.conjugate(lam)**2-lam)
L = d+2*q*sp.conjugate(H)
radial = sp.simplify(sp.re(sp.expand_complex(sp.conjugate(lam)*L)))
assert sp.simplify(radial+2*R*A*A*(1+R)) == 0
assert sp.simplify(sp.expand_complex(lam*sp.conjugate(lam))) == 1
assert sp.simplify(sp.re(sp.expand_complex(sp.conjugate(lam)*(S+c)))-(S-A-R*A)) == 0

alpha, beta = sp.symbols('alpha beta', nonnegative=True, real=True)
a = 1-(alpha+beta)/2
b = sp.sqrt(3)*(alpha-beta)/2
s = 1+alpha+beta
assert sp.simplify((a*a+b*b)-s*a-sp.Rational(3,2)*(alpha*alpha+beta*beta-alpha-beta)) == 0

al, be = sp.Rational(3,2), sp.Rational(1,10)
s0 = 1+al+be
a0 = 1-(al+be)/2
b0 = sp.sqrt(3)*(al-be)/2
r0 = sp.factor(R.subs({A:a0,B:b0,S:s0}))
assert r0 == sp.Rational(104,151)
assert sp.factor(radial.subs({A:a0,B:b0,S:s0})) == -sp.Rational(10608,114005)

# Compare exact Fourier equations to a direct independent three-coordinate expansion.
omega = -sp.Rational(1,2)+sp.sqrt(3)*sp.I/2
r, w, v, rate = sp.symbols('r w v rate')
u = [1/s0+r+w*omega**j+v*omega**(-j) for j in range(3)]
updated = [sp.expand(u[j]+rate*u[j]*(1-u[j]-al*u[(j+1)%3]-be*u[(j+2)%3])) for j in range(3)]
real_mode = sp.expand(sum(updated)/3-1/s0)
complex_mode = sp.expand(sum(updated[j]*omega**(-j) for j in range(3))/3)
mode_c = a0+sp.I*b0
expected_real = (1-rate)*r-rate*(s0*r*r+2*a0*w*v)
expected_complex = (1-rate*mode_c/s0)*w-rate*((s0+mode_c)*r*w+sp.conjugate(mode_c)*v*v)
assert sp.simplify(sp.expand_complex(real_mode-expected_real)) == 0
assert sp.simplify(sp.expand_complex(complex_mode-expected_complex)) == 0

lc = sp.simplify(1-r0*mode_c/s0)
assert sp.simplify(lc*sp.conjugate(lc)-1) == 0
assert -1 < 1-r0 < 1
for power in range(1,5):
    assert sp.simplify(lc**power-1) != 0

# A finite numerical test of the leading Fourier radius, not a theorem proof.
Rvalue = float(r0)+0.005
x0 = float(1/s0)
u = [x0+0.01, x0-0.006, x0-0.004]
for _ in range(90000):
    x,y,z = u
    u = [x+Rvalue*x*(1-x-float(al)*y-float(be)*z),
         y+Rvalue*y*(1-float(be)*x-y-float(al)*z),
         z+Rvalue*z*(1-float(al)*x-float(be)*y-z)]
    assert all(math.isfinite(t) and t>0 for t in u)
zz = sum((u[j]-x0)*cmath.exp(-2j*math.pi*j/3) for j in range(3))/3
empirical = abs(zz)
predicted = math.sqrt(0.005/(2*float(r0)*float(a0)*float(s0)*(1+float(r0))))
assert abs(empirical/predicted-1)<0.04,(empirical,predicted)
print('PASS: global symbolic cubic identity and sharp-crossing polynomial')
print('PASS: direct quadratic Fourier reconstruction and nonresonant rational sample')
print('PASS: finite near-onset amplitude diagnostic (not an existence proof)')
print(f'  onset R={r0}, cubic=-10608/114005, measured |w|={empirical:.8f}, leading={predicted:.8f}')
