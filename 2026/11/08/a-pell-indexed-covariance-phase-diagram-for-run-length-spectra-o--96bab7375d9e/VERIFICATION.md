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

The attached `verify.py` uses Python's standard library and exact rational arithmetic. Executing `python3 verify.py` produced `2440 exact checks passed`. Exhaustive enumeration covered every fixed-weight word in the designated small ranges, rather than selected random samples. A separate collection of exact rational tests compared the exceptional rational identity for \((1,8)\) at all multiples of three from \(15\) through \(180\). Further tests checked integer discriminant conditions and the first six Pell-generated equality pairs.

The infinite covariance-density formula, the full sign phase, and the square-root critical-window limit are proved algebraically in RESULT.md. Finite checks alone do not prove these infinite statements. The earlier general conditional generating-function work is a substantive priority risk for any specialized moment result. No external review, independent audit, or growing-run-length theorem was performed.
