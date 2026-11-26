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

The axial orbit is exact, and its transverse linearization is u'=-(a+ks)u+av, v'=su-cv with s=bt-z0; the axial variation is constant. The Riccati equation for r=u/v is r'=a+(c-a-ks)r-sr^2. Matching the constant and inverse-s orders gives A=a/k and B=((c-a)A-A^2)/k in r=A/s+B/s^2. The residual is O(s^-2); adding and subtracting L/s^3 changes its leading coefficient by minus or plus kL, so for fixed sufficiently large L and then s, scalar comparison traps a solution on a forward half-line. Reconstructing v>0 and integrating sr-c gives exponent A-c and power B/b with relative error O(s^-1). For the fast line the scalar elimination is valid on that half-line. If g=W/v_s^2 is the positive integrand in the terminal reduction-of-order formula, the exact Wronskian and the slow logarithmic derivative give g'/g=-ks+O(1). Then (g/(ks))'=-g(1+O(s^-1)), so the integral tail is g/(ks)(1+O(s^-1)); this justifies both the fast logarithmic derivative and norm estimate without differentiating an unproved remainder. The derivative of the integral supplies a nonzero Wronskian and ensures independence. Both solutions extend to any finite initial time by the original nonsingular linear system, even if s=0 there. At critical k=a/c, A=c and B=-c^2, so every nonfast transverse vector gives the claimed algebraic amplitudes and the exceptional line still decays faster. The equilibrium count follows from xy=b and y=ax/(a-ck), with impossibility when a-ck=0. An independent symbolic check `python3 /workspace/replay/audit_checks.py 5` (output `/workspace/replay/5.txt`) uses w=u+kv; for D=a+k(a-c) nonzero one can eliminate v from w'=-aw+Dv, v'=sw-(ks+c)v. Removing the first derivative and taking X=(ks+a-c+2a/k)/sqrt(kb) gives Y_XX=(X^2/4+1/2+B/b)Y. The code verifies that alternative exact reduction and the D=0 triangular and critical coefficients. The long-time statements are justified by the proof, not the symbolic test.

## originality

PASS

Dong's vector field, Jacobian, and finite-equilibrium boundary are prior and are credited as such. The supported distinct material is the full two-mode transverse classification on the drifting axis, including the critical power, the fast line, and coverage for all positive parameters. Classical ODE and parabolic-cylinder theory are tools, not new results; a separate model-specific reduction shows how the classical scales map to these particular coefficients. No exact Dong-axis rate or equivalent applied reduction was identified in the checked sources.

## value

PASS

Equilibria escaping to infinity motivate this exact cutoff independently of the calculation. Leading exponential growth alone cannot tell whether the marginal transverse perturbations decay; the specific inverse-power exponent does. The complete mode splitting also identifies the exceptional fast-stable line on the growing side. This makes a useful exact stability diagnostic for the published field, not a claim of a new general ODE method or nonlinear attraction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
