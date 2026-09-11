"""Route A (rigorous, stdlib only): certify the 1D resonance constant c0 != 0.

mu1hat(xi) = prod_{k>=1} Phi(xi/20^k), Phi(v) = (1/6) sum_{j=0}^5 e^{-2 pi i j v}.
c0 := mu1hat(1). Exact identity: mu1hat(20^m) = c0 for all m>=1, since
Phi(integer) = 1 exactly, so mu1hat(20) = Phi(1)*prod_{k>=2} Phi(20^{1-k}) = c0.

Rigorous bounds used (pen-and-paper, reproduced numerically here):
  |Phi(v)-1| <= 5*pi*|v|,  |Phi(u)-Phi(u')| <= 5*pi*|u-u'|      (1)
  from |(1/6) sum_{j=0}^5 (e^{-2 pi i j v}-1)| <= (2 pi |v|/6)(0+..+5) = 5 pi |v|.
Hence |c0| >= prod_{k=1..3}(1-5 pi_up 20^{-k}) * (1 - 5 pi_up 20^{-3}/19),
via Weierstrass product inequality prod(1-a_k) >= 1 - sum a_k (a_k>=0).
"""
import math

PI_UP = math.pi + 1e-15  # rigorous upper bound (float pi error <= 1 ulp)

terms = [(1 - 5 * PI_UP * 20.0**-k) for k in (1, 2, 3)]
A = 5 * PI_UP * 20.0**-3 / 19.0
assert all(t > 0 for t in terms) and (1 - A) > 0
L_c0 = terms[0] * terms[1] * terms[2] * (1 - A)

# small-argument uniform bound: |mu1hat(xi)| >= 1 - 5 pi_up |xi|/19
def slow(xi):
    return 1 - 5 * PI_UP * abs(xi) / 19.0

print("ROUTE A CERTIFICATE")
print(f"PI_UP = {PI_UP!r}")
print(f"finite factors: {[f'{t:.10f}' for t in terms]}, tail factor {(1-A):.10f}")
print(f"|c0| >= {L_c0:.6f}")
assert L_c0 > 0.2, "certificate threshold"
print("PASS: |c0| > 0.2  (true value ~0.8616; margin >4x)")
print(f"small-arg check: |mu1hat(xi)| >= {slow(1/20):.6f} for |xi| <= 1/20")

# Non-rigorous numeric cross-check (labeled as such)
def Phi(v):
    return sum(cmath.exp(-2j * math.pi * j * v) for j in range(6)) / 6
import cmath
p = 1 + 0j
for k in range(1, 9):
    p *= Phi(1.0 / 20**k)
print(f"(non-rigorous cross-check) c0 ~= {p}  |c0| ~= {abs(p):.6f}")
print("CONSEQUENCE: no uniform 1D power decay |mu1hat(xi)| <= C|xi|^{-d}, d>0, exists;")
print("every tail-closure route needing uniform decay is structurally blocked.")
