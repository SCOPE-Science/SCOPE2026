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

# Verification of the local-branch theorem

Run `python3 verify.py` from this directory. The standard-library script enumerates all \(16\) base-sign configurations for exact second, fourth, and sixth moments of the two explicit coefficient arrays. It separately checks the parity-block fourth-moment identity for \(44\) rational six-coefficient examples, and computes numerical approximations to the two unique roots and the relevant Hessian signs for sample exponents.

Recorded output from the current package:

```
EXACT_16_SIGN_MOMENTS_AND_PARITY_BLOCKS_OK 44
LOCAL_AND_CROSSING_ROOTS_OK 2.341822454747 2.736277322007
ALL_TWO_LOCAL_BRANCH_CHECKS_OK
```

These are finite corroborating computations. The arbitrary-real-exponent theorem uses the explicit local Taylor expansions, strict convexity of the root-defining functions, and the dimension-splitting argument in `RESULT.md`. The numerical root values are approximate; the root uniqueness, separation, and strict-sign conclusions are established analytically. No exhaustive stationary-point classification, global sharp norm, or independent audit is claimed.
