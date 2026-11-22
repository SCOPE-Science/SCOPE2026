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

# Reproducibility and scope

Run `python3 VERIFY.py` in the extracted directory. The script uses Python standard-library integer arithmetic and prints four independent small-alphabet word/dynamic-program checks followed by the exact 49-state symbolic check. All 49 vector polynomial identities and all numerator coefficients are asserted as coefficientwise integer equalities in a free indeterminate (alphabet size), not tested by finite interpolation alone.

The direct tests cover alphabet sizes 2, 4, 6 and 8, with exhaustive strings to lengths 16, 9, 7 and 5, respectively. Dynamic programming checks reach lengths 25, 25, 20 and 15. The four-letter primitive transfer graph has 256 vertices; both forward and reverse reachability visit all 256 and a self-loop is present.

The mathematical theorem is for exactly one intervening symbol, every even alphabet size, and every nonnegative length. It does not establish general longer-loop avoidance, full DNA secondary-structure avoidance, or physical stability. No independent audit is claimed.
