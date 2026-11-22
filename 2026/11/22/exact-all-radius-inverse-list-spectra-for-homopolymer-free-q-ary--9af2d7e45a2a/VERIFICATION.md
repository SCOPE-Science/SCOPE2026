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

# Reproducible checks

Run `python3 checker.py` with Python 3 standard library only. The program checks distinct length-\(m+d\) homopolymer-free sources against distinct subsequence outputs for multiple alphabets and length/deletion pairs; uses an independent deterministic greedy-subsequence DP for larger instances; and checks the strict spectrum and feasibility count as exact integers.

Expected output includes:

```
PASS 70295 receiver configurations 72586 source configurations (summed over lengths and deletions)
INDEPENDENT DFA PASS 2260
SPECTRUM CHECK PASS 2016 alphabet/length/deletion configurations
```

The full theorem is supported by the bijective argument in `RESULT.md`; a finite checker by itself cannot establish all lengths. The checks enumerate distinct predecessor **words**, not embedding/deletion-mask multiplicities. No independent audit or certification is claimed.
