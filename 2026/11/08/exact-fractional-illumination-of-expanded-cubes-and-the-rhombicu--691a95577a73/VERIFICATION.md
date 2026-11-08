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

The proof gives the precise 26-facet halfspace presentation for each real \(a>1\), identifies all four active normals at every vertex, and reduces illumination to four strict integer-normal inequalities independent of \(a\). The seven-vertex upper bound is a direct case classification for generic directions; strictness extends it to nongeneric directions by perturbation. The orbit construction supplies an exact matching weighted covering. No numerical extrapolation is used as a continuum proof.

The included standalone `verify.py` was executed after embedding and extraction. It checks 24 vertices, 48 signed-permutation illuminating directions, 14 incidences at every vertex, all four proposed ordinary directions, and 288 exact generic-direction comparisons against the analytic formula. The result was `EXACT_OK`.

These computations are independent consistency tests of finite arithmetic. They do not independently certify the literature-priority assessment, the general analytic proof, or any external audit. The ordinary number for the regular member was previously bounded by four in the 2012 primary literature; originality here concerns the fractional value and the constant family profile.
