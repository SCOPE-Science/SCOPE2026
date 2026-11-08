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

# Verification of the q-Berezin power law

The exact power normalization follows from basis images \(S_\beta^m z^j=\beta^{mj+m(m-1)/2}z^{j+m}\). The normalized Szegő kernel pairing is computed directly in RESULT.md. Symbolic algebra checks the derivative quartic, its endpoint signs, the special values at the overlap branch threshold and at the origin transition, and the nonnegative third derivative. Convexity of the quartic's derivative proves uniqueness analytically, not numerically. A separate logarithmic stationary-point argument proves the universal large-power limit for each fixed \(q>0\).

The independent-of-source diagnostic command is `python checks/checker.py` (Python, NumPy, SciPy). During preparation it returned `Finite diagnostic assertions passed: 8493`. Its tests include 1,188 parameter sets for the exact maximizing quartic and kernel formula, finite global-magnitude comparisons, phase-sign checks, and a sweep of damping parameters and powers for the asymptotic law.

These finite tests are not proofs of the infinite-dimensional theorem. Literature comparison is qualified and does not certify publication priority. The fixed-parameter asymptotic is not uniform near the singular limit \(q\downarrow0\). The first-power special case is prior-covered. Independent audit: not performed.
