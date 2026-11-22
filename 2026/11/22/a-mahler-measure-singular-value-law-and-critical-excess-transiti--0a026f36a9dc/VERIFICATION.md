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

# Reproducible verification

Run `python verify.py` with Python 3.10 or later, standard library only. The current extracted run produced:

`FINITE_RATIONAL_CHECKS_OK 852 assertions; infinite spectral conclusions require the written proof`

The program checks exact rational determinants of leading Jacobi sections and arbitrary selected principal submatrices; the factorization into consecutive runs; the displacement lower bound in terms of run count; and exact geometric self-similarity of the squared modulus. Supplemental finite singular-value comparisons (not required to replay the proof) used direct dense finite matrix computations for several damping values and tap separations.

**Infinite mathematical verification:** RESULT.md Steps 1--5 supply an analytic compact-Jacobi min--max proof; partition generating-function convergence; exterior-product bounds; a critical determinant-divergence argument; exact Blaschke isometric duality; and finite residue-class decomposition. The checker does not replace those proofs. Publication priority is a best-knowledge literature comparison, not an independently certified assertion.
