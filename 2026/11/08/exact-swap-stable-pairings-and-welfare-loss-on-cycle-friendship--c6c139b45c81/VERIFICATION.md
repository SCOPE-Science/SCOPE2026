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

The proof in `RESULT.md` is self-contained. For corroborating computations, execute the supplied standalone Python file using:

```bash
python3 verify_cycle_pairs.py
```

Only Python's standard library is required. The verifier enumerates all pair partitions of labeled cycles of sizes 6, 8, 10, 12, and 14, checks whether any swap is a weak/strict improvement by direct comparison of the two swapping participants, independently checks the structural characterization, and compares exact integer counts with the inclusion-exclusion expression. It additionally evaluates formula totals through 30 agents. The expected count of enumerated partitions is 146595; the stable totals for the five exhaustively checked orders are 2, 2, 7, 17 and 37. Computation cannot establish the infinitely quantified theorem; the deductive proof supplies that step.

No external independent scientific audit has been performed. The code evaluates only the indicated finite cases and is not a complete global enumeration for arbitrary input order.
