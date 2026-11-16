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

Run `python CHECK.py` from the directory containing this file. The checker uses only Python's standard library, rational arithmetic at four rational \(q\)-values, and 1,152 exact samples of the vertex factorization, 48 exact facet samples and eight high-mode obstruction witnesses. The exact expected output is:

```
CHECK_OK exact_vertex_factorizations=1152 facet_interior=48 high_mode_obstructions=8
```

The universally quantified claims are established by the algebraic and analytic proof in `RESULT.md`; a finite checker cannot certify them. No independent audit has been performed.
