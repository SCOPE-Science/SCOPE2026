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
# Verification notes
The exact proof reduces the Euclidean obtuse-angle event to a comparison of independent positive quadratic forms; integrates their independent \(\chi^2_2\) radial parts; symmetrizes two iid angular variables to prove strict monotonicity; and controls the singular endpoint of the large-anisotropy integral by uniform Taylor bounds. Both asymptotic constants are obtained analytically.

Execute `python verify.py` with NumPy and SciPy installed. The verifier uses a deterministic seed; checks the isotropic identity; compares independent one- and two-angle quadratures at six ratios; compares each probability with direct simulation from three Gaussian vertices; checks the quadratic susceptibility at three near-isotropic ratios; and checks the high-anisotropy leading constant at three large ratios. The executed result was:

`VERIFY_OK exact_isotropic=1/4 quadrature_symmetry_cases=6 direct_triangle_simulations=1200000 local_quadratic_cases=3 large_anisotropy_cases=3 tail_coefficients=0.557181082,0.555263645,0.554280283`

These are numerical tests and do not certify global inequalities or asymptotic limits. Those follow from the analytic identities in `RESULT.md`. No third-party source text is reproduced in the package.
