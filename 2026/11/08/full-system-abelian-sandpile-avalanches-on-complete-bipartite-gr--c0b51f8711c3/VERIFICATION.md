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

# Reproducibility and verification

The proof of the theorem is in `RESULT.md`. For executable finite checks using Python 3 standard libraries only, run:

```
python3 checks/exhaustive.py
python3 checks/structural.py
```

`checks/exhaustive.py` uses the forbidden-subconfiguration recurrence criterion on every stable state for each of ten \((a,b)\) sizes, then independently stabilizes each driven recurrent state. It verifies stationary population counts, full-avalanche counts, the maximum of total topplings, the one-toppling property and exact rational expected activity. The largest included case has \((a,b)=(5,3)\); another is \((4,4)\).

`checks/structural.py` enumerates recurrent states of the smaller auxiliary graph with a separate burning implementation, reconstructs maximizing original configurations, independently verifies their recurrence and actual toppling vectors, and solves the original reduced-Laplacian Green-function equation using exact rational Gaussian elimination. It uses the same ten size pairs.

Observed completion markers: `EXHAUSTIVE_FSC_OK 10` and `STRUCTURAL_GREEN_OK 10`.

Finite tests do not establish the general theorem without the stated proof. No external independent validation or certificate is asserted.
