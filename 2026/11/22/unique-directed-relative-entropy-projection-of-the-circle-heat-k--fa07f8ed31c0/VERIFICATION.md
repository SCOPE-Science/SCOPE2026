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

Final file: /workspace/repairs/3/RESULT.md. Frozen line 39 falsely said the limiting quotient 2∫exp(-u-u²/c²)du increases from zero to one, then used an interior crossing of one. The limit is two, not one. The replacement supplies strict increase and a finite bracketing argument, and replaces the informal entropy-limit justification with explicitly integrable bounds on the expanding scaled interval. No theorem, constant, or checker needs to change. Re-audit: positive Fourier weights force the center and the derivative at the centered r=0 boundary is negative. At r=exp(-s), the derivative sign is that of B-A. The heat tilt decreases the geometric mean index strictly, giving (log(A/B))'>1/(1+exp(-s)); endpoint quotient limits 0 and infinity ensure one global crossing. At s=t termwise comparison gives A<B; the s crossing increases smoothly with t. The Riemann-sum quotient has the corrected limit curve with endpoints 0 and 2, proving s_t/sqrt(t)->c_* and hence the radius scale. The wrapped Gaussian scaled density lies between g and Cg on the principal interval by bounding each translated-image ratio. At s~c sqrt(t), the Poisson density is uniformly comparable to 1/(1+x²); at s=t, its ratio to sqrt(t) is comparable to 1/(x²+t). These give valid dominated convergence including at the logarithmic point x=0, and E log X²=-gamma for variance-two Gaussian. The analytic divided stationarity equation has unit r-derivative at (0,0); oddness and coefficient matching give r=q-q³+3q⁵+O(q⁷). The difference of densities is -2q² cos(2 theta)+o(q²) uniformly and the KL quadratic factor is 1/2, so the leading minimum is q⁴. Independent quadrature gives c_*=0.865503198732615861 and K_*=0.182758308669706348; at t=1e-6 direct scaled circle minimization gives s/sqrt(t) about 0.865503375 and KL 0.182758080; at t=6 the minimum divided by exp(-4t) is 0.99998771. Replay: python /workspace/branches/reproduce_frozen.py (circle section). Frozen verification and checker inspected, not executed; finite checks do not establish the limits. The repaired statement is still only for single heat inputs and forward KL.

## originality

PASS

For the final corrected proof the distinct claim is the unique all-t single wrapped-normal to freely centered wrapped-Cauchy forward-KL projection and exact information-loss law. Related model families, Fourier formulas and analogous L² calibration are established; they do not by themselves give the stated KL optimum. The proof repair does not extend the novelty scope.

## value

PASS

The repaired result gives an exact, globally unique calibration between two standard directional families for a widely used asymmetric information loss. The finite optimal KL versus divergent first-moment-matched KL is a concrete failure of a natural alternative, not a small numerical gain. It also explains why the L²-optimal scale from the same model families is not interchangeable with the information-optimal scale. The supplied bounds make the singular limiting comparison usable without appealing to finite grids.

The dated certificate retains the supplied scientific assessment, sources and limitations.
