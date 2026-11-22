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

Execute `python3 check.py` using Python's standard library only. The recorded exact run produced `CHECK_OK 17261 exact assertions; n<= 1100`. It reconstructs the Schröder values from an integer recurrence; checks 1100 neighboring-gap valuations; verifies 101 finite hypergeometric identities by exact rational arithmetic; exercises 2-adic isometry on many odd inputs and shifts; and tests modular zero loci through modulus \(2^{11}\).

The infinite proof is in RESULT.md: uniform convergence, binomial difference valuations, the explicit cubic-index term, and evaluation at exact two-adic roots. No formal or independent certification is claimed. Source [2] gives the hypergeometric input identity; no unpublished computation is required as a premise.
