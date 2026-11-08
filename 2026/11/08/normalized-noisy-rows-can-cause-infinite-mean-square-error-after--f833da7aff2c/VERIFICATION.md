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

# Reproducibility

Run `python checks.py` with the Python standard library. The script tests the finite, exact forced-row-selection identity, the regular-polygon two-angle Jacobian for integer batch counts, normalization and noiseless second row, and quadrature of the Poisson-kernel mean. It also evaluates the derived ridge error bound and conducts a finite-sample sanity check. A successful program exit does not by itself establish the divergent expectation.

The non-computational proof uses a strictly positive angular density, a one-dimensional antipodal cancellation tube for \(N=2\), a rank-two inverse-function chart for \(N\ge3\), the tail-integral criterion for \(\|v_N\|^{-2}\), and the strong law. For the stabilized step, the separate bound uses \(\|DT_\lambda\|\le4/a^2\) on a high-probability neighborhood, coordinatewise Hoeffding and deterministic regularization bias.

No independent mathematical audit has been performed. This does not certify a global iterative convergence claim or historical uniqueness.
