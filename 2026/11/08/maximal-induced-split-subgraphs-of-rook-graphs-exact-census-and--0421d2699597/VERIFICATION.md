---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Every clique of K_m square K_n with >=2 vertices lies in a line. Maximal induced split sets admit a full row or column plus a maximal nonattacking rook placement on its complement. An unselected cell cannot extend such a set without violating clique/independent structure; the m=2 columns and 2x2 overlap are handled separately by induced C4 and 2K2. Enumerating oriented lines gives m(n)_{m-1} z^(m+n-1)+n(n-1)_m z^(2m) (m<n), 2m*m! z^(2m-1) for m=n>=3, and 4z^3 for m=n=2. Cancellation proves probability m/[m+d(d+1)]. Fresh direct split-partition checks on boards 2x2 through 3x4 matched.

## originality

PASS

Rook graph is the line graph L(K_{m,n}); choosing induced split-graph vertices corresponds to a selected edge set whose line graph is split, not to arbitrary edge-induced subgraphs or an independent-rook placement alone. Brosse 2023 Thesis Theorem 3.13 supplies a general necessary maximal clique plus maximal stable set representation; its converse for the rook families and multiplicities are not supplied. Cao 2020 gives polynomial-delay enumeration, not this exact size enumerator. The general structural template permits candidate construction but alone neither proves distinctness/sufficiency for m=2,n=2 nor determines two class frequencies and square-root crossover. These are supplied by the family-specific proof. Best-of-knowledge originality with disclosed residual risks; no search failure alone is treated as novelty proof.

## value

PASS

The exact labeled inclusion-maximal split-set polynomial and long missing size intervals for a classical vertex-transitive family are natural finite combinatorics. The square-root aspect-ratio phase change is a quantitative count phenomenon not derivable from knowing only maximal split-subgraph existence or a general listing algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
