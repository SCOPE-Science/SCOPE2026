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

Run the included `verify.py` with the Python standard library. The script enumerates all maps for each size from two through seven, reconstructs cycles directly, and compares rational conditional factorial moments, exact covariance by every cycle length, its sign split, and aggregate covariance sums. Total enumerated maps: 873611. It also displays finite-size approximations for the two limiting aggregate constants and checks convergence of the individual mesoscopic profile at three positive arguments.

The proof is contained in RESULT.md, with all assumptions and quantifiers. Exhaustive enumeration only covers the stated small finite sizes and does not, by itself, establish the infinite-domain signs or limits; those follow from product monotonicity, explicit asymptotics, and uniform Gaussian domination. The independent-audit channel is not performed; no external certification is claimed.
