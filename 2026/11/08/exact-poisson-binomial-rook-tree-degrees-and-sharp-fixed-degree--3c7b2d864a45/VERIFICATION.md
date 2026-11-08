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

# Verification of the claimed formulas

The proof in `RESULT.md` is analytic and applies to every pair of integers \(m,n\ge2\). The standalone program `VERIFY.py` uses exact rational/integer arithmetic, builds Laplacians without using the transfer-current matrix formula, compares four evaluations of the degree generating polynomial for several dimensions, enumerates spanning trees on small rook graphs and tests finite-ratio extremizers. It prints `VERIFY_OK 2522 exact assertions` when all checks pass.

The program supplies checks of implementation and low-dimensional boundaries, not a proof of the infinite statements. The spectral decomposition, block eigenanalysis, convexity inequality, and Poisson approximation are independently presented in the written proof. The originality claim is a qualified comparison with inspected literature, not a guarantee of priority. Independent audit has not yet been performed.
