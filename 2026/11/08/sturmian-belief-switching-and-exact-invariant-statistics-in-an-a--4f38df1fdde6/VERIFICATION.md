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

# Verification

Run `python3 verify.py` from the directory containing `RESULT.md`. Using only the Python standard library, the script checks 988 exact Fraction odds identities and 1300 independent rational trajectory and threshold-word observations, including the switching tie, initial conditions outside recurrent support, and rational periodic comparators. It prints `VERIFY_OK` on success and the computed special-case frequency and mean.

The infinite classifications do not follow from finite testing. The full proof in `RESULT.md` establishes the exact entrance into the interval, the rigid circle conjugacy, rational/irrational dichotomy, uniqueness and equidistribution in the irrational case, the balanced mechanical coding and strict finite-window discrepancy, the logistic integral, and a prime-factor irrationality certificate. The Lyapunov claim is restricted to points whose orbits avoid the nondifferentiable switch. Endpoints of the belief simplex are absorbing and excluded from recurrent uniqueness. The separate public source date 2023-10-26 records a descriptive interview, not the first technical preprint (2024-05-29).
