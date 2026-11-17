---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For N=30·2^h with h≥0, the exact degree-eight Phi_30 remainder certificate has weights 0 at 0..4 and 15..19 and strictly positive at all positions 5..14. Consequently a nonnegative degree<20 multiple has no coefficients in the central window, and X^15≡−1 (mod Phi_30) forces equality of both degree≤4 outer blocks. Residue-class decomposition modulo 2^h and Phi_(30·2^h)(X)=Phi_30(X^(2^h)) lift the cone identity to all h; monomial removal gives uniqueness. The 1+X^(10t)+X^(20t) witness first breaks antipodal rigidity at diameter 20t. Disjoint antipodal blocks yield the binary counts 1 and 2^(k−1). Independently recomputed Phi_30 and all 20 certificate values and identities for t=1,2,4,8 by exact SymPy arithmetic. Finite certificates support but do not replace the all-h algebra.

## originality

PASS

PASS for the exact REAL nonnegative cone and sharp subcritical diameter interval for all dyadic 30t, not for known minimal diameter 15t or for the known 20t nonpolygonal minimal zero-one witness. Tan–Zhang Theorem 1.1 and Section 5 establish the lower bound/equality and concentration estimate but do not imply zero weight at ten exact forbidden exponents for the entire interval. Earlier checkerboard classification bounds circular diameter of nonpolygonal minimal zero-one sums at N=30 to 20, but minimality/integrality does not control arbitrary nonminimal real positive coefficient combinations. Some further stronger cone theorem may exist.

## value

PASS

A natural quantitative continuation of the cyclotomic minimal-diameter problem: this gives a full positive cone rigidity threshold with exact coefficient parameterization and binary enumerator, rather than one extremal polynomial or a low-weight example. Three-prime-factor moduli make usual two-prime cone decompositions inapplicable; dyadic lifting supplies a meaningful infinite tower.

The dated certificate retains the supplied scientific assessment, sources and limitations.
