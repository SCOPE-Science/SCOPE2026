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

# Exact finite-state certificate

Run `python3 verify_cycles.py` with the ordinary Python 3 standard library. This constructs the complete 6401-state graphs in integer coordinates with independent exact rational successor checks and two distinct functional-graph census algorithms. The script asserts all cycle/basin pairs, maximum transient depths, and the 5122-edge difference before reporting PASS. There is no floating-point computation, stochastic input, hardware validation, or generalization to other state resolutions.
