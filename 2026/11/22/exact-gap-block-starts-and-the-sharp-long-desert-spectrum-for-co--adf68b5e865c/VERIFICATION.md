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

# Reproducibility checks

Run `python3 verify.py` with Python 3. The checker uses Dijkstra shortest paths for each residue class, independently predicts the complete Apéry rectangle and all gap-block starts for every \(3\le n\le120\), exhaustively enumerates actual gaps through the Frobenius number for \(3\le n\le60\), checks the exact larger-than-\(n+1\) spectrum, and verifies all membership positions by an independent coin-change recurrence for \(3\le n\le28\). The observed terminal line was:

```
VERIFY_OK n=3..120; Apéry entries and all starts checked: 583156 ; full runs n=3..60: 73776 ; independent DP n=3..28
```

All tests are finite and cannot establish the infinitely quantified statements by themselves. The proof in RESULT.md supplies the infinite argument. No external mathematical validation has been performed.
