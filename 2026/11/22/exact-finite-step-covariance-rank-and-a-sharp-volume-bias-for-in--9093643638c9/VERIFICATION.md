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

Run `python3 -S verify_rank.py` using Python 3 with only its standard library. It reports `VERIFY_OK 248`. The script checks exact rational original transformed Shu–Osher stages against separately assembled composite quadrature matrices; ranks in dimensions \(2\) through \(7\), five time-step counts, and three positive rational step lengths; real-spectrum diagonal stable examples at exponential sample times with rational values; weighted Vandermonde Gram determinants; and the three-state determinant ratio \(5/2\).

The analytical zero-count lemma for exponential polynomials with real exponents establishes the arbitrary-dimension, arbitrary-step rank formula; the finite computational tests cannot prove it. At the nilpotent witness, the exact continuum determinant is calculated from Hilbert moments and the discrete determinant from a three-node Gram matrix, not inferred numerically. No finite-precision lower bound for positive eigenvalues, extension to non-real spectrum, or independent validation is claimed.
