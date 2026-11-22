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

# Reproduction and limits

Run `python3 -S verify_ice7.py` in a Python 3 environment with the standard library. The script must print `ICE7_EXACT_PASS` and the exact signed spectrum, rank, low-weight zero supports, full projection-kernel histogram and sharp norm.

It checks all 16,384 orientation bitstrings in one labelling and independently all 16,384 cyclic jump-coordinate assignments; both yield the identical 60 orientations. A separate finite multivariate coefficient dynamic program confirms 256 distinct cut-gauge signed sums, and the full integer Walsh transform supplies all 16,384 spectral values. Parseval, the first even-weight zero characterization, the exact Fourier support inverse and its integer \(\ell^1\) sum 71,936 are asserted.

The unrestricted sharpness of the projection norm is an analytic finite-group translation-averaging argument supplied in `RESULT.md`. Exact finite enumeration establishes this graph only; no infinite-size extension, absolute literature priority or independent validation is claimed.
