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

# Reproducibility and verification scope

The directly executable artifact `checker.py` is the complete standalone Python 3.9+ finite-test program. Run `python checker.py` in a directory containing that file. It requires no third-party libraries, data files or network connection. The program prints `PASS: 19578 finite exact-arithmetic and complex-root assertions.` on successful completion.

The exact tests form finite-time probability laws from the renewal recurrence with coprime integer durations and rational speed probabilities. They check total probability, admissible support, the explicit limiting phase distributions, their sawtooth means, and convergence at a large sampled cycle count. Additional tests solve the implicit complex root equation near continued-fraction approximants to \(\sqrt2\) by Newton iteration and check that each root is simple, has negative real part, agrees with the stated quadratic approximation, and does not cancel in the particular mean-position Laplace numerator.

The analytical claims that require proof beyond finite computation are the exponential convergence of lattice renewal masses for all eligible parameters; the nonarithmetic weak limit for all continuous tests; existence of an infinite resonant pole sequence; and the impossibility of any exponential decay for the mean. These are established in the proof via generating-function poles, the key renewal theorem, analytic implicit differentiation and analytic continuation. The checks do not constitute exhaustive enumeration or external certification.
