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

# Reproducibility and limitations

The singular-value decompositions and one-variable optima are proven in RESULT.md. `CHECK.py` uses only Python's standard library; running `python CHECK.py` tests each formula for dimensions one through forty on an independent fine grid. The checker establishes only finite diagnostics and identities, not general uniqueness, publication priority, or any independent mathematical certification. The structural arguments for countably infinite masks use finite-submatrix exhaustion and the two-block decomposition proven in RESULT.md. The historical literature comparisons are described in REVIEW.md and AUDIT.json.
