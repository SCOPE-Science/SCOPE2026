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

## Reproducibility and limits

- The local runoff formula, area-weighted expectation, unique active retention inversion, derivative identity, and two-soil benchmark are defined independently in `check.py`.
- `python check.py` runs deterministic randomized distributions and checks numerical monotonicity, equation inversion, derivatives, and the explicit sign-reversal example.
- Finite sampling does not certify the general theorem; the universal argument is the strict-concavity/Jensen proof in `RESULT.md`.
- Textual comparisons inspect a complete open two-class study and the available text of a later spatial-upscaling model. Full texts of some older curve-number-averaging studies were not accessible; historical priority is provisional.
- No independently conducted scientific audit has occurred.
