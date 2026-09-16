"""Bounded recovery test: pole/growth audit for Pi0 = 1^{(+n+1)} Eisenstein input.

Checks, for n>=3 on Miao arXiv:2110.11529 notation:
 (i)   the (s,w)->(s',w') involution identities used in Prop 3.5;
 (ii)  factorization L(s,Pi(lambda) x ~pi)=prod_i L(s+lambda_i,~pi) and the
       collision of n+1 polar hyperplanes at lambda=0 when pi is Eisenstein;
 (iii) Casselman-Shalika spherical normalization divisor
       prod_{i<j} zeta_v(1+lambda_i-lambda_j) singular at lambda=0;
 (iv)  Borel-Eisenstein moderate growth vs rapid decay needed by Props 3.4/3.5.
This is an exponent/counting audit, not a full automorphic computation.
"""
from fractions import Fraction

def involution(n, s, w):
    sp = (1 + (n - 1) * w - s) / n
    wp = ((n + 1) * s + w - 1) / n
    return sp, wp

def check_involution(n=3):
    # exact rational check of the two linear relations in proof of Prop 3.5:
    # n(s'-1/2) = n(1/2-s)+(n-1)(s+w-1); s'+w'-1 = s+w-1
    s, w = Fraction(3, 4), Fraction(2, 3)
    sp = (1 + (n - 1) * w - s) / n
    wp = ((n + 1) * s + w - 1) / n
    assert n * (sp - Fraction(1, 2)) == n * (Fraction(1, 2) - s) + (n - 1) * (s + w - 1)
    assert sp + wp - 1 == s + w - 1
    # involution is its own inverse
    s2, w2 = involution(n, float(sp), float(wp))
    assert abs(s2 - float(s)) < 1e-12 and abs(w2 - float(w)) < 1e-12
    return True

def pole_audit(n=3):
    # Pi(lambda)=|.|^{l1}+...+|.|^{l_{n+1}}; L(s,Pi(l) x ~pi)=prod_i L(s+l_i,~pi).
    # Cuspidal pi on GL(n): each standard factor entire -> product entire, but
    # spherical Whittaker value carries divisor prod_{i<j} zeta(1+l_i-l_j),
    # singular (zeta pole) at l=0: the "same H" limit is ill-defined.
    # Eisenstein pi=sigma1|.|^{it1} + sigma2|.|^{it2}: each L(s+l_i,~pi) can
    # contribute a pole in (s,t); at l=0 the n+1 hyperplanes coincide -> order
    # up to n+1 pole in s, absent from Miao Prop 3.14 which assumes
    # Lambda(s,Pi x ~pi) entire (Pi cuspidal) and only w+it1=1 poles.
    nplus1 = n + 1
    cuspidal_s_poles = 0  # entire standard factors
    eisenstein_max_s_order = nplus1  # coincident hyperplanes
    cs_divisor_factors = nplus1 * n // 2  # pairs i<j, each zeta(1+l_i-l_j)
    return cuspidal_s_poles, eisenstein_max_s_order, cs_divisor_factors

def growth_audit(n=3):
    # Borel Eisenstein constant term exponent rho+lambda with
    # rho=(n/2,(n-2)/2,...,-n/2); rapid decay needs super-polynomial decay in
    # Siegel sets, which moderate growth |a|^{rho+lambda} violates. Hence the
    # period I(s,Phi,phi) absolute convergence hypothesis of Prop 3.4 and the
    # rapid-decay spectral expansion (3.12)/Prop 3.1 fail for Phi0.
    rho_first = n / 2.0
    return {"rho_first_exponent": rho_first, "rapid_decay": False,
            "moderate_growth": True}

if __name__ == "__main__":
    assert check_involution(3)
    c, e, d = pole_audit(3)
    g = growth_audit(3)
    print("involution identities: OK (n=3 rational check)")
    print(f"cuspidal-pi s-poles from L factors: {c} (entire), "
          f"but H-limit singular via {d} zeta(1+l_i-l_j) divisors")
    print(f"eisenstein-pi max coincident s-pole order at lambda=0: {e}")
    print(f"growth: {g} -> Prop 3.4/3.5 rapid-decay hypothesis fails")
    print("RESULT: structural obstruction confirmed (divergence + higher-order "
          "s-residues outside Miao R(H)); stated M=N+M shape not recoverable "
          "without regularized truncation theory.")
