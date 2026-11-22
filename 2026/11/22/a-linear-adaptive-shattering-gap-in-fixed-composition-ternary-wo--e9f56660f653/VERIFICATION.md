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

# Reproducible checks and limits

From the package root, run `python3 checker/verify_online.py`. It reads the exact `checker/depth3_tree.json` leaf certificate; every one of the \(2^3=8\) answer paths is checked against its displayed fixed-composition realization, and the twelve-concept count excludes depth four. Expected output:

```
TERNARY_FIXED_CONTENT_DEPTH3_PASS 12 hypotheses 8 certified leaves
BASE_VC_2_LITTLESTONE_3
```

Optionally compile `g++ -std=c++17 -O2 checker/check_quota.cpp -o check_quota` and run `./check_quota`. Its complete output is in `checker/quota_output.txt`; it checks 61,481 candidate supports with at most the number of available positions through nine finite capacity profiles. The enumerator independently counts all realized binary traces and compares them with the capacity criterion. These finite checks do not verify an unbounded recursion automatically: the proof in RESULT.md supplies the full all-order argument by embedding a product of \(m\) independent seed blocks.

No external proof assistant, independent auditor, or formal verification is claimed. The research does not establish the optimal adaptive dimension for larger \(m\).
