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

# Verification instructions and limits

Run `python3 verify.py` from the directory containing this file. The program uses only Python 3 standard-library modules and reports **2,843 supplementary checks passed** on successful execution. It computes eigenvalue clipping with a symmetric Jacobi algorithm, compares explicit Fréchet differentials against finite input perturbations, tests algebraic row-profile identities and optimizing roots at sampled dimensions, and samples the asymptotic expansion. Its random examples use a fixed numerical seed for reproducibility.

The complete mathematical argument for arbitrary dimension and all symmetric perturbations is in `RESULT.md`: simple-eigenprojector differentiation; independent-entry dual maximization; Cauchy–Schwarz sharpness; unique one-variable optimum; nonsingular finite-pair limit; and Frobenius nonexpansivity. Finite numerical checks, no matter how numerous, do not certify universal quantifiers or historical priority. No claim of external or independent validation is made.
