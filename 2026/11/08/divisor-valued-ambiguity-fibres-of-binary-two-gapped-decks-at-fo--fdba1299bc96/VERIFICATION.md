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

# Reproducibility and limits

Run `python3 verify.py` with Python 3.8 or newer. The script uses only the standard library. It counts every separated positional pair directly, without calling the mathematical proof's formula for the observations, then groups words by their resulting deck and independently evaluates the proposed fibre formula.

Observed output from the packaged program:

```text
VERIFY_OK words=8094 profiles=5611 ambiguity={2: 1, 4: 1816} multiplication_tables=529 divisor_examples=120
```

The literal checks exhaust all binary words having at most four runs and length at most 18. They verify every observed class size, exact run recoverability, and the cross-pair invariant; they separately verify multiplication-table and divisor identities on finite parameter grids. The proof in `RESULT.md`, rather than this enumeration, justifies the unlimited-length claims. The source's pre-existing six-letter collision is not a novel contribution of this result. No independent scientific audit was performed.
