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

# Verification performed

Running `python3 verify.py` from the folder containing the seven supplied files gave `PASS: 3359 exact rational assertions, all finite.` The code enumerates all increasing recursive parent maps and all binary edge-deletion masks through seven vertices, independently computes their root-component sizes and exact expectations conditional on each deletion count, and verifies the stated rising-factorial identity for moment orders one through five. It also checks a separate rational-coefficient product expansion up to 22 vertices and exact finite log-concavity diagnostics.

The complete all-size and asymptotic results do not rest on enumeration. Their critical analytical steps are the marked rising-factorial recursion; exact coefficient extraction; a Fourier-inversion local central limit for the factorial-moment-tilted deletion count; gamma asymptotics; and moment determinacy. No independent audit has been conducted.
