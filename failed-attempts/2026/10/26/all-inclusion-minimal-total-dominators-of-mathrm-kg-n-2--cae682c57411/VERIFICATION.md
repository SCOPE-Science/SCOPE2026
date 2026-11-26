---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

A ground-set pair has no selected Kneser neighbor exactly when it covers the selected edges; smaller covers extend to a pair. Thus inclusion-minimal total domination is edge-minimality for cover number at least three, and deletion lowers cover number by at most one. The frozen cross-intersecting edge/cover pairs give the six-edge bound by pairwise disjoint ordering events of probability 1/6. There is also a code-independent exhaustion: in a bipartite graph use König's theorem to obtain three disjoint edges. In a triangle-free nonbipartite graph an odd cycle either has length five or already contains a three-edge matching. If there is a triangle T, an edge outside T gives K₃ disjoint K₂. Otherwise every cover of size two would have to be two vertices of T, so cover number at least three forces every vertex of T to have an outside neighbor. An outside vertex adjacent to all three gives K₄. An outside vertex x adjacent to just two creates a new triangle with those two; an edge from the third vertex of T to its outside neighbor y≠x is disjoint from that triangle. If all outside vertices have at most one neighbor in T there is a three-edge matching. Each of the four obtained subgraphs has cover number three and loses that property upon deletion of an edge, so minimality forces equality up to isolates. The labeled factors on their supports are 15, 10, 12 and 1, and K₄ is available for every n≥4. The frozen edge classifier's endpoint augmentation and exact canonicalization were inspected, with the recorded four survivors; the direct checker and recorded output corroborate n=4–8. No uploaded script was run; the independent exhaustion avoids making the theorem depend on a recorded run.

## originality

FAIL

A distinct Resultary record states the identical all-n classification, polynomial, and upper parameter, and goes further to characterize log-concavity and unimodality. The different proof organization does not change the frozen mathematical claims. The exact match suffices without assigning historical priority from the date keys.

## value

FAIL

The all-size total-domination census would be a useful exact invariant if uncovered. Here the precise objects, counts, and extremum are already present together in a stronger catalogue result. The frozen finite checks and set-pair bound add no independently useful unresolved case or new mathematical invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
