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
Run `python3 verify.py` to check the theorem against independent adjacency evaluation and to build the all-size arithmetic-progression witnesses up to \(m=40\). The script performs 1,066,494 bounded-grid marked-subset checks on every nondecreasing center tuple of at most seven vertices in a nine-site quarter-unit grid. For each parameter size, the rational witness produces the claimed open and closed trace counts. The all-size statement is proven by the endpoint-sweep and self-deletion argument in `RESULT.md`, not by finite search.

# Limits
The numerical checker is deliberately finite, with no claim of infinite exhaustive coverage or independent validation. No separate external expert audit has occurred.
