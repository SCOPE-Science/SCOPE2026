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

# Reproduction

Run `python3 verify.py` from the extracted files. The checker uses only Python's standard library. It tests joint stationary finite-window probabilities for multiple rational decay parameters, exhaustive finite-start parent-choice enumerations, product asymptotics, and finite anti-clustering bounds. Read the analytical proof in RESULT.md for the infinite-process argument; no finite checker proves weak convergence or historical priority.
