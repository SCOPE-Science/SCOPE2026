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

# Exact verification and scope

Run `python3 check_derangement_first_zero.py` beside the six reports. This is standard-library-only code using two exact arithmetic routes: a subset-DP signed hollow permanent and a direct sum over enumerated derangements. Exhaustive off-diagonal sign supports were checked up to weight one at size three, weight three at size four, weight four at size five, and weight three at sizes six and seven. The independent computations agree and verify the sharp lower envelope and equality geometry. A separate loop checks the parity and every row-star identity through size sixteen.

Expected output concludes: `DERANGEMENT_SPARSE_WALSH_PASS; exact assertions/groups: 23518`. These calculations confirm finite instances, not the infinite theorem; its proof uses the stated uniform matching marginal, the integer sign bound, Hall extendibility, and derangement parity. The exact first-weight counts and the classification at the stated odd sizes follow from those arguments, not from sampling. No external independent mathematical validation has been performed.
