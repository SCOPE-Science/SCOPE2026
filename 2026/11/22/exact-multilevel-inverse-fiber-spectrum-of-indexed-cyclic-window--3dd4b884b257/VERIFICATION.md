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

# Computational verification and scope

Execute `python3 verify.py` from a directory containing the accompanying file. The script uses only Python's standard library. It independently forms every cyclic readout by direct integer addition, groups outputs into complete source fibers, and compares every inverse-frequency count with a normalized-pattern computation.

Recorded output:

```
VERIFY_OK parameter_cases= 168 source_instances= 599000 q_ranges=2:2..12,3:2..9,4:2..7,5:2..6 three_residue_ternary=1..3
```

It separately checks mass conservation, the all-alphabet distinct-output formula, the central-coefficient maximum, and the seven-level ternary special case. A finite check of these ranges is not a proof for all lengths; the algebraic proof in `RESULT.md` carries the universal quantifiers. No external certification is claimed.
