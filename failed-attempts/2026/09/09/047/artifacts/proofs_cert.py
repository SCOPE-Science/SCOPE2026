"""Exact certificates for the emergent route-separation theorem (lane-398).
Part A: E1 = 65 by exact integer arithmetic + threshold comparison.
Part B: rigorous rational lower bound c_* for A(15^k) >= c_*/15^k (LINEAR tail).
Part C: exact machine counts E2, E3 (deterministic brute force).
Uses only: pi_up = 3.1416 upper bound; cos t >= 1-t^2/2; |e^{it}-1| <= |t|;
global Lipschitz 2pi for nu_hat (support in [0,1]); resonance nu_hat(15n)=nu_hat(n).
"""
from fractions import Fraction
from collections import Counter
D = [0,1,2,13,14]
# ---- A ----
N = Counter(x+y for x in D for y in D)
assert sum(N.values()) == 25
E1 = sum(v*v for v in N.values())
print("pair sums:", sorted(N.items()))
print("E1 =", E1)
assert E1 == 65
thr = Fraction(5**4, 15)
print("threshold 5^4/15 =", thr)
assert E1 > thr
print("excess E1/threshold =", Fraction(E1*15, 625))
# ---- B (linear tail, correct: mean(d)=6 so |m(u)-1|<=12 pi |u|) ----
pi_up = Fraction(31416, 10000)
t1 = (2*pi_up/15); t2 = (4*pi_up/15)
cos1 = 1 - t1*t1/2; cos2 = 1 - t2*t2/2
m1 = (1 + 2*cos1 + 2*cos2)/5
print("m(1/15) >=", float(m1))
assert m1 > Fraction(82,100)  # 0.82
# tail j>=2: factor (1-12 pi 15^-j), product >= 1 - sum (Weierstrass product ineq.)
S = sum(12*pi_up*Fraction(1,15**j) for j in range(2,12)) + Fraction(1,10**9)  # j>=12 tail <1e-9
tail = 1 - S
print("tail >=", float(tail))
assert tail > Fraction(80,100)
nu1 = m1*tail
print("|nu_hat(1)| >=", float(nu1))
delta = Fraction(1,20)  # =0.05, near-optimal
eps1 = delta*delta/2
a = (nu1 - 2*pi_up*eps1)**2
b = (1 - 2*pi_up*delta)**2
c = a*b*delta/pi_up
print("a >=", float(a), " b >=", float(b))
print("c_* >=", float(c))
assert c > Fraction(30,10000)  # 0.003
print("CERTIFIED: A(15^k) >= 0.003/15^k for all k>=0 (normalized circular mean)")
# ---- C ----
W2 = [a+15*b for a in D for b in D]
c2 = Counter(p+q for p in W2 for q in W2)
E2 = sum(v*v for v in c2.values())
print("E2 =", E2)
assert E2 == 5265
W3 = [a+15*b+225*c for a in D for b in D for c in D]
c3 = Counter(p+q for p in W3 for q in W3)
E3 = sum(v*v for v in c3.values())
print("E3 =", E3)
assert E3 == 438945
print("budgets: (125/3)^1 =", 125/3, " (125/3)^2 =", (125/3)**2, " (125/3)^3 =", (125/3)**3)
print("excess:", 65/(125/3), 5265/((125/3)**2), 438945/((125/3)**3))
print("ALL CERTIFICATES PASS")
