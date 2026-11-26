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

With w fixed at the design point, the thinned Poisson intensity has log-derivatives (1,(x/sigma)^2). Integrating their outer product gives the stated 2-by-2 matrix; substituting the budget leaves F(a)/(a+kappa)^2. F>0 by strict Gram positivity, and differentiating the Gram determinant gives the rescaled kernel for aF'(a). For x=log a, the negative exponential term in the joint log kernel has negative diagonal Hessian entries and determinant 2 exp(4x)(1-u^2)>0 on the convex support 0<u<1. Prékopa applies first to the u-integral and then to the cumulative integral (multiply by the indicator of y<=x on the joint (y,x) space), so log F(exp x) is concave. The derivative E is nonincreasing; any failure of strict decrease would give a constant interval and by analyticity a global constant. The endpoints exclude this: F=(4/45)a^6+O(a^8) with analytic remainder, and the limiting Gaussian moments give F->pi with aF'->0. The log-objective derivative multiplied by a crosses zero exactly once, including kappa=0; increasing kappa strictly lowers the comparison term at a fixed a, shifting the root right, and no bounded root is possible as kappa tends to infinity. Independent high-precision direct moment quadrature and objective differentiation give a_0=2.483403229461727769, edge detection probability 0.0457920034599350, a_1=2.744175332913743488 and a_5=3.166331990571762460. Replay: python /workspace/branches/reproduce_frozen.py (transect section). The frozen checker and verification notes were inspected, not executed; finite diagnostics do not prove monotonicity. The proof uses exactly the complete marked Poisson likelihood, nominal scale and the stated cost law, not counts alone or density-only estimation.

## originality

PASS

Best of current knowledge, the distinct contribution is the exact all-kappa joint-information design, including rigorous monotonicity, global uniqueness, and its minimum-width endpoint. The observation model and log-concavity theorem are not new; the verified analogous truncation work uses a different risk. No external access limitation is treated as noncoverage.

## value

PASS

For the standard half-normal detection model, joint scale/intensity inference has a real effort-versus-information tradeoff: extending width changes both the number and leverage of the recorded distances while using budget. The strict global law and universal zero-base-cost lower bound determine the design without a grid or a guessed effective strip width and are interpretable in nominal scale units. This is an exact local-design benchmark, not a generic field recommendation or a density-only efficiency claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
