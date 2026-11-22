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

# Exact finite verification and proof boundary

Run `python3 verify.py` with Python 3 standard library. The code uses integer arithmetic exclusively and requires no downloads. It computes all total-dominating incidence masks of labelled paths \(P_n\) for \(2\le n\le16\), their full Walsh--Hadamard transforms, and a completely separate parity-chain signed-independence recurrence. For \(2\le n\le8\), it also computes each character sum directly over enumerated total dominating sets. The independence-set signed recurrence is checked against a separate fast Walsh transform for every frequency and chain length \(0\le L\le15\).

The observed exact terminal output was:

```
TOTAL_DOMINATION_WALSH_EXACT_PASS assertions=197234
ranks/nullities n=4,7,10,13: (4, (4, 12)) (7, (44, 84)) (10, (484, 540)) (13, (4444, 3748))
```

The exact all-length proof is in `RESULT.md`; no finite test is interpreted as exhaustive evidence for an infinite statement. The checker is supplementary and does not verify historical originality or independent mathematical review. All multipliers are unnormalized integer sums; no claim about a normalized convolution kernel is made.
