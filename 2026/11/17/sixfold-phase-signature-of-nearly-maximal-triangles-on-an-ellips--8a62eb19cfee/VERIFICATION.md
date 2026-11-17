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
# Verification of the sixfold ellipse phase law

## Analytic checks

The proof gives a fixed-shape positive-definite area Hessian, its quadratic-region volume, arclength-density factorization, a positive normalization, and a strict covariance sign for the inverse sixth moment. The claimed convergence of the marked conditional distribution follows from \(L^1\) convergence of the *rescaled joint densities*. The scalar tail normalization is consistent with the prior density-correlation literature and is not asserted as new. The sequential flattened-ellipse limit is not a uniform joint asymptotic.

## Executable diagnostics

Run `python check.py` after installing `requirements.txt`. It independently evaluates the predicted scalar coefficient and sixth moment at \(q=0,0.35,0.70,0.92\) by numerical quadrature and compares them with normalized-area and phase-moment statistics from independent boundary-arclength rejection sampling, with 550,000 sampled triples at each parameter. The checked diagnostic completed with the terminal marker `ELLIPSE_MAX_TRIANGLE_SIXTH_HARMONIC_CHECK_OK`.

Predicted \((K(q),M_6(q))\) values: at \(q=0\), \((0.42441318158,0)\); at \(q=0.35\), \((0.41416819086,-0.00295085570)\); at \(q=0.70\), \((0.37541179558,-0.03399129556)\); at \(q=0.92\), \((0.31461783641,-0.13992218557)\). A separate stricter-threshold diagnostic with two million trials per parameter gave, at \(\varepsilon=0.007\), empirical coefficient and sixth moment \((0.37336,-0.03451)\) for \(q=0.70\), and \((0.30907,-0.12237)\) for \(q=0.92\). Monte Carlo statistical error is nonzero; these numbers only check consistency.

## Limits of verification

The script cannot prove total-variation convergence, global orientation uniqueness, strict harmonic monotonicity or historical originality. Those statements are addressed in the written proof and scientific comparison. No independent mathematical review has been performed.
