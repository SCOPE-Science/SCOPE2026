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

# Verification scope

The packaged `check_collision.py` verifies the exact covariance by two independent finite computations: conditioning and complete enumeration of labeled allocation words, both using rational arithmetic. It then checks the quadratic sign spectrum, singleton factorization, exact zero discriminant, sample-size reentrance and selected integer double-zero families. Invocation: `python3 check_collision.py`. The checker reports 174,349 exact arithmetic assertions passed in the checked environment.

The all-parameter correctness claim is mathematical, not computational: the proof in `RESULT.md` derives the conditional collision law, exact quadratic, both discriminants, conservation-based existence of negative frequencies and the arithmetic infinite family. A finite testing grid is not proof for unbounded parameters. No independent external audit has been performed.
