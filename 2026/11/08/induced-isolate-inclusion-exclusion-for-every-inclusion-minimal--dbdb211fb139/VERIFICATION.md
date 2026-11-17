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

PASS: With omitted vertices W, each edge internal to G[W] is forced; other essential selected edges are exactly one cross-edge from each w isolated in G[W]. Selected receivers u are essential iff an unchosen edge u-w to W becomes uncovered upon removal; bad receiver events require all nonempty W-neighbors isolated in G[W] and all assigned to u. Inclusion–exclusion over pairwise disjoint receiver neighbor sets B_u gives c_G(W); each minimal cover has weight n-|W|+e(W)+|I(W)|. Bound at most sum_W 2^{n-|W|}=3^n terms. Independent original-coverage brute force matched receiver formula for K2, P3, K3, C4, K4. n=1 isolated-vertex boundary yields only its chosen vertex.

## originality

PASS

PASS best-of-knowledge: Aprile–Ferrarini covers general problem and incidence reduction; a published biclique enumerator covers only a special case. The new arbitrary-graph induced-isolate formula is structurally stronger; generic minimal domination priority risk remains.

## value

PASS

PASS: Uniform exact structural classification and inclusion–exclusion for every inclusion-minimal mixed vertex-edge cover of an arbitrary graph extends a natural domination problem from optimization and special host families. Exact count and normal form may be used independently despite exponential complexity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
