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

Run `python3 verify.py` from the extracted package directory. The checked output was:

```
VERIFY_OK 6556 exact coefficient/shell/Bernstein checks
```

The script uses only the Python 3 standard library (`fractions`, `itertools`, `math`). It compares the independent Hamming adjacency-walk recurrence to closed-form shell entries at selected integer dimensions and alphabet sizes, verifies each Bernstein coefficient identity by exact rational arithmetic on a broad parameter grid, and evaluates a direct sparse Laplacian polynomial on small Cartesian graphs. The proof for all integers and all real timesteps is the symbolic Bernstein-sign argument in RESULT.md, not the numerical enumeration. Public verification has no independent mathematical certification or third-party audit.
