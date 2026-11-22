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

# Computational verification

Run `python verify.py` with Python 3 and the standard library. The checks produce:

`VERIFY_OK constructions=70 small_order_checks=12715 random_saturation_cases=74`

The constructor tests every successor-subsignature in one, two and three orders for parameter counts zero through four. The independent direct type calculator enumerates all order permutations in the prescribed small configurations and checks each sharp universal upper bound. Finally, explicit enumeration of chosen marked positions checks the exact binomial saturation count in 74 finite cases. These finite tests do not establish arbitrary-size correctness or the probabilistic limit; proofs are in `RESULT.md`. No independent validation has been performed.
