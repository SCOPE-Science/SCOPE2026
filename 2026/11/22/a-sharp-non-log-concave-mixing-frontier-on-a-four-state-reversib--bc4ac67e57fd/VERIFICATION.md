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

# Verification details

The reproducible `verify.py` checks the closed-form eigenvector, parity block characteristic polynomial and strict interlacing identity, exact row-saturation identity for the low-mass optimum, the high-mass odd-block matrix-square identity, and coincidence of the two branches at the threshold. It then compares the proposed SLEM with spectral decompositions for twelve prescribed mass ratios and 1,800 feasible independently randomized edge-weight triples. The script finished with `ALL CHECKS PASS` in the delivered source checkout.

The continuum proof uses the Rayleigh principle and a sharp endpoint-vector operator-norm bound, neither of which depends on finite enumeration. The proof assumes strictly positive stationary masses and nonnegative transition probabilities with holding allowed. No claims concern irreversible kernels, longer paths or non-reflected stationary laws. Independent review has not been performed.
