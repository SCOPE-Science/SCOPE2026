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

The analytic proof in `RESULT.md` derives exact row norms, summability of nuclear rank-one rows, invertibility of the real-linear map, and the ball inclusions for the entire range \(0<\tau<3\). The critical nonattainment implication uses a two-sided coordinate perturbation and the complex parallelogram identity. Infinite nonvanishing of moments for every nonzero finitely supported sequence follows from the lowest-index dominant exponential. This step is proved for all \(k\) asymptotically, not inferred from tests.

`check_finite_profiles.py` is a standalone Python 3 standard-library exact-rational checker. Its expected successful output is `MOMENT_KERNEL_RATIONAL_CHECK_OK 450`. It tests selected finite row sums and finite moment profiles. These checks cannot certify the statement for every \(\ell_1\) functional or every parameter, and no independent mathematical audit has been carried out.
