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

For the canonical Newton-polytope embedding P_{d,n} with n>=d>=3, each prefix simplex has 0 and consecutive coordinate-one vertices. Additive support gives coordinate bounds r<=c_i<=w_i-r and difference-facet bounds c_j-c_i+sqrt(2)r<=sum_{t=i}^{j-1} b_t-binomial(j-i,2), where b_t=min(d,n-t). The normal-ray classification in the Bossinger–Gürdoğan originating work is the explicitly stated external premise. Summing adjacent constraints yields r<=d(2n-d+1)/(2(2+(n-1)sqrt(2))), while endpoint widths give r<=d/2. At r* the inequality sqrt(2)r*>(d-1)/2 makes longer differences redundant; concavity of interval support numerators proves all path feasibility inequalities. The tight chain gives a unique incenter with n+1 contacts in one regime; strict slack gives an affine (n-2)-dimensional incenter set with generic four contacts in the other. Equality would equate irrational and rational quantities. The n,d>=3, metric/realization caveats matter.

## originality

PASS

The published Bossinger–Gürdoğan paper introduces precisely these intermediate pellytopes and their normal fans. Its accessible abstract/introduction and facet-normal description do not state this inradius and contact transition; related Resultary inball theorems study other embeddings/polytopes. The full originating 2026 paper remained inaccessible via arXiv/OA and authorized Oxford reported vpn_disconnected, so this is an explicitly qualified best-of-knowledge originality PASS with substantive residual risk, not a claim of negative coverage from unread pages.

## value

PASS

The exact inball and center-space phase boundary for a named natural interpolating family supply a nontrivial metric invariant not determined by combinatorial equivalence. Both the radius and a change from unique incenter to a high-dimensional face of incenters are significant structural features, and the contact-facet classification is mathematically motivated by the family geometry. No paper-sized generalization is required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
