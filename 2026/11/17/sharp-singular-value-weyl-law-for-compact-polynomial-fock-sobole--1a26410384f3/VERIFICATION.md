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

# Scientific verification

The infinite-dimensional spectral claim is proved by the four-step analytical argument in `RESULT.md`. It uses exact monomial moments, a finite-band weighted Weyl lemma proved from closed-walk moments and Riemann sums, low/high-index control, and singular-counting perturbation inequalities. The source and target Hilbert norms are normalized by \(1/\pi\). Every leading coefficient and exponent has been checked against the exact factorial and gamma-moment formulas. The strict degree deficit guarantees compactness.

To reproduce the supplementary checks, run `python fock_weyl_check.py` with NumPy and SciPy. The checker passes \(182\) finite assertions on the two-band example, including direct factorial comparisons, nonnegative Gram spectra, and angular-moment identities. Finite-section singular values are not an infinite-dimensional proof; the theorem and the logarithmic critical coefficient follow analytically. No formal proof assistant or independent external audit was used.

The principal remaining scientific risk is priority relative to the general compact pseudodifferential Weyl literature or an undiscovered earlier Fock–Sobolev specialization. The theorem concerns only leading spectral behavior and explicitly excludes higher-order asymptotics and arbitrary entire coefficients.
