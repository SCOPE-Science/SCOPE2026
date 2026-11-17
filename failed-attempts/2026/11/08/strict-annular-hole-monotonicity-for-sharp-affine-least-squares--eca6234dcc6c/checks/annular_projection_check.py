"""Independent diagnostics for the exact annular affine projection norm.

The accompanying proof, not this finite set of checks, establishes all-parameter
strict monotonicity and norm-attainment.
"""
from sympy import symbols, simplify, diff, pi, sqrt, asin
from mpmath import mp


t = symbols('t', real=True, nonnegative=True)
A = 16*t/(1+t)**2
B = 16/(1+t)**2
assert simplify(diff(A,t) - 16*(1-t)/(1+t)**3) == 0
assert simplify(diff(B,t) + 32/(1+t)**3) == 0
assert simplify((A+B)/2-8/(1+t)) == 0
assert simplify((B-A)-16*(1-t)/(1+t)**2) == 0

mp.dps = 45

def h(z):
    z=mp.mpf(z)
    if z <= 1:
        return mp.mpf(1)
    return (2/mp.pi)*(mp.sqrt(z*z-1)+mp.asin(1/z))

def F(q):
    q=mp.mpf(q)
    if q<=1:
        return q
    return q*h(mp.sqrt(q))-2/(3*mp.pi)*(q-1)**mp.mpf('1.5')

def formula(a):
    a=mp.mpf(a)
    if a == 1:
        return h(2)
    lo=16*a*a/(1+a*a)**2
    hi=16/(1+a*a)**2
    return (F(hi)-F(lo))/(hi-lo)

def via_radial(a):
    a=mp.mpf(a)
    if a==1:
        return h(2)
    return mp.quad(lambda u: h(4*mp.sqrt(a*a+(1-a*a)*u)/(1+a*a)), [0,1])

radii=['0','0.05','0.18','0.25','0.4','0.62','0.77','0.91','0.98','1']
results=[formula(a) for a in radii]
for a, exact in zip(radii, results):
    direct=via_radial(a)
    assert abs(exact-direct)<mp.mpf('8e-8'), (a,exact,direct)
assert all(results[j]>results[j+1] for j in range(len(results)-1))
L_disk=11*mp.sqrt(15)/(8*mp.pi)+2*mp.asin(mp.mpf(1)/4)/mp.pi
L_circle=mp.mpf(1)/3+2*mp.sqrt(3)/mp.pi
assert abs(formula(0)-L_disk)<mp.mpf('1e-40')
assert abs(formula(1)-L_circle)<mp.mpf('1e-40')
lead_hole=1-mp.sqrt(15)/(8*mp.pi)-2*mp.asin(mp.mpf(1)/4)/mp.pi
for aa in [mp.mpf('0.0001'),mp.mpf('0.001')]:
    approx=L_disk-lead_hole*aa**2
    assert abs(formula(aa)-approx)<4*aa**4
for aa in [mp.mpf('0.9999'),mp.mpf('0.999')]:
    approx=L_circle+mp.sqrt(3)/mp.pi*(1-aa)
    assert abs(formula(aa)-approx)<3*(1-aa)**2
assert L_disk> L_circle>1
print('EXACT_ENDPOINT_FORMULAS_OK')
print('SYMBOLIC_MOVING_BOUNDARY_IDENTITIES_OK')
print('INDEPENDENT_RADIAL_INTEGRATION_AND_MONOTONIC_SAMPLES_OK',len(radii))
print('HOLE_AND_THIN_RING_ASYMPTOTICS_OK')
print('ALL_ANNULAR_AFFINE_PROJECTION_CHECKS_PASSED')
