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

# Finite verification and analytic limits

The analytic certificate is the complete proof in `RESULT.md`: chain lengths are explicit, the odd-chain parity imbalance bounds every coupling, and the adjacent-pair involution attains that bound. No numerical step is required for arbitrary real distances.

Running `python3 checker.py` in Python 3 with only the standard library gave `PASS 9867 exact rational and exhaustive finite checks`. The checker exhaustively enumerates every permutation coupling of equal discrete-uniform marginals for grid orders 2 through 8, checks the explicit optimal involution on all rational grid distances through order 128, and checks rational bounds for fractions with denominators through 59. By finite-dimensional Birkhoff–von Neumann, the exhaustive permutation maximum is the discrete transportation maximum.

The finite tests are not a proof for irrational distances or all positive integers. Those statements follow from the measure-theoretic argument, which is what was reviewed. No independent external validation was performed.
