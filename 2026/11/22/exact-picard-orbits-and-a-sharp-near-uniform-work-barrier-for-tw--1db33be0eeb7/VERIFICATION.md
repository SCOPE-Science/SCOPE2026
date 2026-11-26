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

For the stated exactly mass-preserving predictor and mean-value gradients, Gram elimination gives G_p(mu+z)=mu+w+(ρ²−r²)(w+z)/||w+z||², with determinant ||w+z||²/4. The initialized orbit is radial with t_{j+1}=(rt_j+ρ²)/(r+t_j), positive t_j, and Cayley coordinate (t_j−ρ)/(t_j+ρ)=κ^{j+1}. A nonsingular fixed point is feasible by the discrete chain rule. For r>0, z−w is parallel to z+w with proportionality not equal to one, so z=±ρw/r; the negative root is excluded exactly at r=ρ, and Cauchy–Schwarz gives the nearest positive root. At r=0 the initialization has rank one but the entire target sphere consists of nonsingular fixed points. For r<ρ, a=−κ, even j passes iff a^{j+1}≤ε/(2−ε) and odd j needs the smaller threshold ε/(2+ε). An even candidate attains the lower bound for any successful j up to two updates, and −log a=2r/ρ+O((r/ρ)^3), proving the sharp coefficient. The first iterate is (r²+ρ²)/(2r). On u⊥, J²=−I, so the explicit RK predictor polynomial is (1−h²)(I+hJ); r/ρ=2√2|h−1|+O((h−1)²), giving the singular start and coefficient 1/(4√2) times the stated logarithm. The frozen count uses distance to the selected limit, not the residual tolerance of Pu–Ran Algorithm 1. Replay: checker.py lines 9–73 (rational radial Gram, branches and singular start), 76–92 (finite stopping cases at ε=0.1), 95–110 (predictor, not the Gram solve at h=1). Inspected but not executed; CHECKS.txt records 1,044 rational, 12 stopping and 16 oscillator checks. No finite-precision or outer accuracy guarantee follows.

## originality

PASS

The correction method, Cayley solution of a scalar fractional-linear recurrence, and exact radial normalization are not new. The distinct claim is the exact branch selection and nonuniform work of a specified Gram iteration, with the singular finite-step RK witness. The strongest inspected source for the algorithm specifies neither those global inner dynamics nor a complexity theorem that covers this degeneration.

## value

PASS

The theorem diagnoses a genuine numerical limitation not visible from existence of a nearby feasible corrected solution: the selected endpoint stays bounded while the actual initialized solver makes an arbitrarily large excursion and takes order ρ/r iterations at fixed accuracy. An explicit, valid conservative ODE predictor can reach the singular state at a finite step. This makes the branch and work distinction useful for implementing or safeguarding such corrections; the example does not purport to show accurate integration at that large step.

The dated certificate retains the supplied scientific assessment, sources and limitations.
