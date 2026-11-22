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

# Verification details

To verify the rational diagnostics, run `python checker.py` using Python 3.9 or later. It uses only the standard library, with the expected terminal output `PASS 14412 exact assertions`.

The checker verifies the cross-term expression for the apparent local exponent against derivatives of the two-power discharge, derivative signs against the polynomial-power sign expression, positivity of the excess and the two rational examples for integer powers \(2\) through \(5\). It also verifies several exact amplitude envelopes for the special square-law case. The continuum proof, uniqueness and sharp boundary rest on the algebra and monotonicity argument in `RESULT.md`, not on finite samples.

The model assumes independently draining stores, no inputs during the recession and no measurement noise. Independent external mathematical and bibliographic validation has not been performed.
