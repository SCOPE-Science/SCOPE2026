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

# Verification record

## Checks performed
The exact-state recurrence in `checks/verify_exact.py` was independently compared against an unoccupied-vertex bitmask dynamic program on the labeled graph for \(2\le n\le7\). All outputs agreed as exact rational fractions. The symbolic verifier `checks/verify_asymptotic.py` checked the rational one-tag and two-tag bounds with SymPy and computed illustrative probabilities for \(n=10,20,50,100,200,400\). Both scripts completed with PASS outputs from this package's source contents.

## Proof/computational boundaries
The all-size assertion and sharp \(3/4\) limit are established by the proof in RESULT.md, not by finite enumeration. The exact recurrence counts all feasible edges per reachable aggregate state and the independent mask enumeration exhausts sizes up to seven only. No Monte Carlo or timed-out calculation is used as a theorem. No independent external scientific audit has been performed.

## Execution
From the package directory, use `python checks/verify_exact.py` and `python checks/verify_asymptotic.py` with a Python 3 environment containing SymPy for the second check. The first checker uses Python's standard library only.
