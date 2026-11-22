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

# Exact verification

Run `python3 verify_fixed_point_walsh.py` from the same directory as this note. No external modules are required. The program independently enumerates every permutation through order eight, constructs its entire exact fixed-position distribution, transforms it by the integer Walsh–Hadamard algorithm, and compares every frequency to the factorial expansion. It additionally checks the recurrence, all boundary cases, the exact exponential partial sum, strict positivity and sharp uniform conditioning through order 150. Any disagreement raises an assertion error. This is a reproducibility check, not an assertion that finite tests constitute an infinite proof. The proof in `RESULT.md` is the mathematical justification for all dimensions.
