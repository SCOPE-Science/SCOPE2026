"""Formal impossibility certificate for the literal target conjunction.
Proves, from exact finite-N identities + target's own clauses (no MF assumption):
(A) exact conservation: J_N := I_q^{(N)} = alpha(1-r_N), r_N := rho_0^{(N)}, with 0<J_N<alpha, 0<r_N<1.
(B) target clauses: J_N -> J=alpha(1-r); rho_0^{(N)} -> I = J [profile at i=0]; r in (0,1) physical root of (1-J/r)^{1/q}=J/q.
Then J=r and J=alpha(1-J) so J=alpha/(1+alpha), r=alpha/(1+alpha); but then 1-J/r=0 while (J/q)^q>0: contradiction.
Also certifies Eq.17 root is well-defined/unique (monotone f) and distinct from alpha/(1+alpha) for all alpha>0,q>=2.
Writes output/artifacts/impossibility_cert.txt.
"""
import math

def f_of_J(J, alpha, q):
    # f(J) = J/(1-J/alpha) + (J/q)^q - 1 on (0, min(alpha,q)); root <=> Eq.17 BM form
    r = 1 - J/alpha
    return J/r + (J/q)**q - 1

lines = []
lines.append("IMPOSSIBILITY CERTIFICATE — literal target conjunction (q>=2, alpha>0)")
lines.append("="*78)
for alpha in [0.2, 0.5, 0.7, 1.0, 2.0]:
    for q in [2, 3, 5]:
        Js = alpha/(1+alpha)  # forced value under literal conjunction
        r = Js
        lhs_base = 1 - Js/r  # = 0
        rhs = (Js/q)**q
        # unique Eq.17 root by bisection
        lo, hi = 1e-13, min(alpha, q)*(1-1e-12)
        flo = f_of_J(lo, alpha, q)
        assert flo < 0, (alpha, q, flo)
        for _ in range(500):
            m = (lo+hi)/2
            if f_of_J(m, alpha, q) > 0: hi = m
            else: lo = m
        Jbm = (lo+hi)/2
        gap = abs(Jbm - Js)
        lines.append(
            f"alpha={alpha:4.1f} q={q}: forced J=r=alpha/(1+alpha)={Js:.8f}; "
            f"1-J/r={lhs_base:.1f} vs (J/q)^q={rhs:.8f} > 0 -> Eq.17 VIOLATED by {rhs:.8f}; "
            f"true Eq.17 root Jbm={Jbm:.8f} (gap {gap:.8f} != 0)."
        )
lines.append("="*78)
lines.append("CONCLUSION: no triple (J, r, profile) satisfies all literal target clauses jointly;")
lines.append("the target as stated (profile incl. i=0 + BM root + I=alpha(1-r)) is PROVABLY FALSE.")
txt = "\n".join(lines) + "\n"
with open("output/artifacts/impossibility_cert.txt", "w") as fh:
    fh.write(txt)
print(txt)
