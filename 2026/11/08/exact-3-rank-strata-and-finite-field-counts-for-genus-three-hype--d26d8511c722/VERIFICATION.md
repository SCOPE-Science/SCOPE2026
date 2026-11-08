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

# Reproducibility and limits

Run `python3 verify_octic.py` with standard Python 3; no third-party dependencies are required. The recorded output is `verification_output.txt`. The program builds finite fields of cardinalities \(3\), \(9\), and \(27\); checks squarefreeness independently via polynomial greatest common divisors; computes the semilinear stable Hasse–Witt rank from matrix powers; and compares the full count of coefficient triples against the exact closed formulas. Successful output terminates with `ALL_CHECKS_PASSED`.

The complete checks found \(19\), \(655\), and \(18979\) smooth triples, with respective 3-rank distributions \((0,0,9,10)\), \((0,32,101,522)\), and \((0,0,1353,17626)\). They are finite checks, not exhaustive checks over all extension fields. The general claim follows instead from the explicit Cartier-block rank computation, smoothness algebra, multiplicative-character generating series and elementary finite-field arithmetic in `RESULT.md`.

There has been no independent audit or third-party validation. The literature comparison is subject to the historical-priority limitations stated in `RESULT.md` and `REVIEW.md`.
