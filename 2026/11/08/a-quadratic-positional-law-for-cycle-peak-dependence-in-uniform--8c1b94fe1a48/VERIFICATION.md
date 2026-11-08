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

The standalone `verify.py` checks the exact formula for all \(n=3,\ldots,8\), every position triple and all image prescriptions for \(n\le6\), using integer and rational arithmetic. Last executed result: `VERIFY_OK 3237 exact assertions`. Reproduce with `python3 verify.py`. Exhaustion is only finite corroboration; the proof in `RESULT.md` establishes the identity for every \(n\ge3\). Independent validation has not been performed.
