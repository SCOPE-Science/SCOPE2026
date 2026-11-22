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

Run `python3 verify.py` with standard Python 3 and SymPy. The script reconstructs all vertex pairs independently from the triangular cutoff coordinates, separates inclusion-comparable and incomparable pairs, and compares the entire histogram against the theorem for dimensions 2 through 18. It checks the exact number of incomparable pairs and all beta-binomial conditional means and variances by exact arithmetic, verifies near-diameter coefficients, and symbolically integrates the claimed limit densities.

Expected terminal line: `LADDER_CHORD_JOINT_SPECTRUM_PASS`.

These finite tests are not an infinite certificate. The all-dimension proof is the stars-and-bars displacement enumeration plus the beta-binomial algebra and Riemann-sum limit. No independent mathematical audit has been performed.
