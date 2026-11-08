---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible mathematical checks

From the directory containing the two standalone programs, execute `python3 verify_multinomial.py` and `python3 verify_extension.py`. Both use only the Python standard library. The first constructs polynomial coefficient formulas by multinomial combinatorics and compares the complete \(3\times3\) Cartier matrices. The second independently multiplies the defining polynomial \((p-1)/2\) times in polynomial rings over finite quadratic extensions, checks all matrix entries, computes ranks by explicit minors, and exhaustively checks every smooth coefficient in \(\mathbb F_{49}\) and \(\mathbb F_{121}\). The actual successful checks are `ALL_MULTINOMIAL_CHECKS_PASS`, `EXTENSION_ENUMERATION_PASS 7`, `EXTENSION_ENUMERATION_PASS 11`, and `ALL_EXTENSION_CHECKS_PASS`.

The ring computations are exact and deterministic. Since all roots of the factored Cartier entries lie in these quadratic extensions, the numerical checks exercise every exceptional geometric point, including the characteristic-eleven roots of \(c^2+1\). The **proof** that no other exceptions occur over the algebraic closure is the symbolic factorization of the explicitly extracted Cartier matrix; finite-field enumeration alone would not prove that assertion. The fact that Cartier rank equals geometric \(p\)-rank is separately proved by stability of the invertible semilinear subblocks. The elliptic/Prym decomposition uses a standard separable double-cover isogeny of degree prime to \(p\), rather than inferring Prym invariants merely from numerical counting.

Not checked here: complete Newton polygons, isomorphism class orbits, other characteristics, stack-theoretic Hasse multiplicities, or historical-priority certification. Independent mathematical audit was not performed.
