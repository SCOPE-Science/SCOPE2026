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

# Verification details

The all-length proof is the closed-walk bijection and exact cyclic-component trace identity in `RESULT.md`. `verify_life_cylinder.py` is a standalone standard-library implementation of the two transfer digraphs, an exact SCC decomposition, Newton-identity characteristic-polynomial checks, the integer Perron inequalities, and small-size traces. The strict inequalities are exact integer statements, not floating-point guesses or numerical experiments. This yields a proof for every integer circumference \(n\ge3\).

`crosscheck_life_cylinder.py` implements an independently written direct Moore-neighborhood evolution and exhausts all \(299520\) configurations on the four sizes \(n=3,4,5,6\). This is a finite cross-check, not the basis of the all-length theorem. Captured stdout from both code paths is included as `transfer_check.txt` and `direct_check.txt`. Execute each script with Python 3 and compare its stdout with its text artifact.

Open issues: No analysis of return times three or more, transients, or infinite-plane objects. Published historical-priority comparison remains qualified by unavailable full chapters. No independent audit has been performed.
