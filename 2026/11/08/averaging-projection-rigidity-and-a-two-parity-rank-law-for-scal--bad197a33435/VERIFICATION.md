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

The executable `verify.py` implements finite-field linear algebra directly from the defining brackets, without using the proof's classification of projections. Run `python3 verify.py`. Successful exhaustive outputs: order 2 dimensions 2,3,4; order 3 dimensions 2,3; order 4 dimensions 2,3; final token `VERIFY_OK`. The code checks \(P^2=P\), both averaging identities, the endomorphism identity, and the complete rank histogram. In the order-four case, arithmetic is performed in \(\mathbb F_2[u]/(u^2+u+1)\). The infinite-family formula and asymptotic limit are verified by the mathematical proof, not by extrapolation from these cases. Independent audit is not performed.
