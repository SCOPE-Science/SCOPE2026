---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

## Reproducibility and limits

Run `python3 check.py` using the Python standard library. The program computes exact projected stochastic matrices and normalized lag-one statistics for the connected four-vertex and disconnected seven-vertex sharpness witnesses. It checks the relevant projected stationary laws, equality of all one- and two-edge projected kernels, the exact three-edge gaps, and reconstruction from these statistics. It also tests reconstruction from the analytic lag formula on all simple graphs without isolated vertices on fixed labelled vertex sets of orders two through five (814 graphs total). The finite runs illustrate the analytic proof; they do not supply the unbounded quantifier. The proof uses inclusion–exclusion and reconstructs labelled vertex stars directly.

```text
N=4: labelled order-two kernels coincide; the order-three gap is 9/128
N=7: labelled order-two kernels coincide; the order-three gap is 9/224
PASS: 814 additional simple graphs on at most five vertices without isolates
```
