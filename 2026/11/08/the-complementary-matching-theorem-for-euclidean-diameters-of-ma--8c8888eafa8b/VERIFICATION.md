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

# Reproducibility and verification limits

The complete unrestricted proof is in `RESULT.md`. The standalone standard-library Python checker `verify.py` checks every feasible size/overlap orbit for dimensions from \(2\) through \(50\), and separately checks all individual vertex pairs in dimensions from \(2\) through \(9\). It uses exact `fractions.Fraction` arithmetic. Successful execution prints:

`PASS 506298 exact assertions; entire size/intersection orbit space n=2..50; direct vertex pairs n=2..9`

The finite range is not an infinite certificate. The unrestricted claim follows from the algebraic expressions and derivative sign comparisons in `RESULT.md`. The value \(N=2\) is included as a boundary case, and odd/even cases are verified independently. No separate human or institutional independent mathematical audit has been performed.
