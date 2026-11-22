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

# Reproducible finite verification

Execute from the directory containing the attached files:

```
python3 verify_positional.py
python3 verify_recursion.py
```

The positional program exhaustively tests every ordered deletion of the source period in \(P^{r+1}\) for 36 cases with \(2\le q\le7\) and \(0\le r\le5\), capped at 1,500 embeddings per case. It checks the exact complement language generated from nondecreasing phase codes, the count and every collision-fiber size. The recursive program independently computes complement sets by two-choice recursion on the source and deleted pattern, and compares them to a direct phase-language construction in 25 cases with \(2\le q\le6\) and \(0\le r\le4\).

Expected exact outputs are preserved in `positional_output.txt` and `recursion_output.txt` respectively. The arithmetic theorem for all parameter values is established by the proof in `RESULT.md`, not by exhaustively checking infinitely many cases. Neither program supplies an independent external audit or formal proof certificate.
