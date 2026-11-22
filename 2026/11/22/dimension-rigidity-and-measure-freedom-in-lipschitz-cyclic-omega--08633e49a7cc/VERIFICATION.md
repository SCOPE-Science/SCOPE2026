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

Execute `python3 verify.py` (Python 3 standard library only) beside the files. The program exhaustively checks finite binary-cylinder addresses, preservation of first-difference depth under addition modulo powers of two, exact rational separation inequalities, the global Lipschitz bound for the corresponding finite odometer approximants, the zero-dimensional model's exact scale formula, small cyclic rescalings, and an exact 96-step full orbit of a finite three-fibre triangular interpolant.

The acceptance test is not based on code output alone. The infinite proof in RESULT.md establishes: cyclic onto restrictions of a globally Lipschitz triangular map; dimension monotonicity; uniform bi-Lipschitz control of the binary adding machine; fractal dimensions and positive finite Hausdorff measure of standard Cantor sets; zero-dimensional variable contractions; global Lipschitz extension and interpolation; dense orbit realization; and the similarity law for prescribed measure ratios. Finite enumeration cannot prove those statements for all dimensions or levels.

Limits: all dimensions are with the Euclidean metric; the base omega-limit must be a finite orbit; no prescribed uniform Lipschitz constant, arbitrary section shapes, global attractivity or smooth realization is claimed. No independent review or external audit is claimed.
