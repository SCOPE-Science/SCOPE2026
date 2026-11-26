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

At u=qt the radial component of W=v×a is −prq² sin(u)(1−r cos(u)), so only u=0 or π can give a zero; the radial acceleration there selects (r*,π). The squared speed never vanishes. The q periods cancel dt=du/q, so there is no extra q in the local coefficient. At the zero, set D=p²+q², V=|v(r*,π)|, x=u−π and δ=r−r*. The first derivatives of W are orthogonal, of lengths A=DV and B=p r* q²(1+r*). The squared norm is even in x and has exact local form a(δ)²δ²+x²b(x,δ), with a(δ)=D|v(r*+δ,π)|, a(0)=A, and b analytic, even in x and b(0,0)=B². Change variables to y=x√b/B. Parameter-dependent limits can be replaced by symmetric fixed limits up to an analytic contribution. The even weight, including inverse squared speed and Jacobian, is its value at y=0 (V⁻²+O(δ)) plus O(y²); the latter term has bounded integrated second derivative, by the bound O(1/√(y²+δ²)) for two radial derivatives of the square root. Integrating the constant-in-y term explicitly gives A²/(BV²)=D⁴/[p³q²(2p²+q²)] as the δ² log coefficient and a second derivative diverging to +∞. Dominated differentiation gives C¹; off the critical radius the integrand is analytic uniformly on compact radial intervals. The scaling r=λp²/q² gives a uniform O(q⁻¹) density error by the norm Lipschitz inequality, even at λ=1 and at the continuous λ=0 endpoint. Factoring the profile radicand gives the stated E modulus; the complementary modulus |λ−1|/(1+λ) yields the cusp by DLMF. A positive second derivative away from 1 and continuous first derivative through 1 imply strict convexity and, since F′(0)=0, strict increase. The frozen checker was inspected but not run; its finite diagnostics are not needed for these conclusions.

## originality

PASS

The supported distinct assertions are the integrated fixed-winding singularity with exact coefficient and the uniform bounded-λ geometric scaling law. Fuller's local zero classification and the classical elliptic endpoint expansion are established inputs, not separately credited as new. The strongest cited potential overlap was not fully accessible; the inference here is a best-of-knowledge comparison, not a priority certificate.

## value

PASS

The exact logarithmic coefficient describes how a local inflection affects a global knot observable and distinguishes C¹ from C². The uniform high-winding law resolves the transition through the zero and provides an invertible geometric radius profile, not merely a re-evaluation of a special function or a known inflection count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
