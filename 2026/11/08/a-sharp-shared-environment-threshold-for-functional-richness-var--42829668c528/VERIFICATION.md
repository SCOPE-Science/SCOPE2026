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

For g>=2, p∈(0,1), θ>0, conditional Beta Bernoulli sampling gives u=E(1−P)^2 and v=E(1−P)^4, hence V=g u+g(g−1)v−g²u². Independent SymPy differentiation exactly reproduced the specified derivative factorization gp(p−1)H/[(θ+1)^3(θ+2)^2(θ+3)^2]. The proof checks c3,c4,c5>0 for all parameters, c2 and c1 sign compatibility (including g=2 special region) and c0 crossing at p_c(g)=(g+5)/(12g), so Descartes gives zero or one simple positive θ root with correct derivative signs. Independently checked g=2,p=1/5,θ=1/3 exact witness V=2052/3125 and endpoint bounds. The proof is uniform; finite examples are only corroboration.

## originality

PASS

Best-of-knowledge original exact global one-peak versus monotone law with threshold p_c(g)=(g+5)/(12g) under common Beta propensity; basic beta moments and intraclass correlation are prior standard facts.

## value

PASS

The unique interior-variance-maximizing environmental correlation boundary is a motivated exact classification for a natural exchangeable survival model and variable functional richness; it is a genuine finite-system dependence transition, not a mechanical finite enumeration or unmotivated slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
