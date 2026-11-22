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

# Computational and analytic checks

`VERIFY.py` runs with standard Python 3, constructs the two weighted finite-state automata from their rules, and computes their exact characteristic coefficients via Newton identities. It enumerates all \(9^n\) input states independently for \(n=3,4,5,6\), replays the synchronous cellular automaton, and compares first-all-rest times with the trace formulas. It computes the formulas through \(n=12\) and checks all reported values. Captured actual output: `CHECKS.txt`.

The formal all-length proof is the local exclusion of any excitation at or after update three, the exact five-site initial trigger for update-two excitation, and the derivation of both finite transition matrices and their determinant identities. Exhaustive checks at finite lengths alone cannot prove the infinite-family statement. The small-width circular overlap cases are included in the analytic transfer-matrix interpretation and separately tested.

No external/independent mathematical audit has been performed. No claims are made for different contact thresholds, alphabet sizes, update schedules or graph families.
