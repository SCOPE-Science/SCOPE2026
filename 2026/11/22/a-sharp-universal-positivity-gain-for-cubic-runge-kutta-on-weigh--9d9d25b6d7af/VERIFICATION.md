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

# Verification of the weighted-bipartite cubic RK theorem

The standalone `verify.py` uses only Python 3 standard-library exact `Fraction` matrices. Running `python3 verify.py` from this package yielded:

`VERIFY_OK weighted_bipartite_graphs= 486 exact_entry_checks= 178505 SSP_assertions= 20`

The checker independently computes the cubic Runge–Kutta endpoint from exact matrix products, reconstructs diagonal/edge/distance-two/distance-three identities, compares all entries, and checks row stochasticity and the SSP convex-decomposition identity. Tests cover multiple families and randomly generated rational positive conductances. The actual output is included in `VERIFY_OUTPUT.txt`.

The proof is analytic: edge quadratic discriminants are strictly negative, distance-two terms cross at their exact positive roots, and each diagonal is a strictly decreasing spectral mixture of cubic Taylor polynomials. The extremal 1 and alpha constants follow from the stochastic convex combination and a maximum-degree diagonal, with concrete cycle and star sharpness witnesses. No finite test establishes the universal quantified claims; the proofs in `RESULT.md` supply those deductions.

Limits: bipartite undirected symmetric positive-weight finite graphs; completed classical cubic RK matrix, not internal stages, all higher-order RK polynomials, method stability, or error-optimal time stepping. No independent audit or historical-priority certification has been performed.
