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

# Verification and limits

The analytical arguments in `RESULT.md` use the exact two-state recursion and a Yule–Walker elimination for stationary covariance. Differentiation produces an explicit quartic numerator and a rational turning-point function. The derivative of that function factors into a positive factor times \(a^2-2a-2\), establishing the unique threshold. The multidimensional example is certified by the three rational derivative signs displayed there.

Run `python verify.py` with Python 3 and only its standard library. The checker directly solves the three scalar linear equations for a symmetric stationary state-space covariance on rational parameter grids, checks agreement with the independently written rational formula and derivative, checks stationary positive definiteness, and reproduces the exact eleven-dimensional sign certificates. It also runs two fixed-seed Gaussian trajectory checks; these are finite simulations, not proofs of stationarity or global optimality. An example replay is recorded in `CHECKS.txt`, ending with `PASS: 299 checks`.

The proof is for finite-dimensional SPD quadratic objectives, fixed damping equal to the minimum eigenvalue, independent Gaussian velocity increments of variance proportional to the step, and strictly Schur-stable steps. Outside these conditions no theorem is asserted. Neither a human nor an independent external review is represented by this document.
