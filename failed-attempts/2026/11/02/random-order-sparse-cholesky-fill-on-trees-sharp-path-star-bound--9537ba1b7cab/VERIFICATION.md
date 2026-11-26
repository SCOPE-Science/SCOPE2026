---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The stated theorem is correct. In each Schur step the pivot is positive and the update subtracts a strictly positive amount exactly for a pair of surviving neighbours of the pivot; off-diagonal entries never become positive or cancel. The symbolic fill-path criterion on a tree requires all d-1 internal vertices of the unique path to precede both endpoints, which occupy the last two of d+1 relative positions. This gives 2/[d(d+1)] and the distance sum. The upper bound is the nonedge count times 1/3, with equality exactly when all nonedges are at distance two. Deleting a leaf leaves old distances unchanged; the sorted distances d_j from that leaf satisfy d_1=1 and d_j<=j (take a shortest path to a farthest vertex). Thus its contribution is at least sum_{j=2}^{n-1} 2/[j(j+1)]=1-2/n. Equality requires a vertex at distance n-1 from the leaf, and paths attain it. For the path, the surviving graph is a path at every step. Given the entire elimination history, the next vertex with k remaining is uniform and exactly k-2 of the k choices create one new fill edge. The conditional probability does not depend on the history, which gives the independent Bernoulli factors and the claimed PGF. Their mean, variance, and products for the extreme probabilities give the formulas, and bounded summands with variance 2 log n+O(1) give Lindeberg's condition. For the star, only elimination of the center can create fill; it joins the K remaining leaves, with K uniform. At n=2,3 the two extremal trees coincide. There is a local proof error at frozen line 73: inserting the largest value can destroy earlier records; inserting the smallest value gives exactly the claimed recurrence. The direct conditional path proof above independently establishes the theorem without that sentence. No repaired package is proposed for an otherwise non-passing finding.

## originality

FAIL

The exact pair probability and hence the distance-weighted expectation are immediate from the classical fill-path criterion and one relative-rank count. The sharp extrema follow by elementary ordering of tree distances, the path distribution is a relabelled two-sided record law, and the star law is an exact case of a distinct catalogue result. No separate nonroutine fill theorem remains. This is an implication assessment, not an assertion that a prior text printed the entire package or that the same-day record has chronological priority.

## value

FAIL

Random-order fill is a natural baseline, and contrasting linear and quadratic means is pedagogically useful. But the proposed standalone results amount to a relative-permutation count in the standard deterministic criterion, a telescoping evaluation under elementary distance domination, and elementary or already covered path and star laws. The frozen claim has no additional nonroutine algorithmic, distributional, or structural conclusion after those deductions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
