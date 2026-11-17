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

# Verification and limitations

The exact quantitative claim was checked by reconstructing finite-atomic duality, Hilbert orthogonality, the sub-Hilbert power-mean inequality, the super-Hilbert atom-cost optimization, equality characterization, central-symmetry diameter, and the asymptotic expansion. The calculation holds for real and complex Hilbert spaces, all positive atom weights, zero original coefficients, all \(1<p<\infty\), and every \(R>1\). Its norm-preserving endpoint \(R=1\) is the singleton extension.

Supplementary `checks/verify.py` performs reproducible finite arithmetic stress tests with a deterministic pseudorandom generator and analytic extremizing choices. It checks 36,288 individual assertions; its random sampling cannot certify an infinite theorem. The mathematical proof appears in `RESULT.md`.

The literature comparison distinguishes the new exact tolerance-dependent diameter from qualitative property-preservation theorems. An older exact equivalent under alternative Chebyshev geometry terminology remains a priority risk. There has been no independent audit.
