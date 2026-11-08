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

# Exact checks and limitations

`check_exact.py` computes the unique backward-coordinate preimage directly from rational weights, then compares its squared norm with identity (1) using independent closed product formulas. It checks three rational parameters, 11 support endpoints and 13 iterate orders, a total of 429 exact identities. The source code was executed on extraction from the delivered package and reported `MBEKHTA_CORE_EXACT_FINITE_OK 429`. The proof of all-index and infinite-dimensional claims is mathematical, not experimental. No external or independent audit has been performed.
