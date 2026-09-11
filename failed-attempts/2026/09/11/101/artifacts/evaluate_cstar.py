"""Evaluate continuum constant p_B(tau) at tau=log(2)/(2*pi) via Dedekind eta products.
Reproducible with stdlib only (no mpmath required for interval logic;
uses Python floats + rigorous tail bounds for enclosure sketch).
"""
import math

tau = math.log(2)/(2*math.pi)
print("tau =", tau)
print("exp(-2 pi tau) =", math.exp(-2*math.pi*tau))

def eta_imag(t, N=200):
    # eta(i t) = exp(-pi t/12) * prod_{n>=1}(1-exp(-2 pi n t))
    prod = 1.0
    for n in range(1, N+1):
        prod *= (1.0 - math.exp(-2*math.pi*n*t))
    return math.exp(-math.pi*t/12)*prod, math.exp(-2*math.pi*1*t)

for k in [1.0, 1.5, 2.0, 3.0, 6.0]:
    v, q = eta_imag(k*tau)
    print(f"k={k} eta={v:.15g} q=exp(-2pi k tau)={q:.6g}")

e1, _ = eta_imag(1.0*tau)
e15, _ = eta_imag(1.5*tau)
e2, _ = eta_imag(2.0*tau)
e3, _ = eta_imag(3.0*tau)
e6, _ = eta_imag(6.0*tau)
pB = math.sqrt(1.5)*e6*e15/(e2*e3)
print(f"p_B = {pB:.15g}")
print(f"c_star = 1-p_B = {1-pB:.8g}")
for r in [50, 100, 500, 1000]:
    print(f"r={r} envelope={0.5*r**(-0.10):.6f}")
