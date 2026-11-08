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

# Reproducibility

The scientific argument is fully given in `RESULT.md`; the standalone `checks.py` supplements, but does not replace, its proofs.

Run `python checks.py` using Python 3 standard library. An actual run passed **6,594 grouped finite assertions** and an exhaustive adjacent-difference check across the indicated finite range. In particular it checks powers of the piecewise-linear level map by direct iteration, that the adjacent gaps are all one or two, and that block averages are exact right inverses on rational sample inputs. No floating-point or numerical-infinite extrapolation is involved.

The mathematical proof separately verifies quantifiers for every exponent \(1<p<\infty\), every starting coordinate, every orbit vector and all relevant times. The computation itself checks only the ranges hard-coded in `checks.py`; it cannot certify an infinite theorem, absolute novelty, or the contents of inaccessible literature.

An independent mathematical audit was not performed.
