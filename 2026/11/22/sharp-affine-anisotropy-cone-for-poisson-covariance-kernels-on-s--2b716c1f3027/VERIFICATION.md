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

The analytic argument establishes the claim for every integer dimension \(d\ge2\), every \(0<r<1\), and every real affine parameter pair. The included `check_poisson.py` performs exact rational matrix comparisons and numerical integral quadratures, but these finite checks do not constitute a proof of universal positivity or nonpositivity.

Run `python3 check_poisson.py`. Dependencies are Python 3, NumPy and SciPy. Exact rational Fourier-block tests cover 1,681 matrix entries. The exact outside-cone witness has factorized energy \(-1/26\). Twenty-four independent sphere-integral tests and thirty-six independent circle-integral tests of the Poisson midpoint identity had maximum absolute residuals of \(4.11\times10^{-14}\) and \(1.51\times10^{-14}\), respectively.

For analytic reconstruction, compare the degree-\(m\) and degree-\(n\) harmonic blocks of \(T_sM_vT_s\) and \(M_vT_{s^2}+T_{s^2}M_v\). Coordinate multiplication links only degrees differing by one. This yields the exact operator identity, the nonnegative-weight sufficient condition, a negative smooth-function witness outside the cone, and strict finite-point positivity at equality by harmonic uniqueness. No independent audit has been performed.
