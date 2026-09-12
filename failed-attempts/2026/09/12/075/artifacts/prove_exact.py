"""Prove exact formula log Z_n = F0 n^2 + F1 n + C_{n mod 4} for the CJ Kasteleyn determinant?
Need analytic proof of closed form for det K_{a,1}. Approach: domino shuffling / spider move.
Known: two-periodic weights are 4-periodic under shuffling (Chhita-Young). The partition functions
T_n(i,j) (refined, with face weights varying) satisfy octahedron recurrence; the *unrefined* Z_n(a)
may satisfy a closed 4-step recurrence with explicit coefficients, which the data confirm:
  Z_n Z_{n-4} / Z_{n-2}^2 = e^{8F0} * e^{C_r + C_{r} - 2C_{r+2}}... but C_0=C_2=0, C_1,C_3 as above.
Let's compute the exact recurrence coefficients from data and try to identify them as rational functions of a.
Also directly test candidate closed form Z_n = exp(F0 n^2 + F1 n + C_r) i.e.
  Z_n = (2a(1+a^2))^{n^2/4} (2a)^{n/2} e^{C_r}.
e^{C_0}=1, e^{C_2}=1, e^{C_3}=(2a)^{1/2}/(2a(1+a^2))^{1/4}, e^{C_1}=a(2a)^{1/2}/(2a(1+a^2))^{1/4}.
"""
import math
from kasteleyn import logZ
def F0(a): return 0.25*math.log(2*a*(1+a*a))
def F1(a): return 0.5*math.log(2*a)
def C(a,r):
    if r in (0,2): return 0.0
    if r==3: return F1(a)-F0(a)
    return F1(a)-F0(a)+math.log(a)
ok=True
for a in [0.13,0.37,0.61,0.83,1.7,2.3]:
    for n in range(1,17):
        pred=F0(a)*n*n+F1(a)*n+C(a,n%4)
        err=abs(pred-logZ(n,a))
        if err>5e-9:
            print(f"FAIL a={a} n={n} err={err:.3e}"); ok=False
print("exact closed form holds for all tested a,n" if ok else "FAILED")
# print Z in factored form
for a in [0.3,0.7]:
    print(f"a={a}: F0={F0(a):.10f} F1={F1(a):.10f} C1={C(a,1):.10f} C3={C(a,3):.10f}")
