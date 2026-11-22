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

# Verification
The source equation and assumptions are transcribed in `RESULT.md`. Run `python verification/check.py` with SymPy to reproduce exact algebraic identities, equilibria, eigenvalue characteristic polynomials, the optimal-rate equilibrium, and the rational feedback parameters. The check completed successfully on the delivered source file.

The all-time estimate follows from the exact logit derivative plus an elementary product/minimum inequality, and the critical case from uniform continuity and integrability. Exact finite symbolic verification does not replace those proofs. The stable sharpness example uses standard hyperbolic equilibrium theory and integrable logarithmic-derivative errors to show strictly positive asymptotic coefficients. The primary paper's supporting S1 material was not fully inspected; an independent scientific audit is outstanding.
