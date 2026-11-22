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

The standalone verifier `artifacts/verify.py` uses Python 3 standard-library code. Execute `python3 artifacts/verify.py` from this package root. Expected output: `ALL_HEIGHT_TWO_CHECKS_PASS 255`, recorded in `artifacts/verification_output.txt`.

The checker directly builds each finite order with a new point, performs full transitive closure and compares the resulting admissible-extension counts to independent-set/biclique enumeration. It tests all small missing-edge patterns through three deleted relations on sides of at most three vertices, then exercises the matching formula and the sharp first/second minima for additional parameters, including the four-by-four case. This independently checks finite cases only. The infinite inequality and equality classifications depend on the written combinatorial proof and Harris's product-measure correlation inequality, not on computational extrapolation.
