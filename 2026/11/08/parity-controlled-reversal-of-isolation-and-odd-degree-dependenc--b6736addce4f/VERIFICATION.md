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

# Reproducibility and limits

Run `python3 verify.py` in the directory containing this file. The checker constructs all labeled graphs for \(2\le n\le6\) and independently accumulates the joint moments of isolated-vertex and odd-degree-vertex counts by graph edge number, then compares the resulting exact rational covariance against the displayed formula at five rational probabilities per order. It reports 25 exact rational tests and 16 additional numerical asymptotic-window checks. The theorem's proof is contained in `RESULT.md`, including the strict sign and uniqueness arguments for all orders; the finite checker is not a proof of universal statements. Independent audit and external validation have not been performed.
