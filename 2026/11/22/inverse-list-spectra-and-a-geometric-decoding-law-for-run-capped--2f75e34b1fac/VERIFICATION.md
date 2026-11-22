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

The structural proof treats every \(h\ge1\) and \(m\ge1\), while `verify.py` independently checks exact finite cases. Command: `python3 verify.py`. Actual output: `VERIFY_OK words= 20470  compatible_parent_incidences= 123144  h=1..5, m=1..11`.

The checker constructs all one-insertion words and filters by the source constraint; it separately constructs run-length compositions and their predicted size histogram. The rational-series and asymptotic statements are proved algebraically in RESULT.md, not inferred from exhaustive finite samples. No independent audit has been performed.
