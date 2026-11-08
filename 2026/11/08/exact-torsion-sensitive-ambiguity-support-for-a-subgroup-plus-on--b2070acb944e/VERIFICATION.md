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

# Verification notes

The theorem is proved in `RESULT.md` using exact character orthogonality, coset intersections, evaluation-map fiber sizes, and a complete case split by quotient order. The correction for a merged cross-coset is a sum of exact rational integers \(N/o(x)\). No numerical extrapolation is required in the proof.

Run `python check_subgroup_spike.py` with Python 3 and SymPy. It tests 11 cyclic or product-group configurations and 7 Gaussian-integer impulse choices each, plus two algebraic binary examples and one primitive-eighth-root example, reducing ambiguity coefficients in exact cyclotomic rings. The actual output was `EXACT_CYCLOTOMIC_AMBIGUITY_CHECKS_PASS 80`. A separate symbolic test with square-root amplitudes on the four-element binary group verified the sharp lower-bound equality count of nine for both real and imaginary impulses; these two symbolic tests are included in the reproducible checker and do not replace the general proof.

Scientific limits: the finite tests check only the listed small groups and Gaussian-integer amplitudes; in particular they do not enumerate arbitrary root-of-unity phases or all finite abelian groups. The full proof is analytical. Literature comparison remains provisional and independent mathematical audit has not been performed.
