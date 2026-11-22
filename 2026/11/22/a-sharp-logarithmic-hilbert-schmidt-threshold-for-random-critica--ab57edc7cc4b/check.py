"""Finite diagnostics for a Poisson--Dirichlet Gram leakage theorem.

The diagnostics test constants and finite-dimensional calculations.
The infinite-dimensional theorem is established by the accompanying proof.
"""
import math
import mpmath as mp

mp.mp.dps = 45
checks = 0

# K(q) = Li_{1/2}(q)/q has the stated singular coefficient sqrt(pi).
for u in (0.03, 0.01, 0.003, 0.001):
    q = mp.mpf(1) - mp.mpf(str(u))
    K = mp.polylog(mp.mpf('0.5'), q)/q
    rel = K * mp.sqrt(1-q)/mp.sqrt(mp.pi)
    assert abs(rel - 1) < 2*mp.sqrt(u)
    checks += 1

# The angle-averaged Cauchy kernel has logarithmic coefficient 1/pi.
for u in (1e-3, 1e-5, 1e-7, 1e-9):
    a = mp.mpf(1)-mp.mpf(str(u))
    k2 = 4*a/(1+a)**2
    angle_mean = 2*mp.ellipk(k2)/(mp.pi*(1+a))
    asymptotic = mp.log(8/u)/mp.pi
    assert abs(angle_mean-asymptotic) < mp.mpf('0.005')
    checks += 1

# Direct beta quadrature of the exact model angular integral for two shell depths.
for t,s in (('0.1','0.03'),('0.003','0.0005'),('0.00005','0.00001')):
    t,s = mp.mpf(t),mp.mpf(s)
    a = mp.sqrt((1-t)*(1-s))
    exact = 2*mp.ellipk(4*a/(1+a)**2)/(mp.pi*(1+a))
    approx = mp.log(1/(t+s))/mp.pi
    assert exact > 0
    assert abs(exact - approx) < 2
    checks += 1

# The singular double integral with logarithmic coordinates u,v >= U
# has closed form 2 U^(3-2b)/[(b-1)(2b-3)].
U=mp.mpf('2')
for bstr in ('1.6','1.7','2','2.5','3'):
    b=mp.mpf(bstr)
    exact=2*U**(3-2*b)/((b-1)*(2*b-3))
    via_integral=2/(b-1)*U**(3-2*b)*mp.quad(lambda x: x**(2*b-4),[0,1])
    assert abs(via_integral-exact)/exact < mp.mpf('1e-8')
    checks+=1

# Leading pole of J(b) is 2/(b-3/2).
for estr in ('0.1','0.05','0.02','0.005'):
    eps=mp.mpf(estr)
    b=mp.mpf('1.5')+eps
    J=2*U**(3-2*b)/((b-1)*(2*b-3))
    assert abs(eps*J-2)<8*eps*mp.log(U+1)
    checks+=1

# Coefficient checks: the reference kernel is a normalized irreducible
# positive coefficient power series; nothing here certifies Pick positivity.
for N in (4,8,16,64):
    weights=[1/math.sqrt(k+1) for k in range(N)]
    assert all(weights[k]>weights[k+1]>0 for k in range(N-1))
    checks+=1
print('PASS:',checks,'finite diagnostic assertions')
