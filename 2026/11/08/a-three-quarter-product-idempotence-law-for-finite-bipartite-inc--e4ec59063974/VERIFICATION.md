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

The accompanying `verify.py` independently constructs actual finite incidence-algebra matrices, checks literal idempotence by matrix multiplication, and counts ordered pairs meeting the one-order and two-order product conditions. It compares these with both independently enumerated four-state tables and the exact multinomial sums. Seven small cases include fields of orders two and three and bipartite sizes through \((a,b)=(2,3)\). All tested cases pass and the command `python verify.py` terminates with `VERIFY_OK`.

The verifier also computes the exact rational probabilities in several larger balanced instances. These finite computations corroborate but do not prove the formula for all fields or the limiting laws. The unrestricted proof is provided in `RESULT.md`; an independent audit has not been performed.
