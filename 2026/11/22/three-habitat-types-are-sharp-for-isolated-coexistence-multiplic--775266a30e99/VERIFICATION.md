---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

At a positive equilibrium the two weighted totals U,V are nonzero and the stationary equations solve locally and globally for the occupancies: vacancy p_i/(1+h_iU+k_iV), species occupancies h_iU and k_iV times that vacancy. The two linear consistency equations in w_i=1/(1+h_iU+k_iV) ensure the same totals are recovered, so this is a continuous bijection with continuous inverse on the positive equilibrium set. For n=2 independent coefficient rows fix both w_i; independent denominator rows then fix U,V, and dependent rows leave a line through any positive solution. Proportional consistency rows either are inconsistent or coincide. The resulting single equation has strictly negative partials, so at every positive solution it has a local curve; this covers n=1 as well. In the three-type example the two linear equations in 1/(1+U+V) and the sum of the other reciprocals force U+V=3 and the reciprocal sum 20/99. On 0<U<3, denominators never vanish; clearing them gives (U−1)(U−2)=0. I independently rebuilt the equilibria with rational arithmetic, checked feasibility and all stationary residuals, differentiated the full ODE in blocks, and computed characteristic coefficients by traces of powers. Both factorizations and the Routh minors in the finding were reproduced. The Routh first columns have no zero entries and signs (+,+,+,+,+) and (+,+,+,+,−); the remaining two eigenvalues are both −1. Thus the points are respectively a hyperbolic sink and a saddle with one unstable direction, and the invertible Jacobians and interior inequalities give persistence under small rank-one parameter perturbations by the implicit function theorem. Replay: python3 /workspace/reproductions/habitats3.py. The uploaded checker was inspected but not executed.

## originality

PASS

The ecological occupancy equations themselves are closely anteceded: the primary two-habitat ODE examined has this structure with general colonization inputs. Its existence and persistence statements do not prove the isolated-equilibrium count or give the three-type construction. A shared-kernel uniqueness result is not equivalent to independently factorized kernels. The exact matching indexed record is the frozen finding itself. The pass is for the sharp threshold and robust exact witness, not for the underlying occupancy model or rank-one reduction in isolation.

## value

PASS

The natural simplification to species-specific separable colonization raises an ecological modeling question: how much habitat heterogeneity is needed to allow more than one isolated coexistence state? The exact low-type obstruction explicitly separates multiplicity from fine-tuned continua, and the three-type witness with one unstable branch shows multiplicity that is robust rather than a degeneracy or a numerical near miss. This is a meaningful sharp threshold without any claim of two stable coexistence states.

The dated certificate retains the supplied scientific assessment, sources and limitations.
