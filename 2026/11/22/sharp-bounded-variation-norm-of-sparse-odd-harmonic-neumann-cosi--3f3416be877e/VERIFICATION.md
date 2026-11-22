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

# Reproduction and limits

Execute `python3 CHECK.py` in a directory containing this file and the script. The script uses no packages outside the Python standard library. It independently checks the exact radical identity, the positive rational boundary certificates, 10,001 samples of the reduced kernel, 54 predicted one-jump equality locations, 600 noncentral jump tests and 450 finite multijump inequalities. The one-parameter and distributional-measure arguments in RESULT.md are the continuum proof; numeric samples cannot replace them. The script uses approximate quadrature only as a diagnostic with documented tolerances.

This package has undergone self-review. Independent mathematical audit and independent validation have not been performed.
