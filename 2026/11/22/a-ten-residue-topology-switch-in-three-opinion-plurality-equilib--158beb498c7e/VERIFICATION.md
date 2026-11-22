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

# Reproducibility checks

Execute `python3 verify.py` in a Python 3 environment with SymPy installed. `verification_output.txt` records a successful complete execution.

The verification reconstructs the full 81-state stationary transfer from the local rule and the 36- and 45-dimensional symmetry sectors directly. Their symbolic integer characteristic polynomials are checked against explicit factorizations. Newton sums reproduce the seam difference through 18 rungs without using a fitted recurrence. A completely separate microscopic graph implementation enumerates all initial configurations for prism and Möbius lengths 3 through 6, and agrees with the transfer counts. The strict all-length sign proof is an exact finite-recurrence check for lengths 3 through 15 followed by an analytic root bound beginning at length 16; this is not an inference from finite experiments.

The result concerns fixed configurations and does not claim classification of transients, longer recurrent periods, or attraction basins. The exact symbolic check depends on SymPy's polynomial routines; the direct graph enumeration is standard-library Python. Independent external validation remains unperformed.
