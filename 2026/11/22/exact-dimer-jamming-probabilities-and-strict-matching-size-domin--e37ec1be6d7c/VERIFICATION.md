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

Execute `python3 verify_dodeca.py` from the directory containing the standalone verifier, with Python 3.10 or later. No third-party modules, data downloads, or floating-point estimates are used. The graph is the stated generalized Petersen graph, generated from modular edge rules, not an external graph library.

The verifier calculates the exact rational terminal distribution by (i) the recurrence on free-vertex masks and (ii) distinct maximal-matching enumeration plus an ordered-arrival prefix probability recurrence. It then checks equality of all five distribution entries, probability normalization, maximal-matching counts by size, and the strict four-threshold stochastic-dominance test. It checks the exact greedy and uniform expectations and perfect-coverage likelihood ratio by reporting them. For the specified graph, both state spaces are exhausted; no extrapolation beyond that finite input is implied.

Limits: source-date and publication-priority judgments are bibliographic, not certified by the executable. No independent scientific audit or physical experiment is claimed.
