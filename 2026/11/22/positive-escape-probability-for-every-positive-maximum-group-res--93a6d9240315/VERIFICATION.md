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

The correctness argument is analytic. Its decisive ingredients are the killed Brownian Laplace transform, exact two-particle maximum transform under an exponential clock, and super-solution induction for the renewal equation. The Gaussian components are independent because they are orthogonal linear combinations of two independent centered Gaussian increments. The bound on the full absorption probability comes from a monotone limit over finitely many completed resets; Poisson local finiteness rules out any finite-time infinite-reset pathology. The positive survival event from an arbitrary starting point uses the strictly positive killed transition density. The zero-rate mean threshold is obtained from the exact reflection-principle survival formula.

The standalone checker numerically integrates the exact two-particle transform independently for four parameter triples, checks the closed critical constant, checks the finite super-solution inequality across sample points, and compares the no-reset first-passage survival with its asymptotic. Its output is limited to reproducibility diagnostics, not independent validation, uniqueness certification, or proof of asymptotic statements.

To replay: `python checker.py` with Python 3, NumPy, SciPy and SymPy. No third-party paper or external executable is required.
