---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

FAIL

The numeric inradius and spread formulas follow from the published complete-multipartite facet classification, projection to H, polarity, and feasible binary and signed labelings. However the claim additionally asserts that WHEN A_{N,m}=B_N both type-(i) and type-(ii) tangent-facet mechanisms occur for every k>=3. Counterexample: K_{1,1,1}=K_3 gives N=3, m=1, A=B=2/3, but no part contains two vertices; published Proposition 3.5 requires f(A_i)={-1,1} for type-(i), so there are no type-(i) facets whatsoever. Only type-(ii) contacts exist. The source actually claims equality produces both mechanisms even in this case; the theorem as a whole is false on its stated quantifiers, though the radius/spread formulas remain valid. Independent rational boundary check confirms A=B=2/3 and type-(i) facet count zero.

## originality

FAIL

A published stronger exactly same-object result was located and its entire RESULT.md read, not merely a matching title. The prior formula r=1/sqrt(max{C_N,L_*}), with C_N=floor(N^2/4)/N and L_* the maximum parity-balanced signed part contribution only among sizes >=2, algebraically equals this record’s max{B_N,A_{N,m}} throughout k>=3 (when m=1, A is subdominant or coincides at K3). That prior proves the same tangent-facet phase with the correct type-I existence condition. The additional graph-spread formula follows immediately from r^{-2}=max ||f-mean(f)||^2 = N spread(G); it is a covered corollary, regardless of the different wording. Moreover the new result incorrectly asserts both contact types at K3.

## value

FAIL

The exact inradius/tangent-facet phase statement has already been established for the identical polytope realization and all complete multipartite graphs in a published stronger record, including the singleton exclusion. The additional graph-spread identity is an immediate variance=||centered labeling||^2/N reformulation of the same polar maximum, not an independent motivated gap. As asserted the equality-contact statement is also false at K3. This is covered, not an independently valuable new result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
