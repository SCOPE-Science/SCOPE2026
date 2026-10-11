---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Variation of constants gives z≥0 on bounded complete trajectories and forces the origin if z reaches zero. Applying invariance to an arbitrary antiderivative H(z) yields the test-function identity and therefore the conditional expectation, localized Borel formula, moment hierarchy and size-biased marginal. The checker confirms only algebraic generator premises, not stationarity itself.

## originality

FAIL

The central conditional law is the immediate coordinate specialization of the standard stationary-generator identity. Taking a test function depending only on z converts stationarity and the equation for z directly into the claimed conditional expectation. The Borel, moment and size-bias forms are routine restatements; support nonnegativity follows separately from variation of constants.

## value

FAIL

The main identity is a textbook one-test-function consequence of stationarity, and the positivity part is the elementary stable linear-filter formula for the last coordinate. The result does not require a new structural lemma, nontrivial boundary or independently hard invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
