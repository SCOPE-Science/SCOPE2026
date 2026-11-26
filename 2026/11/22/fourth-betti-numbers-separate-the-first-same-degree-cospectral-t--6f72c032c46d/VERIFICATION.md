---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Leaf extension exhausts trees by deleting a leaf, and the recursively sorted rooted codes at the invariant center(s) detect unrooted isomorphism. Matchings give the adjacency polynomial by the shared deletion recurrence. Independently I generated rooted trees as all multisets of already generated rooted branches of the required total order, then identified unrooted trees by minimizing the rooted code over all vertices. Exact adjacency characteristic polynomials, calculated directly rather than by matchings, and sorted degrees give no collision through eight and exactly two buckets of size two at nine; their isomorphism classes match all four witnesses. For cohomology the graph bracket is rational and the compact quotient exists; Nomizu identifies real de Rham dimensions with the Chevalley–Eilenberg complex. The exterior derivation sends each edge form to the wedge of its endpoints up to common sign and preserves vertex support. The supplied support-block elimination is valid; separately I replaced edge-form entries in ordered tuples by their two endpoints, sorted by explicit inversion parity, checked d²=0, and performed full sparse fraction-free elimination over Q without support blocks. The ranks d_0 through d_4 are (0,8,75,404,1383), (0,8,75,404,1382), (0,8,73,397,1351), (0,8,73,397,1350). Subtracting successive ranks from binom(17,k) reproduces the stated Betti vectors. The spectral fact refers to the joint invariant, not to the first adjacency-cospectral trees in isolation.

## originality

PASS

The distinct claim supported by this audit is the specific fourth-Betti separation of both minimal same-degree adjacency-cospectral tree pairs. General graph Lie-algebra methods, lower-degree tables, and examples of trees with the same degree sequence and adjacency spectrum are known. The relevant available exact graph tables and cohomology formulas do not already provide or directly imply the two one-unit fourth-degree differences and equality in all lower degrees.

## value

PASS

The standard unweighted graph Lie algebra and Betti invariants are independently motivated by the published graph cohomology program; adjacency spectrum and degree multiset are standard comparators. The result calibrates both the smallest example class with these two graph invariants tied and the first cohomology degree that actually breaks each tie. The two exact degree-four differences are useful reference values outside the known path and star families, not just a check that two graph Lie algebras are nonisomorphic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
