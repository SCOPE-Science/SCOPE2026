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

# Verification record

Run the embedded standard-library-only diagnostic script with `python3 verify.py`. It uses exact rational arithmetic and reproducible fixed-seed parameter selections. The observed output was:

```
Exact rational diagnostic assertions: 9791
Four contrasting parameter points passed.
```

Checks include the pgf recurrence through degree 22, signs of first 23 logarithmic coefficients when the analytically derived inequalities hold, first 22 monotonicity inequalities for canonical measures, first 22 log-concavity inequalities when \(\nu\ge1\), and four rational examples distinguishing the regimes. This is finite supporting evidence only. The known infinite-divisibility boundary is reproduced for context using signs of **every** even coefficient; for thinning it establishes all even-index differences; for log-concavity failure it proves an eventual positive second log-difference using full asymptotic expansion. No independent validation has been performed.
