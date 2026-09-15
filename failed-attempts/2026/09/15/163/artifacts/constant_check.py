"""Verify the leading-constant optimization behind Construction H.

Reconstruction: take an unbalanced bipartite C4-free graph G=(U,V) with
|U|=alpha*n, |V|=(1-alpha)*n; pair up neighbours of each u in U into triples
{u} U {v,v'}. #hyperedges = e(G)/2. KST: sum_u C(d_u,2) <= C(|V|,2) gives
d_bar <= |V|/sqrt(|U|), so m <= |U|*|V|/(2*sqrt(|U|)) = f(alpha)*n^{3/2}
with f(alpha) = sqrt(alpha)*(1-alpha)/2. Maximise over alpha in (0,1).
Expected: alpha=1/3, f=1/(3*sqrt(3)).
"""
import math

def f(a):
    return math.sqrt(a) * (1 - a) / 2

best_a, best_f = max(((a, f(a)) for a in (i / 10**6 for i in range(1, 10**6))), key=lambda t: t[1])
target = 1 / (3 * math.sqrt(3))
print(f"numerical maximiser alpha = {best_a:.6f} (expect 0.333333)")
print(f"numerical max f         = {best_f:.9f}")
print(f"1/(3*sqrt(3))          = {target:.9f}")
print(f"|diff|                 = {abs(best_f - target):.2e}")
# closed form: f^2 = a(1-a)^2/4; d/da [a(1-a)^2] = (1-a)(1-3a) -> a=1/3
a = 1/3
assert abs(f(a) - target) < 1e-15, "closed-form check failed"
assert abs(best_a - 1/3) < 2e-6 and abs(best_f - target) < 1e-9
print("PASS: balanced Construction H has alpha=1/3, constant 1/(3*sqrt(3))")
