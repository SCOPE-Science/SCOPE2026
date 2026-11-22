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

The proof is fully analytic and works for the indicated continuum of positive parameters and all real vectors. It uses an exhaustive six-vertex / three-functional reduction, duality between the two-component Hilbert sum and its dual, and an explicit two-by-two eigenvalue computation. The norming pairs are given in the proof. At the degenerate-to-square boundary the separate upper and lower arguments coincide.

`CHECK.py` is a standalone standard-library Python diagnostic. Running `python CHECK.py` yielded `HEXAGON_DEFORMATION_NJ_DIAGNOSTIC_OK 5777`. The diagnostic enumerates each finite facet/vertex candidate at 170 parameters and also tests random vectors; none of those finite checks is claimed to verify the continuum proof. No external certification or independent audit has been performed.
