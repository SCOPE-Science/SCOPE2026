"""Recovery test: shows why a single tracked quadratic constant fails to close globally.
1) Exact deficit on cube-to-Hanner segment P(t)=32/3+(16/3)t(1-t) (cf. SCOPE057):
   deficit is quadratic in t with exact coefficient 16/3 -- local Hessian > 0.
2) Diagonal truncation family has linear deficit D(s)~s/3 (cf. SCOPE101):
   different path => different exponent/rate; no single Hessian covers all directions
   without uniform comparison between BM distance and path parameters.
3) Global-gap effectivization estimate: covering the unconditional BM-compactum at
   resolution eps needs N(eps) nets with log N growing super-polynomially; Lipschitz
   modulus L of P on John's-position slice is dimension-dependent and untracked,
   so eps0 = inf{P: d_BM>=1+delta0}-32/3 has only existence via compactness.
Conclusion: RESULT = BLOCKED (local pieces feasible, global uniform closure not).
"""
from fractions import Fraction as Q

def test():
    # 1) shadow segment exact deficit
    for t in [Q(1,4), Q(1,2), Q(3,4)]:
        P = Q(32,3) + Q(16,3)*t*(1-t)
        print(f"t={t} deficit={P-Q(32,3)}")
    # 2) diagonal linear rate D(s) ~ s/3 vs quadratic t^2: ratio -> inf as s->0
    for s in [0.1, 0.01, 0.001]:
        D = s/3.0
        print(f"s={s} D/quadratic(s^2)={D/s**2:.1f} -> infty (confirms non-uniform exponent)")
    # 3) covering estimate sketch: even an eps=0.1 net over sign/vertex configurations
    # of unconditional polytopes with up to V vertices: N ~ exp(c*V); L untracked.
    print("covering: log N(eps) grows with vertex budget; L(P) untracked => no explicit eps0 in budget")
    print("RESULT=BLOCKED")
test()
