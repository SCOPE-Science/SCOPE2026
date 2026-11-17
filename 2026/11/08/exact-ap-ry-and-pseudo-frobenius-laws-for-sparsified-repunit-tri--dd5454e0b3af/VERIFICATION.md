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

PASS — The identities R_(n+2)=a+u and R_(n+6)=a+mu hold for a=R_n, u=b^n(b+1), m=1+b²+b⁴. Representing a residue increment t with 1- and m-coins has minimal coin count c(t)=floor(t/m)+(t mod m); its least semigroup cost is W(t)=ut+ac(t). Since u>m for b≥2,n≥3 and c(t+a)−c(t)>−(m−1), W(t+a)>W(t); all Apéry representatives are W(t), 0≤t<a, and distinct residues arise from gcd(a,u)=1. Semigroup-order comparisons leave terminal residues a−1 and, for n≥5, km−1 (where a=km+r), both maximal and incomparable; n=3 has only a−1. Using the exact r patterns n mod6=1:1,3:b²+b+1,5:b³+b, the larger terminal gives F at a−2 when n≡1 mod6 and otherwise a−1; summing W gives the stated genus and type-one iff n=3. Independent exact-integer Dijkstra residue shortest paths for (b,n)=(2,3),(2,5),(2,7),(3,3),(3,5),(4,3) reproduced complete Apéry sets, genus/F and pseudo-Frobenius sets, e.g. (2,5): F3159, genus1690, PF{2509,3159}; (2,7): F51048, genus25710, PF{49019,51048}. Finite checks are not universal proof.

## originality

PASS

PASS WITH IMPORTANT PRIOR SUBRESULT COVERAGE — Liu–Xin–Ye–Yin arxiv:2306.03459v4 Collection GCNS Theorem 2.10 already IMPLIES the complete greedy Apéry set for these sparse triples, and Theorem 2.13 already IMPLIES its genus formula after specialization with coin set B=(1,m), GCNS parameter u0=1 and d=u−a>0 (condition u=b^n(b+1)≥m−1). These two ingredients are NOT original. Their Theorem 2.12 Frobenius formula requires s1≤u0+1 or s1<u0+1, violated because s1=m−1≥20 and u0=1; in fact n≡1 mod6 has maximum at a−2 rather than a−1. They do not provide the complete pseudo-Frobenius/type classification or the explicit index-mod6 Frobenius branch. The earlier 2026 positive-offset h-ary three-generator findings have d>0 and a lower bound; our corresponding h=b²+1 offset d=u−b²a<0, hence do not cover it. The assessed surviving original part is the all-odd-index PF/type/symmetry and sharp Frobenius branch, retaining the broader Apéry/genus tools as credited deductions, not standalone novelties.

## value

PASS

PASS — Removing intermediate repunit generators creates a natural genuine three-generator numerical semigroup with nontrivial pseudo-Frobenius type and explicit mod-six Frobenius branch. Its complete PF/symmetry dichotomy for every odd index is a mathematically motivated exact invariant classification, not an arbitrary finite slice or mere routine normalization. Known universal Apéry/ genus machinery is acknowledged and not sufficient for the surviving PF/F statement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
