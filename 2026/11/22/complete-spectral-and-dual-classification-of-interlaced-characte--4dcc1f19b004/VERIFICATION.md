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

# Reproducibility and finite checks

The algebraic proof in `RESULT.md` is self-contained and applies to arbitrary integers \(p\ge2\), \(1\le m\le p\). It uses exact finite-character orthogonality and a finite occupancy count, without relying on numeric testing. The crucial basis, outer-product and reconstruction formulas can be checked directly from the definitions.

Run `OPENBLAS_NUM_THREADS=1 python check.py` with Python 3 and NumPy. The checker constructs the actual cyclic translation and modulation atoms independently of the proof's unitary coordinates. It then computes the frame operator and numerical eigenvalues, testing all eigenvalue multiplicities and the eigenrelation for each atom. Its deterministic cases span \(p=2,\ldots,6\) and multiple injection choices and masks; the recorded result is **1,281 passing matrix tests**.

The script also independently enumerates all binary masks for the small periods \(p=2,3,4\), \(m\le3\), checking the generating-function frame-mask count and optimal frame-condition number with exact integer counts. It reports **63 passing cardinality/count tests**. These tests are finite sanity checks, not exhaustive for arbitrary period, and do not substitute for the proof. The only numerical tolerance is the direct complex-matrix floating-point comparison of eigenvalues/eigenvectors.

Scientific comparison was made with Asipchuk–De Carli–Rodriguez, arXiv:2605.16139, and related finite-frame sources as detailed in `REVIEW.md`. The proposed result uses the prior structural block theorem and claims the explicit all-mask evaluation and design census, not independence from general finite-frame theory.
