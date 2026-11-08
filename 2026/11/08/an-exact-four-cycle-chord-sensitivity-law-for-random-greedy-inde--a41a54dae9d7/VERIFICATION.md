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

# Reproducibility checks

Run `python3 verify.py` in the directory containing this file and the script. It needs only a Python standard library with `fractions`, `functools`, `itertools`, and `math`.

The script checks 516 exact assertions. These include an independent induced-subgraph first-arrival implementation for finite graphs through order 13, direct enumeration of each permutation through order 8, path recurrences and explicit coefficient formulas through order 149, and the alternating increment identity. All equality checks use rational arithmetic. The analytic derivation in `RESULT.md` establishes the theorem for unrestricted order; enumerations are not treated as an infinite proof.

No independent mathematical validation or separate expert certification has been performed. Historical priority remains subject to further independent review.
