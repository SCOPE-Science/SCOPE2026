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

# Reproducibility and scope of checks

`verify.py` is a complete standalone Python 3 script that uses only the standard library. From the directory containing the script, run `python3 verify.py`. The expected successful line is `VERIFY_OK exact_rational_checks=287`.

The script builds matrix exponential coefficient series over exact rational numbers; combines the two noncommuting matrix exponentials in the correct order; multiplies by the branching growth exponential; and integrates coefficient-wise to form the clonal covariance jet. In dimensions two through five and several rational drift configurations it checks the first, second and third jet identities, exact inversion of nonzero skew coefficients under diagonal simple-spectrum damping, the full Lyapunov normalization and the spectral-gap inequality. Further checks cover two positive-definite non-diagonal damping matrices. For repeated eigenvalue examples it compares the rotation and no-rotation series through degree twelve, checks the positive entropy-production quadratic form, and verifies equality in the sharp inverse Lipschitz bound for dimensions two through seven.

The finite tests do not establish an all-dimension theorem or identity for every time; the accompanying exact algebraic proof does. The program does not estimate derivatives from noisy observations, simulate a population, perform an independent literature audit, or claim independent mathematical validation.
