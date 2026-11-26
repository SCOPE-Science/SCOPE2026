---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The boundary Jacobian is triangular, with transverse entry cx; tangent–transverse mixing does not change the product of the transverse diagonal entries. Under x=4 sin²(πθ), the starting law is the stated arcsine law and evolution is a factor of angle doubling. For X=2−2 cos(2πθ) the invariant-measure transfer operator P gives PX=2. For Rf=P(X²f), R1=6+2C and RC=−4−4C with C=cos(2πθ), by keeping only the even cosines before halving frequencies. The trace 2 and determinant −16 and initial moments 1 and 6 give the recurrence, two-root formula, and positive relative variance exponent. As a fresh check, writing the product as the squared modulus of the finite Thue–Morse polynomial, the sum of squared finite aperiodic autocorrelations gave 6,28,152,752,3936,19904,102784 for n=1,…,7 and the coefficient-square sums gave 2^n. Log X is in L² with mean zero and cosine coefficients −2/k, so matching frequencies under doubling gives covariance π²/(3·2^m). Counting lag pairs gives the finite variance. The reverse martingale difference d=2φ−φ∘D has Pd=0, variance π², and the sum differs from Z_n by a uniformly L²-bounded endpoint term; the ergodic reverse martingale CLT applies. Birkhoff gives the almost-sure exponential rate; the CLT and the shift n log c_n=κ√n give Φ(κ/π). These are claims about a linearized boundary cocycle, not finite-density invasion. The frozen code was inspected but not executed.

## originality

FAIL

Defaveri–Smith give both the exact logarithmic covariance at every lag and the polynomial tilted operator for the same arcsine logistic orbit. Their stated eigenvalue alone would not fix the finite prefactor, but their explicit operator and invariant polynomial span mechanically give the full first and second moments, not just their leading rates. Stationary lag counting and a threshold shift of the known CLT then cover the other quantitative claims. The new transverse label does not change this calculation.

## value

FAIL

The annealed versus quenched distinction is a meaningful way to interpret transverse neutrality, but here the predator-free derivative simply multiplies the same logistic observable already examined in the prior work. Both moment rates and every finite-horizon law claimed here follow from its exact calculations or the known limit theorem. No independent nonlinear invasion statement, new observable, or surviving exact invariant is established, so the interpretation alone does not repair the claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
