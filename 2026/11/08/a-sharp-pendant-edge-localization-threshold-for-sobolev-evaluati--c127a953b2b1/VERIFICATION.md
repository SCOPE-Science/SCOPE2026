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

# Reproducibility and limits
Run `python checker.py` with SymPy installed. The checker reconstructs each tested network by subdividing edges, uses exact-rational grounded Laplacian inverses to obtain effective resistances, and integrates the resulting piecewise quadratic functions exactly by Simpson's rule. It also checks the radical threshold identity for integers \(3\le r<70\). Expected diagnostic: `ALL_TWIGGED_BANANA_SOBOLEV_CHECKS_PASSED 103`.

The computation checks finite rational cases and the algebraic threshold formula; it does not verify every real \(h>0\) computationally. The proof in RESULT.md uses analytical effective-resistance and quadratic maximization identities to establish the universal statement. Equality is characterized by Cauchy--Schwarz in the real energy Hilbert space. No independent mathematical audit has been performed.
