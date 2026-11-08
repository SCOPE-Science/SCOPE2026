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

# Verification of exact intensity geometry

Run `python CHECK.py` with Python 3 and NumPy 2+. On the generated package, it reports `PASS 616 assertions`. The independent checks evaluate Fourier intensity from its explicit exponential formula, numerically invert it at selected lags, integrate original covariogram differences without presupposing the cubic identity, integrate first derivatives to form the Gram matrix, check the closed eigenvalues, and compare finite differences in the full data norm. They do not test every real parameter and are not a substitute for the general proof.

The proof is analytic: an exact convolution identity, a full three-case integration of triangular autocorrelation, the Hilbert-space midpoint lemma, and a piecewise-function Fréchet derivative with explicit cross term. The time-domain Fourier convention is unitary on L2, so no factor of \(2\pi\) is omitted. Exact symbolic conditions and interval boundaries are stated in `RESULT.md`. The reviewer status is same-model only; no independent verification has occurred.
