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

# Computational verification and limits

Run `python check_dyadic_inverse.py` with standard Python 3. The checker constructs the modular inverse graph directly, enumerates ordered pair sums without invoking the theorem, and compares the resulting count for every target to an independently implemented dyadic square-root rule. It separately checks the closed image-size and energy formulas. Passed for each exponent 4 through 11; at exponent 11 this covers 4,194,304 targets and 1,048,576 ordered source pairs. Marker: `DYADIC_INVERSE_GRAPH_FULL_CONVOLUTION_PASS`.

The checker uses exact integer arithmetic throughout. It neither proves the all-exponent assertions nor supplies independent mathematical certification. The proof in RESULT.md supplies the infinite argument; verification does not assert historical uniqueness.
