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

# Reproducibility

Run `python verify.py` with Python 3 and the standard library. The actual checked artifact returned:

```
VERIFY_OK 777 exact assertions; exhaustive Pruefer n=3..7
```

The checker enumerates every Prüfer sequence for each order from three through seven, takes all allowable subset sizes with a fixed common vertex, and compares exact rational observed masses to the independent binomial-plus-coupled-Bernoulli law. It separately checks each marginal, covariance, the upper-tail gap and the exact joint total variation identity.

The finite checker does not certify the infinite theorem; the weighted matrix-tree determinant and the ordinary binomial Stirling estimate in RESULT.md establish its full scope. Historical-priority confirmation and independent mathematical audit remain outstanding.
