---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Over C the row-column scaling preserves both ideals. The one-parameter weights ni+j (0-based indices) are distinct, so the invariant (k+1)-dimensional vector subspaces are exactly the coordinate ones. Restriction to any such subspace retains distinct permutation monomials with nonzero coefficients in both minors and permanents; it vanishes identically for all r-blocks precisely when there is no r-matching. Euler localization for the reduced complex algebraic space identifies its compactly supported Euler characteristic with that of the fixed locus, and the Fano schemes are projective. Thus both Euler characteristics count the same finite set without any scheme-multiplicity weights. By Konig's theorem an admissible graph has a cover with at most r-1 vertices, each of degree at most n, proving the threshold for q=k+1. For r=2, pairwise intersecting edges in a simple bipartite graph with at least two edges have a unique common center, proving the two disjoint star counts. The combinatorial checker was inspected, not run; it cannot check Euler localization and is unnecessary for the proof.

## originality

FAIL

No exact independent printing of the Euler formula was located, but the published matching classification of the common finite fixed set already determines the asserted invariant by standard Euler localization. No new fixed-point classification or enumeration remains. The threshold and r=2 formula are direct matching-theory deductions. This is demonstrable prior implication, not a failure due to retrieval or a claim that Chan–Ilten printed the Euler formula.

## value

FAIL

Ordinary Euler characteristic is a natural comparison, but its exact equality here is mechanically read from the already classified common fixed set. The note gives neither a nontrivial evaluation of the remaining general matching count nor an invariant not determined routinely by that set. The valid equality is a useful explanatory corollary rather than a distinct scientific contribution under this standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
