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

The attached `verify.py` is a standalone Python 3.9+ integer-arithmetic checker with no third-party dependencies. It enumerates all labeled simple graphs on 2–5 vertices, filters connectivity, generates each single-deletion bond-percolation expectation by enumerating every open-edge outcome, and converts each candidate cost difference into two degree-six integer polynomials under the rational substitutions for the intervals on either side of \(p=1/4\). Their nonnegative coefficients certify each comparison over a continuum, including strictness when the polynomial is nonzero.

Actual replay: `PASS` for the connected labeled graph counts 1, 4, 38 and 728; the two and only two switching isomorphism classes; 60 and 30 labeled copies; 6,932 strict sign certificates; and the explicit optimal sets and polynomial differences. The proof uses the exhaustive finite range, not an unsupported extrapolation. A separate ordered-pair connectivity calculation validates the component-square score for every enumerated bond configuration.

Limitations: only simple connected undirected graphs of 2–5 vertices, a single perfectly removed vertex, a uniform remaining seed, and independent equal-probability bond transmission. Independent mathematical or historical review has not been performed.
