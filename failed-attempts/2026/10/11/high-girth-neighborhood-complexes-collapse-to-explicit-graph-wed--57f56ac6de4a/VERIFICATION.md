---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

The all-graph proof is mathematically sound. Under girth≥5, any two distinct open neighborhoods share at most one vertex, preventing simplex facet overlap beyond vertices; min degree≥2 makes all neighborhoods distinct maximal simplices. For each center v choose c_v∈N(v) and collapse all lower faces σ⊂N(v)\{c_v}, |σ|≥2, paired with σ∪{c_v} in decreasing cardinality. At each step σ has precisely one remaining strict coface; no other neighborhood simplex contains two of its vertices. Resulting graph has Σ_v(deg v−1)=2m−n distinct edges and n vertices. Edge paths are exactly even-length graph walks, giving one component for nonbipartite G and the two color classes for bipartite G. Euler cycle ranks are 2m−2n+1 or each m−n+1. Independently executed exact free-face collapse checks on C5 and C6. No unsupported infinity extrapolation from those tests; proof is all-graph.

## originality

FAIL

Decisive prior implication: two separate existing published mathematical results already give THE IDENTICAL rooted-star elementary collapse under strictly broader square-free hypotheses. For every nonbipartite G of girth≥5, the published nonbipartite direct-spines theorem applies since no C4 and proves all root choices, connected target graph of n vertices and 2m−n edges, hence wedge^{2m−2n+1}S1. For every bipartite G of girth≥5, the published bipartite direct-spines theorem applies since no C4 and proves two connected rooted-spine components of rank m−n+1. Neither requires min degree≥2 or triangle-free. Combining these two prior full-text results exactly implies the entire submitted theorem, including its constructive proof, not merely its numerical conclusion. C remains PASS; O FAIL and V FAIL under the same scientific bar. Do not mark repaired or rescue with disclaimers.

## value

FAIL

Scientific value FAIL for THIS final claim, not because finite or elementary collapses are worthless in isolation, but because the entire intended topological classification AND root-prescribed collapse mechanism have already been established under stronger hypotheses by two published full results. This restriction to high-girth plus min-degree≥2 supplies neither a distinct obstruction, a new boundary case, nor an independent invariant. It is a special-case restatement, so mathematical significance cannot be claimed as a new contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
