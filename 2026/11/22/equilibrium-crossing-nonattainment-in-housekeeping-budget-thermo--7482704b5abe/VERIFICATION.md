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

Cauchy–Schwarz gives the energy-budget bound after weighting path variation by sqrt(zeta sigma). A primitive of that weight bounds variation below by the endpoint length even for backtracking. To attain equality the velocity is nonnegative off the zero and equals (L/B)sqrt(sigma/zeta); it also vanishes almost everywhere on the zero level set. Taylor's theorem at the C² nonnegative interior minimum gives a velocity bounded by a multiple of distance to c, preventing a finite crossing. Integrating the positive regularized speed gives the exact budget and E=J_epsilon K_epsilon/B, so dominated convergence proves sharpness without attainment. Comparison near c with quadratic coefficients A±delta gives the logarithmic coefficient for a nondegenerate quadratic zero only. To test the claim for all minimizing sequences, rescale any bounded-time subsequence to [0,1], where times are bounded away from zero by B/max(sigma). The transform x↦integral_a^x sqrt(zeta) turns the weighted energy into a time-scaled squared derivative norm; compactness and lower semicontinuity then give a limiting admissible optimizer, a contradiction. More generally, the separated equality-time integral is locally finite iff p<2, under the stated isolated-zero power law and continuity/positivity away from c; its inverse gives an absolutely continuous path when finite. For the ring, differentiating stationarity at zero gives pi'=(-2,1,1)/9 and the clockwise current derivative 1/3. The cycle affinity is 3 lambda and the equilibrium score has variance 2/9 and relaxes at rate 3, giving the stated sigma and zeta expansions. The finite source code was inspected but not executed. All optimization and nonattainment conclusions concern the leading functional, not the finite-speed master equation.

## originality

PASS

The housekeeping-budget length bound and the equality law in the positive-rate geometry are not new. The distinct contribution is the sharp positive-budget crossing result where the prior entropic-time change is singular, including duration divergence for all minimizing sequences, finite admissible protocols achieving the infimum in the limit, the power-law threshold, and a physical example. The decision is bounded by the inspected primary and catalogue evidence.

## value

PASS

The positive-weight formula alone can suggest a finite optimal protocol even when the required physical time diverges. The result resolves this boundary for a physically realizable simple Markov model, distinguishes sharp infimum from an achieved optimum, and quantifies how the time required for one explicit exactly budgeted approximation grows. The critical vanishing order and all-sequence obstruction are usable diagnostics for leading-order optimization; no exact finite-speed physical guarantee is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
