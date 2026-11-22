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

The result relies on explicit, analytic support maximization over the two circle arcs and common intersection points, monotonicity of the three nonconstant width branches, the uniform-orientation arcsine transform, endpoint expansions, and the exact intersecting-circle chord-height identity. All parameter ranges and zero-length branches are specified in `RESULT.md`.

The standalone script `check_lens.py`, executed in the delivered package's own directory with `python check_lens.py`, returned `PASS 2434 deterministic analytic/inverse/independent boundary diagnostics`. It constructs comparison support maxima directly by sampling admissible points on both circular arcs rather than merely replaying the symbolic formula. It also verifies CDF branch inversions and recovery for representative equal-radius, critical, opposite-side and same-side-center cases. Additional evaluations at near-maximum deficits of \(10^{-4}\) and \(10^{-6}\) agreed with each of the three analytic coefficients. These finite checks cannot certify all directions or the theorem's priority; those are addressed by the analytic proof and the separate literature comparison.

The first-appearance date of the motivating proper-lens chord source was verified as 2011-10-17; this is source chronology, not a claim of the theorem's publication date. The comparison is same-model only, not independent certification. Historical-priority uncertainty and exclusion of tangent/contained cases remain.
