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

# Reproducible scientific checks

Run `python check.py` with SymPy. The checker differentiates the exact return and verifies the triple cusp conditions for exponent depths 2, 4, 8 and 16, confirms the explicit rational cusp at exponent 4, and checks the three roots and stability of the given exact parameter witness. It reports `MULTISEASON_STOCHASTIC_CUSP_OK symbolic_depths=4 exact_witness_roots=3` on success.

The proof of the statement for every integer season depth is the analytic derivative sign argument in RESULT.md; the finite symbolic computations corroborate but do not establish its quantifiers. The global basin argument uses monotonicity, not sampled trajectories. The Gaussian limit uses uniform derivative estimates. No independent scientific audit, bibliographic uniqueness certification or empirical population validation is claimed.
