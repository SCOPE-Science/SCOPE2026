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

The analytic proof uses a stationary Poisson-interval representation, exact sphere fourth moments, closed renewal equations, coefficient-ratio monotonicity, and an exact anisotropy evaluation. These steps are displayed in RESULT.md and reproduced algebraically in `verify.py`.

With Python 3 and SymPy available, `python verify.py` must print a PASS result after comparing two symbolic derivations, checking the isotropic specialization, and verifying the threshold-polynomial identities. Numerical bisection examples supplement but cannot establish an all-parameter proof. Unbounded simulation or external formal certification is not claimed.

The domain is integer spatial dimension at least two, strictly positive relaxation and redraw rates, independent complete uniform-orientation redraws, zero translational thermal forcing, and a diagonal harmonic potential. There has been no independent external audit.
