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

# Reproducibility and verification

The proof in `RESULT.md` is analytic; code is a finite corroboration only. Running `python checker.py` with Python 3, SymPy and mpmath verifies (i) the polynomial upper first integral for integer orders 1–6, (ii) the leading coefficient of the polynomial return equation for orders 1–6, (iii) the lower first integral for orders 1–6, and (iv) the positive, contracting unique return at two high-precision radii for orders 1–5.

On the checked package: **18 exact symbolic identities and 10 high-precision return tests passed**. The program uses bisection at 75-digit working precision. The analytic proof separately checks the coefficient from the involution difference, the two crossing speeds, the summability of the quadratic correction, and the higher-order partial-sum asymptotics. None of the finite experiments are treated as a proof of the infinite-time limit.

Three additional original-time numerical stress tests of the explicit polynomial example at \(c=1\) and \(K=4\) yielded the following late-time normalized values:

- At mismatch order \(2\), after 50,000 circuits, \(r_n\exp(t_n/4)\approx0.1229097050\), compared with \(0.1229072499\) after 10,000 circuits. The theoretical assertion is convergence to a positive initial-dependent constant, not a specified universal number.
- At order \(4\), after 200,000 circuits, \(t_n r_n^2\approx1.996177688\), approaching the exact predicted limit \(2\).
- At order \(6\), after 200,000 circuits, \(t_n r_n^4\approx0.998948426\), approaching the exact predicted limit \(1\).

These late-time decimal checks were carried out by solving the unique positive implicit-return equation and adding the exact circuit time \(3r_n+r_{n+1}\). They support, but do not substitute for, the infinite-series and reciprocal-power proof. The source paper's separate claim of infinite arrival time is attributed as prior evidence.
