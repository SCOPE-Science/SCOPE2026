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

# Verification of the mathematical finding

The analytic proof is in `RESULT.md`. It independently derives the correct planar-area normalization and reduces all nonzero radial critical points to the sign equation \(h_a(x)=1/m\), where \(h_a'\) is controlled by an affine function of \(\cosh x\). It establishes the number and nature of the extrema for all integer degrees \(m\ge2\) and middle variances \(a>0\), including the tangency boundary.

Run `python CHECK.py` using only the Python standard library. The code compares independent formulas for the expected intensity, finite-differences the exact derivative of the logarithmic profile, tests the cubic critical equation and tangent condition, samples strictly subcritical and supercritical stationary root counts, and checks large-degree scaling. The actual saved candidate replay passed 149 numerical assertions. These checks do not prove an all-parameter theorem; that follows from the exact sign argument.

No computer-assisted proof system or independent audit was used. The outcome is a self-review only; publication priority and independent correctness review remain open. The result concerns the expected planar density and does not imply a typical sample has one or two rings.
