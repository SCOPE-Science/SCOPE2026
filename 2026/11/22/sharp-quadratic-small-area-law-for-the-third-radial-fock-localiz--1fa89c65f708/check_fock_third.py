"""Finite independent numerical diagnostics for radial Fock localization.

Uses Python's standard library; the proof is analytic and is not replaced by tests.
"""
import math

checks = 0

def verify(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

left, right = 1.0, 2.0
for _ in range(100):
    mid = (left + right) / 2
    if (2-mid)*math.exp(mid) > 2:
        left = mid
    else:
        right = mid
t = (left + right) / 2
A = math.exp(-t)
B = t*t*A/2
c = B/(1+B-A)
p = (B-A)/(1+B-A)
u = p*p/(2*(1-A+B))
verify(abs((2-t)*math.exp(t)-2) < 1e-12, "root equation")
verify(1 < t < 2 and 0 < p < 1, "parameter ranges")
verify(abs((1-p)*B-c) < 1e-12, "mode two balance")
verify(abs(p+(1-p)*A-c) < 1e-12, "mode zero balance")
verify(abs(c*(1-A)-(1-c)*B) < 1e-12, "dual weight identity")
verify(c > math.exp(-math.sqrt(2)), "strict annular gap")
verify(c > 4.5*math.exp(-3), "high-mode gap")

def density(j, x):
    return math.exp(-x)*x**j/math.factorial(j)

def mass(j, lo, hi):
    # Integer-shape gamma integral, stable at these diagnostic scales.
    def survival(x):
        return math.exp(-x)*math.fsum(x**k/math.factorial(k) for k in range(j+1))
    return survival(lo)-survival(hi)

for k in range(1601):
    x = 25*k/1600
    dual = c*density(0,x)+(1-c)*density(2,x)
    verify(dual <= c+2e-14, "sampled dual certificate")
for s in (0.12,0.08,0.05,0.03,0.02,0.01,0.005):
    ps=p+u*s
    lo=t-(1-ps)*s/2
    hi=t+(1-ps)*s/2
    vals=[mass(j,0,ps*s)+mass(j,lo,hi) for j in range(12)]
    order=sorted(range(12),key=lambda j:-vals[j])
    third=vals[order[2]]
    prediction=c*s-c*p*p*s*s/2
    verify(set(order[:3])=={0,1,2}, "third eigenvalue modes")
    verify(third < c*s, "global envelope")
    verify(abs(third-prediction) < 0.008*s**3, "cubic remainder diagnostic")
    verify(vals[1] > vals[0] and vals[1] > vals[2], "strict middle mode")
print("FOCK_THIRD_CHECK_OK", checks, "finite assertions")
