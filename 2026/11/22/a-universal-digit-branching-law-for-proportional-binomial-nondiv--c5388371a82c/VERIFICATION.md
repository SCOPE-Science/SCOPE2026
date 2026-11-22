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

Run `python3 verify.py` with Python 3.8 or later in the extracted directory. The expected single output line is `VERIFY_OK 14130 exact assertions`. The checker performs direct small-index binomial modular tests, exact digital-transition enumeration, all-carry branch counts, and prescribed-suffix census checks. It does not infer a theorem from finite samples; the unlimited claims are justified by the balanced affine-digit lemma and induction in RESULT.md.

The mathematical derivation has received self-review only. No external proof assistant, independent mathematical audit, or formal certification is claimed.
