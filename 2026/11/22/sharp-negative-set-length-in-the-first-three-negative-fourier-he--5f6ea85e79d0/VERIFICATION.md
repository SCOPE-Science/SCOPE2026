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

The scientific statement, Fourier normalization, proof domain, exact inequalities, and reduction from three Hermite modes to the one-parameter quartic are in `RESULT.md`. `verify.py` is a standalone Python 3 standard-library script requiring no input files or network access.

Running `python3 verify.py` checks, using exact rational arithmetic, both Laguerre-basis polynomial identities; six parameter strips with every listed closed interval and every endpoint Bernstein sign; the square-root length inequalities by integer square roots; the positive unbounded parameter tail; the five algebraic Bernstein coefficients on an interval with endpoints in \(\mathbb Q(\sqrt{105})\); and exact polynomial remainders at algebraic roots. These checks support the sign claims uniformly in each real parameter interval by affine interpolation of Bernstein coefficients.

The proof's Fourier-transform identity follows analytically from the Laguerre generating function and Gaussian Fourier formula. Strict enlargement of the negative set at the fixed roots follows by continuity. Computation is a finite exact certificate, not a substitute for either of those steps. The conclusion is restricted to the displayed three-dimensional real space and initial-value constraint. No independent mathematical audit has been performed.
