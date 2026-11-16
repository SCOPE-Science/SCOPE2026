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

The identity for the normalized Gram kernel was derived from the exact weighted upper-half-plane Bergman kernel and the nine-term mixed derivative expansion for real coefficients. The companion standard-library `CHECK.py` enumerates 414 finite parameter or derivative-consistency configurations. It verifies cancellation of odd inverse powers, both surviving even coefficients, locations and multiplicities away from and at the phase threshold, and direct complex evaluation of the nine mixed-derivative terms.

Reproduce by running `python CHECK.py` alongside this file. The observed success output is `PASS 414 parameter or derivative-consistency configurations`.

These are finite checks. The universal sharp criterion, exhaustive count of accessible zeros and boundary-double-root claim follow from the analytic quartic factorization, quadratic discriminant, and surjectivity of the upper-half-plane difference variable given in `RESULT.md`. The classification is confined to real first- and second-derivative coefficients and does not address arbitrary complex coefficients.
