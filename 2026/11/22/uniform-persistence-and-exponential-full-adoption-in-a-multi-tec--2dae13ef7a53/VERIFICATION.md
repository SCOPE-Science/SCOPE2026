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

The proof in `RESULT.md` establishes the all-size and all-time inequalities analytically. To reproduce supporting checks, run `python verify_mate_persistence.py` from the extracted package with Python 3 (standard library only).

The checker constructs local column-stochastic switching matrices with independently varying opinions, verifies 6,300 exact rational four-step adopter-row lower bounds over two through six technology types, and checks 738 numerical path and decay inequalities on a full two-community, three-technology MATE example with nonzero adoption feedback. State conservation and opinion floors are also tested. These computations neither exhaust admissible parameters nor replace the mathematical proof. The constants are sufficient, not optimal. External independent audit has not been performed.
