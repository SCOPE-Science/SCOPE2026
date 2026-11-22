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
The analytic proof in `RESULT.md` is self-contained modulo the standard NP-completeness of positive-integer PARTITION. Every finite-dimensional matrix identity can be verified by elementary multiplication; the optimization over the cube uses strict positivity of the inverse Gram form. To replay exact rational diagnostics, execute `python CHECK.py`; the expected final output is `EQUIANGULAR_TERMINAL_WIDTH_RATIONAL_OK 2932`.

The checker tests finite examples and exact normal identities only. It does not establish the general theorem, bibliographic originality, or any independent validation. The exact threshold decision is weakly NP-complete on binary-encoded positive integer weights at a fixed common angle. The public-source first-version date for the motivating preprint is 2026-11-14; other references serve as earlier mathematical context.
