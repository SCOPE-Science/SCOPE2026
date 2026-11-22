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

From the containing directory, run:

```bash
python3 VERIFY.py
python3 VERIFY_THRESHOLD.py
python3 VERIFY_EXTENSION_FIELD.py
```

The three exact-arithmetic scripts use Python's standard library only. Expected terminal markers: `VERIFY_OK`, `THRESHOLD_VERIFY_OK`, and `EXTENSION_VERIFY_OK`.

`VERIFY.py`: tests exact evaluation-matrix inversion and recovery of four randomly constructed symmetric multiplication tables for each listed parameter case, including rational calculations and prime-field computations. It does not assume a generic tensor. `VERIFY_THRESHOLD.py`: calculates ranks from every vector in the prime fields of orders two, three and five for dimensions two and three and degrees across the field-size threshold, and checks the Frobenius identity. `VERIFY_EXTENSION_FIELD.py`: independently verifies multiplicative arithmetic and the same phase transition over the nonprime finite field \(\mathbb F_4\).

Proof obligations not discharged by finite code are discharged in `RESULT.md`: the evaluation duality, polynomial nonvanishing over arbitrary infinite fields and over all \(\mathbb F_q\) with \(m\le q\), ideal preservation, and counterexample for every larger arity. No independent audit has been performed.
