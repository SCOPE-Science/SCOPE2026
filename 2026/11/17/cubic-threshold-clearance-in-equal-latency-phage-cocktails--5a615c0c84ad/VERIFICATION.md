---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS — At alpha=sum k_i d_i/m_i, the retarded linear system is triangular with a simple zero and stable -mu,-m_i roots. On the compatible-history center manifold I=Bu+O(u^3), Q_i=r_i[1-(A_i/m_i)u+(A_i/m_i)^2u^2]+O(u^3) once K=0; the convolution identity removes the quadratic I correction and delayed state deviations are O(u^3). Substitution gives u'=−C u^3+O(u^4), C=sum k_i d_i A_i^2/m_i^3>0 unless all A_i=0. Stable-foliation tracking plus the exact log S identity exclude an exponentially decaying positive history, giving sqrt(t)S→1/sqrt(2C) and the claimed ratios. If all A_i vanish the equilibrium line (u,Bu,r_i) proves non-isolation. Independent SymPy expansion for two-strain positive witness gives (1+u)^−1+(1−u)^−1=2+2u^2+O(u^4), C=2, rate coefficient 1/2. Local compatible positivity and n=1 exceptional boundary are explicit.

## originality

PASS

PASS best-of-knowledge — The earlier critical-dose result treats nonzero quadratic kappa only and explicitly excludes kappa=0; this claim resolves that excluded zero-coefficient regime by a positive cubic sum and a t^−1/2 clearance profile, not a parameter restatement. The Bardina model and strictly hyperbolic dose criteria are prior, and the equilibrium curvature alone is not the full DDE center-manifold law.

## value

PASS

PASS — The codimension-two cancellation is feasible with strictly positive two-phage parameters and changes the biologically meaningful clearance exponent from t^−1 to t^−1/2. The exact sum-of-squares coefficient and continuum-equilibrium alternative close a mathematically natural criticality boundary in the actual nonlinear delay model; this is beyond a routine stability eigenvalue calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
