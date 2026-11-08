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

# Mathematical and computational verification

The reproducible `verify.py` requires Python 3 standard library only. Run `python verify.py` with `RESULT.md` in the same extracted package; the verified result is `VERIFY_OK 196 exact rational and numeric checks`.

Exact-rational checks reconstruct all six differential equations from the paper's incidence and mixing rule, evaluate their residual at the all-positive state with \(a=1/2\), \(b=3\), \(d=3/2\), and verify the conserved total of two. The strict Perron equations, the quadratic, the reflection-block determinant identities, block Hurwitz signs, and an exact finite mixing cutoff are checked. A family of additional exact rational equilibria checks each original residual independently. Strong-migration checks at \(d=100,1000,10000,100000\) compare the finite eigenvalue and patch difference to their analytic leading constants. These finite tests are supplementary; none establishes the all-parameter and asymptotic theorems without the proof in RESULT.md.

At the exact rational example, direct full six-variable symbolic differentiation yields the Jacobian characteristic polynomial
\[
\frac{z(z+3)(8z^2+34z+5)(8z^2+34z+29)}{64}.
\]
The zero factor is the population conservation mode; the remaining modes are stable on the fixed-mass subspace.

**Proof boundaries.** The no-coexistence assertion concerns strictly positive equilibria, not possible single-strain equilibria or the global outcome of trajectories. Exponential attraction is local. The \(d^{-1}\) spectral law applies for \(a+b>2\), not at critical mean transmission \(a+b=2\). The mathematical literature comparison is best-knowledge and is not an independently verified publication-priority certificate.
