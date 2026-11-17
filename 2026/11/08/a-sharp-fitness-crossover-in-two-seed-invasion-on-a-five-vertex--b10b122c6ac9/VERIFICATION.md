---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For death–Birth update on K_(2,3), the lumped (i,j) count chain has 10 transient states and four rates: (2-i)rj/(3-j+rj), i(3-j)/(3-j+rj), (3-j)ri/(2-i+ri), j(2-i)/(2-i+ri). Supplied rational polynomial certificate N_(i,j)/(60(r+1)Q(r)) has Q positive coefficients; original verifier algebra explicitly checks all ten coefficientwise backward equations, not a finite sample. Independently used symbolic algebra to verify F_(1,1)-F_(2,0)=H/(60(r+1)Q) exactly; all pairwise domination polynomials have positive coefficients. H has one descending-coefficient sign change and H(1)<0<H(3), so exactly one positive root 2.05144026631733... . Neutral r=1 probabilities independently checked as 1/2,5/12,1/3. Full-state rational finite checks are supporting, not a substitute for polynomial identities.

## originality

PASS

Best-of-knowledge original exact all-fitness two-mutant seed-location classification for unweighted K_(2,3) under death–Birth. Durocher et al. already establish biased-voter model, seed optimization and fitness-dependent changes in general, but not this graph’s three rational seed-probability laws and unique 2.05144 threshold. Birth–death bipartite and death–Birth star laws use different mechanisms or graphs.

## value

PASS

K_(2,3) is the smallest nonstar unequal complete bipartite graph suitable for a genuine two-part placement tradeoff, and the exact all-r crossover answers a motivated evolutionary network seed-allocation decision; not a numerical sample alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
