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

# Mathematical verification and reproducibility

The exact proof is given in RESULT.md. The calculation is anchored in the periodic Bernoulli kernel identity, the principal two-by-two eigenvalue lower bound, and a **continuous** three-gap feasibility obstruction. Boundary equality is checked algebraically; the top eigenvalue and its multiplicity follow from an explicit Gram matrix.

Run `python checker.py` using Python 3 with SymPy and NumPy. The checker is independent of all prior work products: it evaluates symbolic algebraic identities, eigenstructure and exact inequalities from the printed formulas, then checks 551,300 rational circular gap triples and 19,600 additional numerical Gram eigenvalue comparisons. At the proposed optimum a separate piecewise polynomial Gauss-rule integration of the representer derivatives reproduces the Gram entries and top singular value. Its exit status zero and final `all checks: PASS` report mean that the stated script checks passed. The exact proof, not the finite enumeration, establishes the universal assertion.

No computational search is taken as evidence that all real configurations have been exhausted. No noisy-sample or more-than-three-sample claim is verified, and independent validation has not been performed.
