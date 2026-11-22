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

The exact-rational certificate script `check_iterated_durrmeyer.py` was executed on the stated input grid. It computed 96 spectral-vs-Bernstein composition identities, checked stochastic symmetric matrices and adjacent strict TP2 minors, verified the first-step identity, two-mode alternating bounds, and strict submultiplicativity across finite cases. It printed `ALL_ITERATED_DURRMEYER_CHECKS_PASS`. These computations check the algebra but cannot establish an all-integer theorem. The proof in RESULT.md supplies the infinite-quantifier argument using strict TP2, unique midpoint crossing, BV derivative-measure decomposition, and Legendre diagonalization. No independent audit has been performed.
