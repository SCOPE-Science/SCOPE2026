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

# Reproduction and proof checks

The mathematical proof is in `RESULT.md`. In particular, its arbitrary-length steps are the unique left-special factor of each length, the forced two-sided predecessor contexts at the characteristic mechanical intercept, and the exhaustive restrictions on first-one positions. These steps, rather than a finite data fit, establish the all-length formula.

Run the standalone file with Python 3:

```sh
python3 verify_sturmian_tortoise.py
```

Expected stdout:

```text
STURMIAN_TORTOISE_VERIFY_OK 8 648 rotation_cell_census prefix_independent_scan n_le_81
```

The code enumerates the \(n+1\) irrational-rotation coding intervals at each length \(1\le n\le81\), checks image-fiber membership and cardinalities, and independently compares their factor sets to those obtained by scanning long prefixes through length \(27\). It evaluates eight algebraic-irrational slopes at 72-digit decimal precision. Near-boundary examples are evaluated only to the stated finite lengths. This check uses approximate arithmetic and has neither infinite quantifier coverage nor independently reviewed proof status. The symbolic arguments, exact domain and exclusions are stated in `RESULT.md`.
