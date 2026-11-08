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
# Reproducibility and limits

Run `python verify_two_locus.py` with Python 3, SymPy and mpmath installed. The run completed and printed `TWO_LOCUS_EXACT_DENSITY_AND_CRITICAL_SCALING_OK`.

The script verifies conservation of the two pair masses and of the weighted sum, the fiber reduction, the exact polynomial-antiderivative evaluation of the conditional-convolution density, symmetry, the symmetric Beta special case, the center value, first endpoint coefficient, and the critical boundary-layer formula. Numerical quadrature at four rational coefficient pairs tests both total mass and the conditional convolution; the latter uses an explicit loose bound only because the integrand has finitely many kinks.

The proof in `RESULT.md` establishes the infinite statements. Symbolic algebra is a check of particular finite identities, and finite quadrature cannot certify distributional convergence by itself. No independent audit has been performed. No prior literature priority beyond the cited inspection is certified.
