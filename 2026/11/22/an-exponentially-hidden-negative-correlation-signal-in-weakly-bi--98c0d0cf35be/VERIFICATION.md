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

# Reproducible verification

Execute `python check.py` with Python 3, SymPy, NumPy, SciPy and mpmath. The program separately reconstructs the column generator, the exact stationary law, its characteristic polynomial, the weak-bias sine and cosine amplitudes, direct matrix-exponential lag correlations for three parameter sets, exact extrema formulas, and arbitrary-precision convergence of the logarithmic negative-amplitude law. It finished with all assertions passing.

The numerical checks cover selected finite parameters only. They do not certify an all-parameter mathematical assertion; the analytical proof in `RESULT.md` supplies that assertion by algebra, the continuous-time Markov semigroup and elementary trigonometric extremum analysis. The numerical limit checks are consistency evidence rather than an independent proof of the limit. Historical literature priority remains subject to external review, including an inaccessible relevant older full text.
