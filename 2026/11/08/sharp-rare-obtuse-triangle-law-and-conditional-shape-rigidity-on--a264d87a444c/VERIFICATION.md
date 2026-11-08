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

# Verification of rare spherical obtusity

The analytic proof establishes the all-dimensional exact integral, the high-dimensional asymptotic with a relative \(O(d^{-1})\) error, the conditional central limit theorem and the limiting right-isosceles shape. Numerical verification is supplementary.

The embedded `verify.py` is executable using Python with NumPy, SciPy and SymPy. It checks the exact saddle location and curvature with symbolic algebra, verifies \(p_3=1/2\) and \(p_5=17/70\) by beta-cap quadrature, compares five increasing-dimensional exact integrals with the predicted prefactor and exponential rate, checks the conditional variance scale, and simulates 180,000 independent triples of sphere points at fixed dimension six. A deterministic seed is used.

Run `python verify.py` in the same directory after extracting this complete package; no previous artifacts are needed. The numeric computation has finite tolerance and cannot establish any limiting statement. The original source formula and its sampling convention have been checked against the primary full text. All computed constants and probability normalizations are independently derived in the proof.

The older 1996 comparator is cited as a historical risk rather than claimed to have been read in full. No external independent audit has been performed.
