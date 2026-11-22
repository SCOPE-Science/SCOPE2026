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

# Reproducibility and proof verification

The result is an all-parameter analytic statement for real \(\alpha>-1\). The supplied `check.py` uses Python and SciPy to test the beta-identity constant, nine independent exponents, quantitative scaled tails, critical Fourier multipliers, logarithmic cusp, and positive-weight moments. Run with `python check.py` after installing a recent SciPy distribution. The result of the tested checker is `PASS 58 finite diagnostics; all-parameter conclusions remain analytic`.

Critical exact steps that do not depend on finite diagnostics: the Fourier positive/negative-frequency representation of the harmonic projection, reproducing normalization, dominated convergence in the rescaled tail, real and complex beta integrals, the cosine-integral Abelian formula, the \(\beta=2\) logarithmic split, and the Parseval/Beta-prime evaluation of the horizontal second moment. The numerical tests are consistency checks and not proofs for infinitely many exponents.

Scientific limitations: the frequency asymptotics hold for each fixed exponent and are not asserted uniform near the critical exponent; the result does not generalize to nonpower vertical weights or higher dimensions. Historical coverage by uninspected or inaccessible publications remains possible. External independent review has not been performed.
