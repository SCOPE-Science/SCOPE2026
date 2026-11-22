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

The derivation in RESULT.md uses an exact area Jacobian, an exact Gaussian-curvature identity, a two-root coarea transformation, elementary quadratic-form endpoint and saddle asymptotics, and an explicit algebraic inverse. All quantifiers require \(a>b>c>0\) and ordinary normalized Euclidean surface-area sampling.

The included `check_curvature.py` requires Python 3, NumPy and SciPy. Running `python check_curvature.py` yielded `PASS 124 diagnostic assertions`. It independently compares the induced surface-area Jacobian with finite-dimensional tangent cross products, evaluates CDFs against a Sobol-weighted sphere quadrature, confirms the endpoint-density constants, checks Gauss–Bonnet mean curvature, and reconstructs axes for four sample ellipsoids. These finite numerical checks do not prove analytic asymptotics, eliminate historical priority risk, or constitute independent mathematical certification.

External independent mathematical audit: not performed.
