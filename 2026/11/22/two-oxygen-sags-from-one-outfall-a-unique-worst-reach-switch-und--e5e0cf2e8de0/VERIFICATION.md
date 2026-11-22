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

# Reproduction

Use Python 3 standard library and execute `python3 verify.py`. The checker computes exact rational strict enclosures for the illustrative critical-location bracket, verifies closed-form solutions and one-sided derivative identities, checks 20,000 reproducible exponential-input parameter instances, and samples 3,750 ratio comparisons for nonexponential log-concave demand inputs. The verified output includes `All finite supplemental checks passed.`

The exact rational numerical enclosure is a finite calculation with a rigorous remainder formula; all quantified shape and uniqueness conclusions follow from the proof in `RESULT.md`, not these finite checks. The code tests the intended idealization only and does not validate field coefficients, physical oxygen saturation or historical originality.
