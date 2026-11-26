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

The primary source defines accelerated first-return edges, with each edge here assigned unit cost despite variable labels. Its adjacency matrices are row-source, column-target in right-to-left lexicographic order; Corollary 4.8 and Example 4.9 give the stated two permutation recursions and check the orientation. Both base maps swap the two vertices. In the independent packed BFS, each target stores a source bitset, initially the diagonal pair; unioning the frontier bitsets at the two predecessors and removing already visited bits gives exactly the pairs newly reached at each distance. A source's last discovery depth is its outward eccentricity. All sources reach all targets. A separate ordinary directed BFS cross-checks levels 1–9. I compared the saved independent results against the actual frozen census.tsv: all 174 distance bins, 15 radii, 15 diameters, 15 eccentricity histograms and 15 ordered diametral-pair counts match. In particular, levels 9–15 have d=n+4, and level 15 has radius 18, diameter 19, eccentricity counts 18:19720 and 19:13048, and 17,136 ordered diametral pairs out of 1,073,741,824 total pairs. The Moore comparison is valid because distance at most n−1 reaches no more than 2^n−1 vertices with two outgoing edges per vertex. The proof claims neither an all-level upper bound nor a bound on the unaccelerated shift time.

## originality

PASS

The supported distinct result is the evaluated metric census on the specific directed accelerated graphs for levels 1–15, including the finite n+4 run and ordered farthest-pair counts. The closest exact catalogue hit is the assigned record itself. The primary source provides the very same graphs, recurrence and strong connectivity, but its inspected construction and connectivity claims do not evaluate these metrics. Nearby transformation-group computations and other Schreier graph diameter results study different invariants or graph families.

## value

PASS

The accelerated graphs arise in an established proof about the Kolakoski shift; their directed metric quantifies how far apart targets remain after acceleration, beyond the qualitative fact of strong connectivity. The profile gives reusable exact benchmarks for tight diameter or eccentricity estimates. A full initial range through level 15 covers both the lower-level transitions and the seven-level diameter excess of four, while histograms measure the rarity of extreme paths rather than only their existence. This is a useful finite result, not evidence of a proved asymptotic pattern or any elapsed-shift-time bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
