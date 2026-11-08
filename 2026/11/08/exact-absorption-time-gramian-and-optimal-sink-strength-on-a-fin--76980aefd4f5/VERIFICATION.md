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
# Verification of the finite absorbing path formulas

The standalone `verify.py` requires Python 3, NumPy, and SciPy. Run `python3 verify.py` in the directory containing this report.

Its first check constructs the proposed time-integrated survival matrix using exact rational arithmetic, forms the killed generator, and checks every entry of \(A^\dagger Q+QA+I=0\). This evaluates 4,960 independent matrix entries at all lengths from one through fifteen with four positive rational parameter pairs. It also checks the site formula and the closed uniform-initial-state average.

Its second, independent check diagonalizes the non-Hermitian generator numerically and directly integrates the exponential spectral sum over time, without using the proposed kernel or a Lyapunov solver in that integration. This validates 90 site-localized survival integrals. For the same cases, a separate SciPy Lyapunov solver reproduces the full proposed matrix and confirms positive definiteness.

Expected final lines:

```
EXACT_LYAPUNOV_ENTRIES_OK 4960
INDEPENDENT_SPECTRAL_LIFETIMES_OK 90
ALL_CHECKS_PASSED
```

The finite tests verify implementation, signs, normalization and sample parameter choices. Arbitrary system size and uniqueness of the optimal rate are proven by the all-index identities and elementary calculus in `RESULT.md`, not by extrapolating any enumeration. No independent audit has been performed.
