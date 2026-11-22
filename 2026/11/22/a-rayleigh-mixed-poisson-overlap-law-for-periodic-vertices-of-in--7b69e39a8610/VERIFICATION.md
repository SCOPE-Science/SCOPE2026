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

The finite checker uses exact integers and rational arithmetic for all maps on one through five vertices. Run `python checker.py` and verify the `EXACT_ASSERTIONS 102` line. For larger sizes the checker evaluates the exact single-pair hypergeometric mixture numerically; those values are illustrative and not proof of convergence. The general limiting theorem is justified by cyclic-set enumeration, deterministic-size mixed factorial moments and a tight random-size mixing argument in RESULT.md. The symbolic integral for the zero-count limit was separately evaluated exactly as \(1/3\).
