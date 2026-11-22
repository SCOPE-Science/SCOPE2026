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

The standalone Python 3 standard-library checker `verify.py` compares complete ternary-block valuation distributions through depth nine against independent direct digit carry counts and exact polynomial recurrences, direct binomial integers at small indices, Legendre factorial valuations at large indices, exact first and second moments, and the top-coefficient cubic recurrence. Running the checker from this directory returned `VERIFY_OK checks=29824 depths=0..9 max_depth=9`.

These finite checks do not themselves prove the unrestricted statement. The proof in RESULT.md derives the complete six-state transition and its exact rational inverse; the extremal recurrence comes from an independent three-state digit constraint; the Gaussian limit uses a simple Perron eigenvalue and analytic perturbation. The scientific conclusion is a self-review only. No independent audit has been performed.
