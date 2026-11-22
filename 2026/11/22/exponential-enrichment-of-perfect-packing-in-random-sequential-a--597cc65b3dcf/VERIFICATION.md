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

# Reproducibility

Run `python CHECK.py` from the directory containing this file. It independently enumerates all possible priority permutations on the open two-row ladder through four rungs. Expected exact probabilities are `1, 1, 7/9, 3/5` for lengths `1, 2, 3, 4`. It additionally calculates midpoint discretizations of the displayed non-selfadjoint transfer operator and checks the rigorous coarse eigenvalue bounds.

The spectral numbers are estimates, not rigorous enclosures. Exhaustive permutation enumeration is only valid for the explicitly checked finite sizes. The all-length claim uses the event integral, the positivity-improving compact square of the operator, the Perron–Frobenius–Jentzsch gap and coordinatewise association/disjoint-block estimates. The static enumeration follows from the Fibonacci recurrence.

No external or independent scientific audit has been performed.
