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

Run `python3 verify.py`. The standard-library script traces every cycle of every labelled permutation for orders 1 through 8, constructs the even-cycle vertex-set count array without using the closed formula, and applies a fresh exact Walsh butterfly. It then checks every spectrum entry and positivity, extrema and nullity. Exact closed-form, symmetry, central-minimum and ratio-sign checks cover all orders 1 through 200. Observed output: `PASS: 47911 exact checks; n=1..8 independent permutation enumeration, n=1..200 symbolic-spectrum integers`.

The infinite statement is proved algebraically in `RESULT.md`, not inferred from finite computation. External independent audit: not performed.
