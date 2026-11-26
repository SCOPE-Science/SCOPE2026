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

For a complement D in Q4 the forest's edge count is 32−4|D|+e(D), ruling out eleven selected vertices and forcing e(D)≤1 at ten. The mixed 2+4 and 3+3 deletions violate that inequality by the neighborhood overlaps; 1+5 leaves the six-cycle formed by the three surviving neighbors of the sole deleted vertex of its parity and their three surviving pairwise common neighbors. Thus the deletions are pure parity. The two retained opposite vertices at distance two would give a square; at distance four they give disjoint full stars. Two maxima with the same full parity differ by two selections, and those with different full parities intersect in four. The Q3 proof's pure deletion triples and mixed triples with exactly one edge give 8+24=32; the two pure cliques are joined by the displayed mixed bridge. Independent replay `python3 /workspace/audit-work/small_graphs.py` uses leaf peeling and pairwise set differences, yielding maximum sizes 2,3,5,10, counts 1,4,32,8, and exchange-edge counts 0,6,144,0 in dimensions one through four. This is exhaustive for those labelled cubes only.

## originality

FAIL

The substantive Q4 equality formula and exchange obstruction are already contained in a distinct indexed record. No separate statement about the three-cube is claimed to be duplicated by that record; the residual contrast does not support the advertised new classification.

## value

FAIL

The natural Q4 extremal family and its exchange rigidity are scientifically meaningful, but the existing work identifies the same family and gives the stronger sharp buffer. What remains is a small comparison obtained by parity triples in Q3, all three-subsets in Q2, and the single edge in Q1. There is no independently motivated remaining classification or structural result to repair out of this submission.

The dated certificate retains the supplied scientific assessment, sources and limitations.
