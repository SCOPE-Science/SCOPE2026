"""Bounded recovery test: naive crystal-only product box overcounts cyclotomic nilHecke.

Target claims a uniform monomial basis indexed only by categorical-crystal/path
data. The simplest uniform candidate is a product box:
  { x_1^{a_1} ... x_n^{a_n} tau_w e(nu) : 0 <= a_k < l, w in S_n },
where l = <h_i, Lambda> is the only crystal/weight datum visible at the first
strand. We compare its size against the known cyclotomic nilHecke dimensions.

Known theorem (cyclotomic nilHecke NH_n^l, type A1, Lambda = l*Lambda_0):
  NH_n^l = 0 for n > l, and for 0 <= n <= l it has basis
    { x_1^{a_1}...x_n^{a_n} tau_w : w in S_n, 0 <= a_k <= l-k },
  so dim = n! * l! / (l-n)!.
The naive box has size n! * l^n, strictly larger for 1 < n <= l.
This shows a crystal-weight-only box cannot be a basis uniformly already in the
target's own claimed specialization case; the true bound (a_k <= l-k) uses
position-dependent Schubert-type truncation coming from KLR relations, not from
crystal data alone.

We also record the mechanism: from KLR relations tau_1 x_2 = x_1 tau_1 + 1 (up to
sign/convention) and x_1^l = 0, tau_1^2 = 0 in the relevant corner, one derives
relations such as x_2^l tau_1 in span of smaller monomials, i.e. dependence among
box monomials invisible to crystal-only counting.
"""
import math

def known_dim(n, l):
    if n > l:
        return 0
    return math.factorial(n) * math.factorial(l) // math.factorial(l - n)

def naive_box(n, l):
    return math.factorial(n) * (l ** n)

print("n l | naive_box known_dim overcount_factor")
for (n, l) in [(2, 2), (2, 3), (3, 3), (3, 4)]:
    nb = naive_box(n, l)
    kd = known_dim(n, l)
    print(f"{n} {l} | {nb:9d} {kd:9d} {nb/kd if kd else float('inf'):.3f}")

# Explicit small enumeration for n=2, l=2:
# naive box: a1,a2 in {0,1}, w in {1,s1} -> 8 monomials
# known dim 4; known basis: a1<=1, a2<=0 -> (a1 in {0,1}, a2=0) x 2 = 4.
naive = [(a1, a2, w) for a1 in [0, 1] for a2 in [0, 1] for w in ["1", "s1"]]
known = [(a1, a2, w) for a1 in [0, 1] for a2 in [0] for w in ["1", "s1"]]
print("\nn=2,l=2 naive box size:", len(naive), "known dim:", len(known))
print("naive set:", naive)
print("known basis (a1<=1,a2<=0):", known)
print("RESULT: naive uniform box OVERCOUNTS by factor", len(naive) / len(known))
print("CONCLUSION: uniform crystal-weight-only product box FAILS as basis.")
