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

# Verification and reproducibility

Run `python verification_check.py` from the extracted package using Python 3 and its standard library. The expected terminal marker is `ARBELOS_CHORD_CHECKS_OK` after finite-deficit numerical comparisons and quadrature identities. The coefficient is computed in two independent ways: the closed arctangent expression and composite Simpson integration of the unevaluated rational integral. Symmetry, the equal-radii special value, and the thin-radii asymptotic are also sampled.

The finite-epsilon test uses a deterministic four-dimensional Halton quadrature for the *actual curved-circle* domain, not the limiting polynomial domain, and compares decreasing epsilon to the predicted limit. A numerical test cannot replace the compactness and dominated-convergence arguments in `RESULT.md`; it only detects arithmetic or normalization mistakes. A fully independent audit has not occurred.
