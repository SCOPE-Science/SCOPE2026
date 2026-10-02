"""Corrected high-precision constants for cubic-trace variance in the symmetric
quartic two-cut model V(x)=x^4/4-2x^2.

The discrete-Gaussian coupling is the derivative of the equilibrium cubic
moment with respect to the positive-cut filling fraction.  On
 y^2=(z^2-2)(z^2-6), the normalized filling variation is
 (pi/fA) dz/y, hence [z^-4] gives c0 = 4*pi/fA.
"""
from mpmath import mp
mp.dps = 80

a = mp.sqrt(2); b = mp.sqrt(6)

def s(x):
    return mp.sqrt((x*x-2)*(6-x*x))

fA = mp.quad(lambda x: 1/s(x), [a,b])
fB = mp.re(mp.quad(lambda x: 1/mp.sqrt((x*x-2)*(x*x-6)), [-a,a]))
t = fB/fA
q = mp.e**(-mp.pi*t)

# Genus-one zero-A-period kernel constant used in the original computation.
def K(x2):
    return mp.quad(lambda x: (x*x*x2*x2 - 4*x*x - 4*x2*x2 + 12)/(((x-x2)**2)*s(x)), [a,b])
C = -K(mp.mpf('0'))/(2*fA)
c = 2*C
VG = 8*c + 16

N = 80
eden = sum(q**(k*k) for k in range(-N,N+1))
enum = sum((k*k)*q**(k*k) for k in range(-N,N+1))
Ve = enum/eden
oden = sum(q**((mp.mpf(k)+mp.mpf('0.5'))**2) for k in range(-N,N))
onum = sum((mp.mpf(k)+mp.mpf('0.5'))**2*q**((mp.mpf(k)+mp.mpf('0.5'))**2) for k in range(-N,N))
Vo = onum/oden

# Correct coefficient: derivative of the cubic moment with respect to filling.
c0 = 4*mp.pi/fA
v_even = VG + c0*c0*Ve
v_odd = VG + c0*c0*Vo

print('fA =', fA)
print('fB =', fB)
print('t =', t)
print('q =', q)
print('C =', C)
print('c =', c)
print('VG =', VG)
print('c0 = 4*pi/fA =', c0)
print('c0^2 =', c0*c0)
print('Ve =', Ve)
print('Vo =', Vo)
print('v_even =', v_even)
print('v_odd =', v_odd)
print('gap =', v_odd-v_even)
assert v_odd-v_even > 50
