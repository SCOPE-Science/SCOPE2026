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

# Reproducibility and verification

The analytic proof is in `RESULT.md`. For each integer \(n\ge3\), it checks the correct facet enumeration, scales, twist endpoints and all real positive height parameters. In particular, the optimized quotient has the strict derivative sign \(9ac-t_*(t_*+4c)<0\), and equality requires the half-step twist and the unique height optimum.

A standalone independent implementation, `verify_antiprism_isoperimetry.py`, uses SciPy's three-dimensional convex hull to compute volumes and areas directly from the source vertices for \(3\le n\le18\) and multiple twists/heights. It additionally tests the analytic extremal formulas through \(n=100\). Execute `python verify_antiprism_isoperimetry.py` in a directory with Python 3, NumPy and SciPy. In the recorded run it returned `TWISTED_PRISMATOID_ISOPERIMETRY_OK 5582`. The checks are finite numerical corroboration; they do not replace the written proof for all integers and all real parameters. No external independent audit was performed.
