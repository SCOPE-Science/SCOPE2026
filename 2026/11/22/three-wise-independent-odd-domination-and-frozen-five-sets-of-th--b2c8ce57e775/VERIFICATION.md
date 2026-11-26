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

Independent replay (python3 /workspace/branches/independent_checks.py 4) checked the LCF and chord descriptions agree, the metric intersection numbers and girth, the eleven listed independent rows and seven listed null vectors including the free-column identity, and traversed all 262144 labeled masks by Gray-code syndrome updates. It found 128 solutions of weights 5/9/13 with counts 18/92/18 and tested all eight patterns on each of 816 triples. Rank 11 plus a nonempty solution set gives an affine dimension-seven code. The nonzero, distinct kernel-generator columns with no vanishing three-column sum give each triple rank three; fixed odd parity on a four-vertex closed neighborhood excludes four-wise independence. For a five-set, odd domination implies even induced degrees; girth six makes the induced subgraph a forest and thus independent. Its fifteen incidences on thirteen exterior vertices single out exactly one vertex v with three selected neighbors. To cover the six distance-three vertices with the two other selected vertices, each must cover three; only distance-four vertices can do so. Conversely the displayed N(v) plus the distance-four layer satisfies every parity equation by the verified layer incidences. Complementation preserves solutions as M times the all-ones vector vanishes; summing equations over a shore makes the total weight odd. The variance 9/2 from pairwise independence, with eighteen cases at each extreme, exhausts the allowed weights by forcing zero at 7 and 11. The replay checked all 153 intersections, confirming profiles 0/1/2/1, and all exchange eccentricities equal 3. For five-sets, intersection size 5-t is precisely a t-vertex replacement, hence the three-move graph is distance three with degree six and 54 edges. Connected even-degree induced subgraphs in the cubic bipartite graph are singletons or even cycles, ruled out by the odd weights at least five. The original scripts were inspected, not run. The proof text overstates the C++ verifier: it does not check the pair-intersection table or the three-move diameter; those are checked by the supplied Python algorithm on inspection and by the executed independent replay. This does not affect the claimed mathematics.

## originality

PASS

Pass for the distinct central parity-coset classification (full enumerator and exact strength three). Credit existing general odd-domination/Lights Out methods and the separate catalogue's substantial ordinary-optimum coverage. Neither the bare count nor the optimal family and intersection incidence, once identified with the ordinary optima, are independent novelty. No priority ordering is inferred from the same calendar date.

## value

PASS

The full weight spectrum and orthogonal-array strength of the closed-neighborhood parity coset are natural exact invariants of a canonical small cubic symmetric graph. Ordinary optimum counts do not answer either question: the parity constraints give uniformity on every triple while the minimum feasible sets are rigid under small replacements. The useful independent content is this full feasible-space benchmark and its structural certificate, not merely another computation of the known ordinary optimum count or the generic even-degree corollary. No generalization to other graphs is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
