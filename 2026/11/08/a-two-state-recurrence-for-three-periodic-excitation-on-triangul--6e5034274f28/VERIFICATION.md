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

Using Python 3 and no external packages, in the same directory run:

```
python3 check_transfer.py
python3 check_dynamics.py
```

`check_transfer.py` explicitly enumerates successor-neighbor support on the nine local extensions, establishes the exact two-state transition, independently recomputes the full six-state transfer, and compares counts for the first one hundred chain lengths. It also tests the second-order recurrence and three-cycle divisibility. Its captured standard output is `check_transfer.out`.

`check_dynamics.py` independently builds the labelled triangular-cactus graph and updates all vertex states simultaneously according to the specified Greenberg–Hastings local rule. It exhaustively tests \(3^3+3^5+3^7+3^9+3^{11}=199287\) states at chain lengths one through five, recording initially fixed and initially primitive three-periodic states. Its captured standard output is `check_dynamics.out`.

The unrestricted theorem for all \(m\geq1\) follows from the combinatorial transfer proof and exact matrix identity in `RESULT.md`. No finite list of experiments establishes the unrestricted claim by itself. No independent external audit has been conducted.
