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

# Reproducibility and boundaries

The proof is self-contained in `RESULT.md`. Reproduce from the package directory with Python 3, using only the standard library:

```
python3 check_enumeration.py
python3 check_constructive.py
```

`check_enumeration.py` builds every legal Dyck word at semilengths 1–11 and computes the entire fourteen-entry linear substring-multiplicity vector without relying on the symbolic classification. `check_constructive.py` independently constructs all feasible parameter cases through semilength 22, checks the Dyck prefix property and unique vector signatures. Both programs completed successfully. They are bounded consistency checks, not computational substitutes for the all-length proof. The equivalence-class size distribution, noisy readings and lengths greater than three are not proved.
