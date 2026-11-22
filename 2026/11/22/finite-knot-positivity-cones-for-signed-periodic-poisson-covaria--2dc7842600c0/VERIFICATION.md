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

The proof checks the signed Fourier convolution, homogeneous recurrence between successive source frequencies, and the reflected boundary recurrence giving the explicit inverse. At \(s=0\) and \(s=k\) the interpolation weights reduce to the knot values; for integer positions strictly inside the gap both weights are positive. Above the final source frequency, the Fourier sequence is a decaying geometric tail. Compact-circle Bochner positivity makes these Fourier facts necessary and sufficient for all finite Gram matrices. A finite Vandermonde matrix proves strictness when the tail is positive; a missing frequency proves failure of uniform density.

Reproduction: execute `python3 checker.py` in the same directory as this file, with the Python 3 standard library. It reports `PASS: 62027 exact-rational assertions`, comparing inverse knot maps, original convolution, interpolated values, ray supports, and signed examples for finite sampled radii, strides, and degrees. This is exact computation but not an infinite-range or all-parameter certificate. The universal statements are proved analytically. No independent audit has occurred.
