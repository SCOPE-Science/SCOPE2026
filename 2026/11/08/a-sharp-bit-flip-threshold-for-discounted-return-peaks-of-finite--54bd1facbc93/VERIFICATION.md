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
# Verification and reproducibility

Execute `python verify.py` from the directory containing the extracted files. Only the Python standard library is required.

The checker constructs the full stochastic transition matrix exactly over rational numbers, inverts \(I-\alpha P_\varepsilon\) exactly, and compares every Green diagonal entry. Its coverage is \(N\in\{2,4\}\), \(\varepsilon\in\{0,1/4,1/2,3/4,1\}\), and \(\alpha\in\{1/3,3/4\}\), totaling 20 exact resolvents. It checks the stated maximum sets, gaps, and affine parameter-complement duality, plus ten exact rational evaluations of an \(N=2\) formula. A separate character check tests 12 modulus–probability families.

Observed run output:

`VERIFY_OK exact_resolvents=20 symbolic_N2_identities=10 Fourier_tests=12 gap_bounds=1 affine_duality=1`

The printed `symbolic_N2_identities` field names exact rational evaluations of a displayed identity, not a computer-algebra proof for all parameters. All-modulus correctness follows from the analytic Fourier inversion and conjugacy argument in `RESULT.md`. The verification is not independent certification and does not establish historical priority.
