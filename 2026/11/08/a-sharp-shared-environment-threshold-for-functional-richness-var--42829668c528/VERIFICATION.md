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

From the extracted package directory, run `python -m pip install -r requirements.txt` then `python check.py`. This script (a) confirms the all-parameter rational derivative identity symbolically, (b) validates all six coefficient formulas, (c) tests representative rational finite cases by complete enumeration of up to ten binary survival variables under the shared Beta distribution, and (d) checks the exact rational witness. It reports PASS only after all assertions succeed. `RESULT.md` contains the proof that establishes the universal quantifiers and the unique-root sign argument; a finite collection of test points alone would not establish the theorem. No external/independent validation has been performed.
