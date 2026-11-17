---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For n=2^r−1 (r≥2), the path adjacency has recurrence p_{m+1}=X p_m+p_{m−1} in characteristic 2, giving p_n=X^n and a cyclic J_n(0) via the endpoint Krylov basis. The rung adjacency is I_2+N_2 with N_2²=0, so ladder A=I+K where K is multiplication by x+y on F2[x,y]/(x^n,y²). Frobenius and a two-dimensional K-kernel yield precisely blocks J_{n+1}(0),J_{n−1}(0). For reversible second-order T=[[A,I],[I,0]], Φ(T)=T²+T+I=diag(K,K)T with T invertible, giving rank-nullity filtration 2min(j,n+1)+2min(j,n−1), hence two irreducible Φ-primary modules of powers n+1 and n−1. In characteristic 2, X^t−1 has Φ multiplicity 0 when 3∤t and 2^{ν₂(t)} otherwise, establishing fixed spaces, exact order 3·2^r, and all primitive orbits by differences of nested fixed sets. Direct explicit-neighbor XOR on all 4096 paired-row states of the n=3 ladder independently gave primitive state populations 1,15,240,3840 at periods 1,3,6,12.

## originality

PASS

Best-of-knowledge PASS for the exact dyadic open-ladder second-order wave Φ-primary blocks and complete orbit census. Earlier reversible second-order CA framework establishes the map but not this special graph decomposition. Related ladder first-order neighbor-sum work supplies zero-primary transient counts, not the invertible two-row wave primitive periods. Plausible older publisher text on second-order linear CA could not be fully accessed, retained as a specific priority risk.

## value

PASS

A complete two-block rational canonical form with exact primitive orbit counts for every dyadic ladder length and every F_{2^f} is a natural and useful classification of a reversible graph wave. The dyadic double-scale Jordan fusion is genuinely structural, not merely a tiny computation; analytic proof provides sharp global period and all finite-field population counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
