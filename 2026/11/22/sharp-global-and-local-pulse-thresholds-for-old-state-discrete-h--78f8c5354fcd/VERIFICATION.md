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

The proof in `RESULT.md` is the claim-bearing evidence. Run `python VERIFY.py` from the extracted directory with Python 3; this uses only standard-library exact rational arithmetic. An execution on the embedded script printed:

```text
VERIFY_OK 14155 rational checks, 3256 strict-split cases
```

The checker enumerates rational positive budgets on small finite horizons, confirms the strict lower comparison with the pulse objective, verifies the exact two-control exchange identity and tests descent above the sharp threshold. These computations are **not** a proof of arbitrary horizon, real parameters, strict local optimality in every feasible direction, or historical originality. Those require the symbolic inequalities and uniform perturbation argument in the accompanying proof. The comparison with prior literature is limited by accessible source material. Independent audit: not performed.
