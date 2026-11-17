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

Run `python3 check_antidictionary.py` (standard-library only). The checker constructs factor languages of the proportional-run block monoid and directly compares all missing-but-prefix-and-suffix-admissible words with the three proposed templates for each \(k\in\{1,2,3,4,5\}\) and each word length from 3 through 16.

Observed result: `VERIFY_OK block_coded_parameters=5 word_lengths=3..16 exact_comparisons=70`.

These tests establish only 70 finite parameter-length equalities. In particular they cannot prove the general theorem; the proof's run-parsing sufficiency lemma and minimality of each template are the essential infinite steps. The mathematical result has undergone self-review, not independent audit.
