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

# Verification methods and limits

The standalone `check.py` operates solely on exact integers. It enumerates all 32 survival configurations for the five removable species, constructs directed reachability from the source root, and separately evaluates Boolean path formulas. It reports the complete six-row cardinality table, all of whose covariance numerators match the theorem.

It then enumerates all \(65{,}536\) possible truth tables of four-variable Boolean functions. Each is included precisely when it respects the 32 one-coordinate monotonicity relations. Exactly 168 are included, matching an independent antichain enumeration of the same 168 truth tables. For every one of the \(168^2=28{,}224\) ordered pairs, the code computes the three interior fixed-cardinality covariance numerators with exact integer arithmetic; none has two strict sign reversals. The complete search was successfully replayed from the generated package.

This is finite exhaustive verification, not a universal numerical extrapolation. No human or independent external audit has been performed. The proof is limited to the specified model and excludes empirical claims.
