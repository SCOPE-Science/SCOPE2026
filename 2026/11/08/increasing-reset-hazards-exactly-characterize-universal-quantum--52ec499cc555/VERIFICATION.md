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

# Verification and reproducibility

Run `python3 verify.py` using Python 3 with the standard library only. The code computes exact finite renewal-age distributions for rational hazards, forms the coefficient vector of the proposed one-step intermediate map, and compares its action after the averaged channel with the next averaged channel on each matrix unit for a cyclic-shift unitary. It also checks normalization, coefficient signs for monotone hazard prefixes, and the negative qubit example.

Observed command result:

```text
PASS: 244 finite rational profiles, 17476 exact identities/checks
PASS: explicit qubit descent witness has negative output -3/8
LIMIT: finite checks do not establish the all-dimensional iff theorem
```

The general proof is in `RESULT.md`. All-dimensional sufficiency requires the coefficient-convexity argument, and necessity requires the explicit cyclic-shift witness and invertibility argument. Neither follows from finite tests alone. The code tests sample profiles rather than enumerating an infinite hazard space. No independent audit has been performed.
