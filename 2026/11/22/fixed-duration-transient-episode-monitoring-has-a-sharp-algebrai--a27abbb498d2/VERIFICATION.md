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

The complete analytical derivation appears in `RESULT.md`. Run `python3 verify_transient_windows.py` to check the reproduced scalar Bellman iteration, numerical first-detection decomposition, randomly generated schedules, independently evaluated one-window arrival integral, and limiting behaviors using only the Python 3 standard library. In the prepared package, the script reported `PASS 16596 checks` and printed the four-window example at unit exponential rate and half-unit window duration.

The numerical checker is a supplementary finite diagnostic and is **not** a proof for all window counts or all real parameters. Global uniqueness, strict positivity and ordering of gaps, the infinite product, and the two error-rate regimes are proven analytically. No actual molecular-capture experiment, instrument calibration or independent external check was performed.
