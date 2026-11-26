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

Walsh diagonalization gives the support count over the reals. Independent relative orders factor the multipliers over the selected forest. Celano–Sieger–Spiro's Theorem 1.6 gives nonzero factors for odd-order trees (the singleton factor is 1); component-wise order reversal cancels the even-order factors. The frozen citation to Theorem 1.4 and Lemma 4.3 abbreviates the additional recurrence in Lemma 4.1; Theorem 1.6 is the direct reference. Independently, orient the selected forest across its bipartition and generate the permutation by ranking independent continuous uniforms on [-1,1]. Conditional on their absolute-value ranks, each edge contributes the sign of the higher-magnitude vertex, negated if that vertex is the tail. Averaging the independent vertex signs gives the indicator that each vertex has an even number of lower-magnitude neighbours, since all edges at any vertex have the same direction relative to it. Such an order exists for an odd tree: direct each cut edge toward its even-size side and take a sink as the last vertex; all branches there are odd, their number is even, and recursion gives the required orders. An even component cannot have such an order since it has an odd number of edges. The two-state recurrence counts precisely the permissible edge subsets, giving A >= F_m and B >= F_(m-1) by Fibonacci addition. An endpoint-rooted path attains both state bounds. For n >= 5, leaf deletion at equality forces the smaller tree to be a path; attaching the leaf to an internal vertex makes its even-root state strictly exceed the Fibonacci bound by F_(p-1) F_q > 0, with p-1 and q the two arm lengths. The two n=4 shapes have counts 3 and 4. Only even edge subsets can survive; a star permits every even subset and a nonstar misses the subset of two disjoint edges.

## originality

PASS

Pass for the sharp all-tree bounds and unique extremizers, not for the odd-component support rule or the path rank in isolation. One prior theorem implies the support rule and a distinct indexed result proves the path specialization; neither supplies the needed extremal comparison over all trees.

## value

PASS

The rank is an exact statistic for loss of Fourier frequencies in permutation comparisons. Determining both sharp ends of its range and singling out the unique extremal shapes is useful beyond computing the known path case; the parity recursion also gives a simple linear-in-tree-size count in integer operations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
