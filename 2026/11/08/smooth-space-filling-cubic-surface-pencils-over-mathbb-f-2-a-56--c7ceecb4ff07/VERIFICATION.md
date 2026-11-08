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

# Reproduction notes

Execute `python3 verify_pencils.py` and `python3 verify_base_cycle.py` with Python 3 and no third-party packages. The first program enumerates all nonzero alternating matrices and all rational lines, checks all 56 pencils and the transvection orbit, and exhaustively rejects three-dimensional all-smooth systems. The second independently enumerates every projective line over the four-element extension, checks the seven base-support lines and Jacobian dependence, and displays the degree and arithmetic-genus checks.

Exact expected markers:

```text
FROBENIUS_CUBIC_PENCILS_PASS 28 56 56 56 360 35
FROBENIUS_CUBIC_BASE_PASS 5 2 7 85 357 9 4 10
```

All calculations are exact. The second program does not treat its extension-field census as an infinite-field proof: elimination of any further geometric component follows from the complete-intersection degree argument in RESULT.md. Historical priority and independent mathematical validation have not been performed.
