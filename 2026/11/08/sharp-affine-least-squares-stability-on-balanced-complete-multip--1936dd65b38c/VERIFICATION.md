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

The analytical proof uses exact nodal Gram integration, a three-eigenspace inversion, and exact signed affine-kernel integrals. The positive kernel sign intervals and the strict interior gap are established analytically for all integers in the stated range.

The accompanying `verify_turan_projector.py` uses standard-library exact rational arithmetic. It directly inverts ten finite Gram matrices and checks 526 individual graph edges, full endpoint row norms and interior rows. It also checks 4,136 finite pairs for the threshold, monotonicity and sharp-envelope identities. Successful output:

```
EXACT_DENSE_MASS_INVERSES_AND_KERNEL_INTEGRALS_OK 10 526
EXACT_THRESHOLD_MONOTONICITY_AND_ENVELOPE_OK 4136
ALL_BALANCED_MULTIPARTITE_P1_CHECKS_OK
```

These finite computations corroborate the proof but do not establish universal quantifiers. The exact formula and its global consequences are derived analytically in the proof using symbolic algebra valid for every integer \(r\ge3\), \(s\ge2\). The verification status above concerns only the stated checks; no external or independent scientific audit was performed.
