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

# Verification record

The included `checker.py` was executed directly and its actual stdout saved as `checker.log`. The script asserts strict checkerboard signs for several rational finite-product cyclic convolution inverses, exhaustively checks centered-ball convolution monotonicity across a range of finite even cycles, and independently compares high-precision Fourier inverses of the circular heat covariance against direct matrix inverses. Actual recorded counts are 3,759 rational-spectrum assertions, 33,626 finite-arc assertions, and 2,189 high-precision heat checks, totaling 39,574 passing checks. Run `python checker.py` with installed SymPy and mpmath to reproduce them.

The universal result for all integers and positive real parameters depends on the analytic proof in RESULT.md: theta product, exact one-factor inverse coefficient, centered-ball cyclic convolution, infinite-tail convergence, and odd/even folding. Numerical tests do not establish universality. The checker excludes extremely small values from numerical sign comparisons when they fall below an explicitly specified threshold; the proof does not. No independent audit has been performed.
