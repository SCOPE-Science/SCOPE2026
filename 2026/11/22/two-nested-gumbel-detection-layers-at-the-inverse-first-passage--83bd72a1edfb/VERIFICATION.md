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

Solving the backward equation for the potential with prescribed positive derivative forces U=log(D tau')+W up to a constant, where W'=1/(D tau'). The resulting scale density is tau' exp(W) and the speed density is -(exp(-W))'. The scale integral diverges; tail integration of the speed in the minimal Green formula gives T'=tau'(1-exp(W-W_infty)). The entrance integral at infinity is the integral of this physical slope, divergent in admissible cases because tau is unbounded, and also divergent outside by the clipped asymptotics below; infinity is natural. Substituting u=1+log(1+x) gives divergence of W exactly for a<2+delta or a=2+delta, b<=1. Outside, the power-law tail of W' gives T' asymptotic to x^(a_c-1)/(D0(a-a_c)); on the critical line the exact logarithmic tail gives x^(a_c-1)log(x)/(D0(b-1)). Integrating gives the two stated constants. With no eventual local minima, integrable speed excludes an eventually nonincreasing potential and the absence of a negative-to-positive derivative change then implies U'>=0 eventually. The resulting monotonicity of D T'+x gives D T' >= (T(x)-T(X))/integral_X^x(1/D)-x; a growth exponent above a_c would make integral 1/(D T') finite, contradicting decay to zero of the physical tail flux D exp(-U)T'. The increasing critical realization attains the bound. For detection, elementary tail integration gives Q=(kappa_epsilon/epsilon)(1+x)^(-epsilon) in the first regime and (kappa_c/eta)ell^(-eta) in the second. Solving Q=-log(h) and substituting the moving coordinates gives the two exact threshold formulas and the common Gumbel curve, exactly in the log-critical case and locally uniformly in the power-critical limit. The physical observable is the relative derivative deficit, not the total MFPT discrepancy or an experimental detection rate. RESULT.md lines 75–180 and the Lamperti reduction with y'=D^(-1/2), V=U-(log D)/2 give replayable derivations. VERIFICATION.md and CHECK.py were inspected, not executed; the finite assertions are not a proof of the boundary or limits.

## originality

PASS

Pass limited to the paired near-critical relative-slope visibility windows, with exact radii and common translated Gumbel curve. The inverse, clipping mechanism, and diffusivity-shifted admissibility via change of coordinate are not independent novelty. The closest known constant-diffusivity result gives an exact clipped cubic example, but the passages inspected do not give a parameter approaching either of these two boundaries with observation distance moving on the corresponding scales.

## value

PASS

The value is the quantitative answer to how far an inadmissible inverse can mimic a target even when the true large-distance behavior is different. Comparing detuning at the power threshold with detuning at the marginal logarithmic threshold exposes genuinely different spatial scales (single versus double exponential) for the same fixed relative slope deficit. The exact radii and common crossover quantify noncommuting limits and are useful beyond restating the standard inverse criterion; the elementary integrating step and the Lamperti change alone are not the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
