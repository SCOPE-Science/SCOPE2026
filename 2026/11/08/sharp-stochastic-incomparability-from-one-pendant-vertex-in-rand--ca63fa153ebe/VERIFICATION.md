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

# Reproducibility

Execute `python3 verify.py` with Python 3.10 or later, using only its standard library. The checker recomputes exact rational random-order greedy independent-set distributions by first-vertex recursion and tests every connected graph on at most three vertices, every attachment root and every threshold; it then evaluates the claimed formulas for stars with three through eight leaves. A replay returned `VERIFY_OK 179 exact assertions`.

These finite computations support but cannot establish all \(m\ge3\); the symbolic first-arrival proof in RESULT.md supplies the unbounded argument. No independent audit has been performed.
