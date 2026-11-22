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

The companion `VERIFY.py` independently constructs exact finite Dirichlet Gram-moment traces and verifies them against the degree-eigenvalue trace and trace square. It also checks the closed cubic spectral coefficient, sign of the logarithmic fifth-order remainder, and fourth-order scalar convergence on representative parameter grids. Observed result: 10 exact rational checks and 108 scalar expansion checks passed.

These finite checks do not prove an infinite-dimensional Schatten limit or exclude an unknown prior theorem. The proof rests on the exact centered product representation, the inverse-hyperbolic-tangent expansion, and exponentially summable Gaussian tails. The reviewed statement is restricted to fixed positive diffusion times and fixed Dirichlet parameters. Independent audit: not performed.
