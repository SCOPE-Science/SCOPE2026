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

Run `python verify.py` with a Python 3 standard-library installation. The script has no external dependencies and tests the formulas by an separately implemented multinomial sum and actual word enumeration.

Checks performed: for every \(6\leq n\leq30\), \(3\leq q\leq14\) and \(1\leq d\leq6\), it compares the claimed \(F_d\) formula with the multinomial sum, confirms all polynomial-difference identities and strictly maximal optimizer distance. It separately enumerates all length-\(n\) q-ary received words at \((n,q)=(6,3),(7,3),(6,4),(6,5)\), counting the shared outputs of explicit two-center pairs at each of the six possible positive distances. All checks completed successfully.

For proof of the infinite theorem, consult the positive-coefficient comparison and factorizations in `RESULT.md`; these are the decisive analytic steps, not a finite-search extrapolation. No external independent review or formal proof certificate has been performed. Existing classical Hamming sphere intersection formulas and any related published optimizers need separate historical-priority evaluation.
