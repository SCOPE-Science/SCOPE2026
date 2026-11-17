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

For rate-one independent vertex clocks, thinning yields independent Poisson clocks on each undirected edge of rate deg(u)^(-1)+deg(v)^(-1). On K_(1,m), this gives E T_star=(1+H_(m-1))/lambda where lambda=(m+1)/m. On the star with added edge between source leaf 1 and leaf 2, a two-event competition before hub infection, with h=(m+2)/(2m) and c=h+1, and an independent maximum of m-2 original leaf clocks, produces the exact E T_edge formula in RESULT.md. The maximum Laplace transform F_m=prod_{i=1}^{m-2}i lambda/(i lambda+c) is derived by exponential spacings. An independent rational subset-state absorption recursion directly matched the two closed forms for m=2..8 and the exact boundary Delta_5=20155225/3059601384. Analytically Delta_m=m[P(m)+2F_mQ(m)]/[(m-1)(m+1)(m+2)(3m+2)^2], where P(m)=3m^4-10m³-32m²-28m-8>0 for m>=6 and Q(m)=m^4+4m³+3m²-4m-4>0 for m>=2. The four finite exceptions m=2..5 are exact, establishing first sign reversal at m=5; F_m<=1/(m-1) gives limit 1/3. All m>=2 covered by proof, not by bounded experiments.

## originality

PASS

The exact continuous-time leaf-source star edge-addition threshold m=5 and limiting penalty 1/3 are a new local-edit comparison on a natural small graph family. Acan et al. establish the exponential-edge representation and the unmodified star distribution; the added edge alters incident rates and requires a distinct two-case calculation. Published robust rumor spreading work mostly treats synchronous updates, and Resultary double-star asynchronous findings concern another topology. No inspected mathematical statement implies the all-m sign and boundary; potential unindexed Braess rumor-spreading examples remain risk.

## value

PASS

This sharp smallest-family Braess-style reversal quantifies when a seemingly helpful extra contact slows asynchronous rumor completion. An exact threshold (first six-vertex example) and nonzero large-star penalty provide a motivated network-design boundary, not just a tiny isolated counterexample. It is confined to a specific initial leaf and edge placement, not a universal edit theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
