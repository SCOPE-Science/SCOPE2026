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

# Verification of the sharp planar width cutoff

The proof of the universal result is in `RESULT.md`. Its essential imported ingredient is the published equality case of the one-interior-point planar flatness theorem. All other steps reduce to Pick's formula, an exact discriminant case split, and a complete classification of twelve small primitive triangles with normalized determinant at most nine.

Run `python3 verify_width.py`. The standalone script checks the twelve admissible normal-form representatives, candidate primitive functionals, their minimal widths in a finite direction box, first seven integer dilation counts, the congruence exclusion for the exceptional determinant-seven triangle, and its unimodular equivalence. Observed result: `PASS 151 finite exact arithmetic checks`.

Finite tests are corroboration only. The absence of a shorter integer functional for the exceptional triangle is analytically proved by bounding its first dual coordinate and checking residues modulo seven. The theorem across all polygons is independently quantified through a case split and the cited planar flatness theorem; no finite search asserts an infinite impossibility.

Self-review passed on correctness, historical originality with residual priority risks, and mathematical value. Independent audit has not been performed.
