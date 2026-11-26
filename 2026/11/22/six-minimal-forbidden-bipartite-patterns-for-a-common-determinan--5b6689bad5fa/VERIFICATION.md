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

For each fixed x, a witnessing lax split supplies at most one chosen row and one chosen column; conversely assign edges on the row to the first atom and the remaining covered edges to the second. Choices in different fibers are independent. Thus a minimal failure has exactly one nonempty fiber, and containment here means edge-subgraph, not induced-subgraph, containment. A three-edge matching is a minimal failure; every nonmatching three-edge set can be covered using a repeated endpoint and an opposite-shore endpoint of the third edge. With no three-edge matching, König's theorem gives a vertex cover of size at most two. A non-cross-coverable graph then needs two same-shore cover vertices, each of degree at least two. Choosing two edges at each yields a failure because one opposite vertex can cover at most one edge at the unchosen center. The neighbor-pair intersections of size zero, one or two give precisely the two-star, path and cycle cases with named shores. Deleting one edge leaves one full center and one opposite endpoint that together cover everything. This also clarifies the abbreviated wording at RESULT.md:58: the chosen center alone misses both edges there; the full cross necessarily misses at least one. Direct labeling gives 3! for the matching bijection, 2 for assigning the ends of an oriented-shore path, and C(4,2)=6 for allocating leaves to two fixed labeled centers, with the cycle counted once. The example pairs (0,1), (6,45), (96,396) and vanishing terms for undersized shores follow. This is a general proof for finite nonempty alphabets, not a continuation of the finite checks in the support file.

## originality

PASS

The supported distinct result is the full named-shore minimal-obstruction basis. The coherence cutoff and cross criterion already have prior coverage; the binomial census is a direct count once the basis is proved, and even the aggregate coefficients potentially follow from the earlier satisfying-team enumerator with a matching correction. The exact obstruction types, not the mere cutoff or the coefficients alone, support the pass.

## value

PASS

The result gives a precise obstruction language for a canonical two-atom dependence split already studied for coherence. It identifies exactly which small witnesses are irredundant, including asymmetry of the two named shores, and enables recognition by one of six explicit subgraph types at any finite alphabet sizes. This structural certificate is useful beyond knowing a failing fragment has at most four assignments; the routine arithmetic alone would not justify value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
