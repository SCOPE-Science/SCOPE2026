---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the biclique majority–minority attraction census

The proof is the exact three-coordinate reduction in `RESULT.md`. Each checker independently implements one aspect of the finite dynamics using only the Python standard library. To run all four together, use Python 3.10 or newer (`int.bit_count` is used by the direct and invariance checkers). From a directory containing the four `check_*.py` files, run:

```sh
python check_direct.py
python check_quotient.py
python check_basins.py
python check_invariance.py
```

Observed checks in this package:

- `check_direct.py`: PASS on 260,100 labelled initial states for all \(1\le a,b\le8\); both periodic orbit types, first entrance times, fixed counts and oscillation populations match the formulas.
- `check_quotient.py`: PASS on all 1,600 parameter pairs with \(1\le a,b\le40\), using exact binomial multiplicities for each reduced signature.
- `check_basins.py`: PASS on individual basin-size multiplicities at all 64 pairs with \(1\le a,b\le8\), using a separate bit-vector update routine.
- `check_invariance.py`: PASS for 257,040 labelled initial states with \(3\le a\le8\) and \(1\le b\le8\), comparing eventual period-two membership with an independent ordinary-majority update.

The checker source is included; the counts above are finite computations and are not a proof of the unbounded-parameter statements. Those statements follow from the explicit transition recurrence and binomial count in `RESULT.md`. No external independent validation is represented by this file. The cited 2009 mixed-majority source was assessed from an available abstract only; historical equivalence cannot be excluded from that access.
