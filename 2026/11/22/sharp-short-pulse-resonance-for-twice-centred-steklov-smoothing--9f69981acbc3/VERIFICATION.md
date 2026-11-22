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

# Verification notes

The mathematical argument is self-contained in `RESULT.md`. The checkable identities are the four-box spline central and outer pieces, the exact derivative polynomial of the arc residual, the primitive \(\Phi\), the rational sign enclosure for its unique critical root, and the separated-jump plateau. `check.py` runs using Python 3 standard library only; it validates 1,628 exact-rational, decimal and bounded-Fourier assertions (the precise count is printed at execution).

At three bandwidths, independent Fourier partial sums verify the exact optimal pulse energy to within the explicit missing-tail bound \(2/(\pi^2N)\) after the first \(N\) positive frequencies. Such finite tests do not establish uniqueness, uniform bandwidth coverage or the full infinite-dimensional \(BV\) bound; those follow from the derivative-measure coupling, analytic fourfold-box convolution, and monotonicity proof. Numerical approximations to the root and constants are subordinate to their exact polynomial definitions.

No independent audit is represented or implied.
