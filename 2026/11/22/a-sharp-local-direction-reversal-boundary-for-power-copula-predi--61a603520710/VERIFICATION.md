---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The mixed density is nonnegative even at β=1/α, and C<uv throughout the open square for β>0. For f=1+β(1−u^α), the factor 6 follows from integrating the unconditional variance of the uniform-response indicator. In the V|U integral the first two nondifferential-in-square terms combine to (u/(2f+1))′ and the mixed-with-v terms to −2(u/(f+2))′; their integrated boundary values cancel the added 1/3. Thus the exact functionals reduce to ξ(V|U)=12∫(uf′)²/(2f+1)^3 du and ξ(U|V)=6∫u²(f−1)²/(2f−1) du over [0,1]. Expanding these shorter formulas and integrating u^(q+mα) as 1/(1+q+mα) independently reproduces D₂, D₃, D₂′(9/2)=−9/100 and D₃(9/2)=−1458/1595. The bounded denominators and uniform integrability on compact shape intervals give a uniform Taylor remainder; the divided functional Δ/β² extends analytically near (9/2,0), including at β=0. The implicit-function derivative is −3240/319, and the negative shape derivative gives the stated signed sides and local uniqueness. At the critical shape the explicit inequality is ξ(V|U)>ξ(U|V) for sufficiently small positive β; this disambiguates ‘reverse conditioning direction’ in line 26. Neither equality at every β for α=9/2 nor globally unique equality nor a causal interpretation follows. The frozen checker was inspected, not executed.

## originality

PASS

The same copula and the same directional population functional are established prior work. The new statement supported here is the model-specific weak-dependence crossing, its nonzero critical cubic coefficient, and the locally unique moving boundary. The strongest overlapping claims inspected do not cover that combination. This is a bounded best-of-knowledge judgment, not historical certification.

## value

PASS

A deliberately asymmetric copula has opposite predictive orderings arbitrarily close to independence without changing the negative quadrant-dependence sign. The exact critical exponent and the nonvanishing cubic term distinguish a leading-order cancellation from actual equal predictability; the β-dependent boundary gives a useful local diagnostic for this established model. This is not just calculation of ξ for isolated parameter choices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
