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

# Verification

The complete proof is in RESULT.md. The standalone `check_hesse_weighted.py` requires only Python 3 standard-library modules (`fractions`) and operates in the exact ring \(\mathbb Z[\omega]/(\omega^2+\omega+1)\). Running `python3 check_hesse_weighted.py` passed all assertions on original/dual-line incidence, all twenty-one distinct projective points, every original-line pairwise intersection, the rational vertices of the Bézout feasible polytope, and the proposed volume bound.

The key proof inequalities are \(12d\ge4A+2B\) and \(9d\ge3B\) for an irreducible curve not equal to any of the twenty-one named lines. Combining these inequalities for every positive real weight pair proves the universal formula; a finite check cannot substitute for this derivation. On the exact chamber wall, the primitive nef class has square zero by direct intersection arithmetic.

The verification does not certify novelty, all wall minimizers, effectivity or semiampleness, or geometric claims beyond the stated domain. Independent mathematical audit has not been performed.
