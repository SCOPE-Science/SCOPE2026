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

# Verification record

The theorem's proof is mathematical: (1) kink-hyperplane rigidity fixes weighted linear forms, (2) graphic-incidence triangles characterize possible permutations, (3) coefficient ratios exclude all boundary swaps away from balanced penalties, (4) explicit endpoint flips attain each possible balanced symmetry, and (5) dimensions one and two are treated separately. Each step applies to arbitrary positive real coefficients.

The included standalone `check_discrete_sobolev_isometries.py` enumerates possible exact signed images of the coordinate weighted forms, checks images of every difference form, and requires the whole weighted-form set to be permuted. The exact checker passed all 13 cases for dimensions 1–5 and selected integer ratios. These finite checks cannot establish the all-dimension proof by themselves.

The continuous Sobolev isometry literature and general zonotope generator-symmetry literature were compared with the exact new statement. The direct global bibliographic uniqueness of this finite path specialisation remains uncertain. Self-review only; no independent audit has been performed.
