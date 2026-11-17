---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For 0<a<1/2, g_a(x)=x/(1+x^2)^a is odd strictly increasing and concave on positive halfline, so any nonfixed two-cycle of F(x)=x-eta g_a(x) must be {R,-R} with R=sqrt((eta/2)^(1/a)-1). Its period multiplier (1-2e_R)^2 is strictly below 1, e_R=(1+(1-2a)R^2)/(1+R^2). For H(r)=|F(r)| and 0<=r<=R, H=h(r)=eta*g_a(r)-r is concave with h(0)=0,h(R)=R. Its range remains <=R iff h'(R)>=0, yielding a<=1/4 or eta<=eta_c(a)=2(4a/(4a-1))^a. Then amplitudes inside (0,R) strictly increase to R, and those outside descend or cross inside. At critical eta, h'(R)=0 forces eventual crossing below R and Taylor coefficient B_a=(5a-1)sqrt(4a-1)/(4a)>0 in R-H(R+delta)=B_a delta^2+O(delta^3), yielding R-H^2(R+delta)=B_a^3 delta^4+O(delta^5). Finite-hit exceptions are countable. Independent symbolic second-derivative and high-precision critical coefficient checks corroborated the algebra.

## originality

PASS

PASS best-of-knowledge and conditional on named accessibility limitation: Itin 2026 gives the general elastic local stability criterion for symmetric period-2 kinetic-map cycles and numerical global-attraction studies, not (from available abstract and relevant summaries) an exact trapping threshold a=1/4 for the fractional g_a family or critical eta with global quartic convergence. Ma et al. 2022 proves a general almost-everywhere convergence result for 1D even-convex decreasing-curvature losses; that antecedent does not contain the one-step invariant amplitude classification or nonzero quartic coefficient. Itin full text could not be lawfully accessed after arXiv/OA efforts and Oxford VPN returned disconnected; NO full-text negative coverage assertion is made for it, and this remains a material priority risk.

## value

PASS

PASS: the sharp finite invariant interval property for a concrete kinetic-gradient map and a unique tuning for nonzero quartic two-step convergence are natural discrete-dynamics invariants relevant to beyond-stability optimization models. The exponent a=1/4 gives a qualitative divide with explicit sharp threshold eta_c(a), rather than an arbitrary parameter slice or routine numerical approximation. Nonzero B^3 and exceptional-set scope are proved, without asserting attraction fails outside trapping.

The dated certificate retains the supplied scientific assessment, sources and limitations.
