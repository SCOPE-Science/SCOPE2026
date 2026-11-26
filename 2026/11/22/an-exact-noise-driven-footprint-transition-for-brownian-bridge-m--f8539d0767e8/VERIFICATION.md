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

Reconstructed the posterior variance and global argument in RESULT.md lines 47–102. The Dirichlet inverse of −d²/dt² applied to 2t−1 gives g=t(1−t)(2t−1)/6 and Var(J)=1/180. Cubic averaging yields the stated cross covariance, and direct averaging of min(s,t)−st gives a+h/3−c²=c(1−c)−h/6 for a=c−h/2. The noisy variance is positive even at the boundary since its minimum without noise is h(4−3h)/12. With z=c(1−c), every interior derivative sign is the sign of the stated quadratic N, and N(1/4)<0. If S>0 strict concavity and endpoint signs give a unique simple crossing; if S≤0 then h≥h₀ and N'(L_h)<0, so N is strictly negative beyond L_h even at equality. The reflected centers exhaust the optimizers; the midpoint has zero reduction. The interior log derivative is strictly increasing in eta and has negative z derivative at its simple maximizing root, establishing inward motion. Implicit differentiation at threshold gives N_eta(L_h)=8(1−h)(1−2h) and dz/dc=1−h, reproducing the positive onset coefficient. Uniform convergence of eta times the objective to its numerator gives the constrained large-noise limit with maximizer z=(2+h²)/12 when h<1/2. Independent bisection of the log derivative on [7/64,1/4] for h=1/4, eta=1/5 gave c=0.196817468335539 and a relative variance-reduction gain of 27.6931016062%. Inspected verify.py, VERIFICATION.md and the printed verification output without running the supplied script.

## originality

PASS

The supported distinct claim is the exact global width/noise boundary-contact transition, its equality cases, and the subsequent center movement for one contiguous normalized average estimating this one signed bridge moment. Gaussian conditioning, Brownian polynomial moment calculus, and optimal point or multi-observation designs are not claimed as novel.

## value

PASS

A fixed nonzero footprint is a motivated measurement constraint. The optimization gives a complete boundary-versus-interior design rule across all widths and noise levels, including exact onset and a limiting location, rather than just a numerical improvement at one setting. The two optimizers and their degeneracies are fully resolved for the scalar design, without making a multi-sensor or arbitrary-prior claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
