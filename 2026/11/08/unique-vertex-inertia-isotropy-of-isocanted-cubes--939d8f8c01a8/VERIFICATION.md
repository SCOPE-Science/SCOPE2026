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

The theorem is proved symbolically from the explicit vertex set and two subset-inclusion probabilities. The all-dimensional proof is in `RESULT.md` and requires no computer algebra. Exact integer identities, the strictly positive derivative of the axial-to-transverse eigenvalue ratio, and the unique positive quadratic root establish the strict ranges and boundary conditions.

To reproduce the corroborative finite checks, run `python3 verify.py` with the standard Python library. It uses exact `fractions.Fraction` arithmetic for the defining inequalities, distinct vertex count, mean-zero condition, every diagonal and off-diagonal covariance entry, full two-eigenvalue spectrum, ratio, and distinct radial shells over dimensions \(2\) through \(8\) and five rational cant ratios. It checks six even-dimensional isotropic cants exactly and five odd-dimensional quadratic-irrational values at 70 decimal digits. The successful output is `ISOCANTED_VERTEX_INERTIA_CHECKS_PASSED exact_profiles= 35 vertices_processed= 5010 exact_even_isotropy= 6 odd_precision_checks= 5`.

The finite checks cannot establish the theorem for arbitrary dimensions or real parameters; their role is detecting algebraic and normalization mistakes. The result is not a claim about uniform interior volume, normalized individual vertex directions, or a spherical design. Literature priority remains provisional.
