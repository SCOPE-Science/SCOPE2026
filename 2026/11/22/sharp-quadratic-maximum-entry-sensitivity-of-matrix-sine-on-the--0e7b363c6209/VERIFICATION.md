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

# Reproducibility

Run `python verify_sine_b2.py` in an environment with SymPy, NumPy and SciPy. During preparation the script passed its exact symbolic algebra checks, a rational Sturm root count, interior finite-difference comparisons and 400 pseudorandom Taylor-remainder checks.

The infinite-dimensional quantifiers over positive band widths and all admissible matrices follow from the analytical proof in `RESULT.md`. The finite tests do not establish these universal claims. The originality evidence is a qualified comparison rather than historical certainty. Independent mathematical validation was not performed.
