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

# Verification record

The proof is self-contained in RESULT.md and covers all even integers \(q\ge2\). The source's lower circular arcs and upper corner are obtained directly from its explicit piecewise-periodic definition. The sharp axis radius follows from vertical geodesic endpoints and a feasible contained Euclidean rectangle. The strict improvement follows from exact hyperbolic distances to one supporting geodesic and the upper corner, a strict nearest-corner derivative sign, and compactness of the remaining boundary.

Execute `python verify.py` to reproduce 100 finite even-parameter consistency tests, for \(q=2,4,\ldots,200\). Checks include the hyperbolic disk's vertical extrema, strict horizontal-side clearance, correct parity positions, upper-corner derivative signs, and positive local contact-distance increments. For larger parameters, direct inverse-hyperbolic floating-point subtraction can round tiny positive increments to zero; the program therefore checks their positive pre-inversion arguments exactly up to ordinary floating-point positivity, rather than comparing rounded distances. The finite sample is an illustration and not an infinite-parameter certificate.

No exact unrestricted inradius, complete incenter classification, or odd-parameter assertion is claimed. No independent review has been performed.
