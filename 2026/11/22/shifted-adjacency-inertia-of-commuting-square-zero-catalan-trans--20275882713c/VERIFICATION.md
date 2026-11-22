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

Execute `python3 checker.py` from a directory containing the supplied standalone script. Dependencies are Python 3 and NumPy. Its output was captured verbatim in `checker_output.txt`; the final line is `VERIFY_OK`.

The checker enumerates every weakly increasing order-decreasing transformation for all \(3\le n\le10\), directly composes transformations to select the square-zero ideal and test pairwise commutation, verifies the exact integer identity \(A_n+I=XH_{n-2}X^{\mathsf T}\), and numerically compares inertia of the two stated graph conventions and of the interval matrix. All eight configurations passed; the largest square-zero set contained 256 maps. The theorem for all \(n\) is justified by the analytic row-span and Schur-complement proof in `RESULT.md`, not by extrapolating numerics. Numerical tests use floating-point tolerances, but incidence matrix identities are exact integers.

This verification does not establish historical priority, independent expert validation, or a complete adjacency characteristic polynomial. The 2012 Catalan monoid preprint and the 2021 zero-divisor paper were read as primary background; a more general interval-matrix theorem could imply the same inertia without naming the Catalan monoid.
