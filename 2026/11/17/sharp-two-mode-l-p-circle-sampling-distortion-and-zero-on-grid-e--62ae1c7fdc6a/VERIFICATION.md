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

# Reproducible verification and limits

The exact claim and its complete quantified domain are in `RESULT.md`. The proof relies on the Chebyshev Rodrigues derivative identity, strict positive-integrand monotonicity, differentiation of the mean coefficient, exact aliasing of absolutely convergent Fourier series, the Gamma reflection identity and a dominated-convergence Gamma-ratio limit. These steps are mathematical identities and inequalities; they are not inferred from tests.

Run `python CHECKER.py` with Python 3 and its standard library. The test checks the beta-integral balanced mean, normalized signed Fourier coefficients, and 21 combinations of exponents and grid sizes with 45 randomly selected complex pairs each. The recorded execution returned `TWO_MODE_CIRCLE_CHECK_OK 1005 finite assertions`. These checks cover finite examples only, and do not independently certify the infinite series, the strict extremizer characterization for all coefficients, or publication novelty.

The first public version of the motivating preprint is dated 4 November 2026. Related older literature was compared on the basis of its accessible statements. Independent validation and independent audit were not performed.
