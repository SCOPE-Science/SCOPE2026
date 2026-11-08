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

## Computations replayed
The included `verify.py` uses Python 3 and NumPy. Its 80 finite checks constructed the exact integer principal Walsh matrices and verified \(4(G-NI)^3=3N^2(G-NI)\) for each, in addition to the corresponding numerical singular-value multiplicities. It covered dimensions \(2,4,6\), matching and complete polar graphs, affine linear masks, both constant coefficients, and all four-variable alternating polars whose squares equal the identity. The recorded result is `QUADRATIC_GRAPH_WALSH_EXACT_PASS cases= 80 involutive_four_dim_polar_matrices= 4`.

## Verification scope
The integer Gram check is exact only for the finitely many tested matrices; the floating-point spectrum comparison uses tolerance \(10^{-8}\). Neither proves an infinite-family theorem. The proof is the algebraic order-six Clifford-phase and order-three Gram argument given in `RESULT.md`. The claim is not a statement about a general bent graph or a nonlinear phase-retrieval operator.

## Independent audit
Not performed; no external mathematical validation or certification is claimed.
