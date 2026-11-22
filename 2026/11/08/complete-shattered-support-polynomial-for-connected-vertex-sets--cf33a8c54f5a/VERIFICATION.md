---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

For every a,b,c>=1, the graph with u,v and three arms has n=a+b+c+2 vertices and is 2-vertex-connected. The empty concept is expressly included. Reconstruct the general iff pairwise-connectivity test: all two-ones trace requires an x-y path avoiding all other support vertices; conversely join arbitrary positive P by such paths avoiding negative support vertices (induction irrelevant). This makes all <=3 supports shattered. For four supports, check two negative vertices: two poles fail, one pole forces one interior query on each arm, and no pole admits exactly arm-counts (2,1,1) or (2,2,0); all permitted cases survive every two-deletion test. With >=5, find a bad four-subset except no-pole (2,2,1); in that last case delete the more-v-end vertex of first doubled arm, the more-u-end vertex of second doubled arm, and the selected third-arm vertex to disconnect remaining positive vertices. Counting the disjoint support types gives Q=2abc+sum_cyc binom(a,2)bc+sum_pairs binom(a,2)binom(b,2); 2abc>0 proves VCdim=4. Edge cases a=b=c=1 work (Q=2). A wording ambiguity in the one-pole rejection when all three interior queries are on one arm is fixed by choosing the first two in arm order as deletion witness; it does not affect the valid theorem. Independently wrote a new finite trace enumerator: 864 complete-support cases across arms in {1,2}^3, and 45740 all-pair graph checks across arms in {1,2,3,4}^3, both exactly match all coefficients. These are corroboration, not an infinite proof. Fetched all seven actual source Git blobs at frozen commit and independently computed Git tree SHA a4e2548beefb44b1c3dd508ba5cc86d80eed7f6c. Read the complete supplied theta_verify.py code; log messages alone were not used as evidence.

## originality

PASS

The novelty asserted is the all-positive-arm exact support characterization and three-type fourth-coefficient polynomial on the three-path theta graph, not the generic 1994 pairwise path criterion or a general VC-dimensional framework. Direct inspection of Kranakis et al. TR-255 (Sections 2,4,5 and Corollary 4.4), Munaro (2013/2016, Sections 1-3), Dossou-Olory (2019 arXiv complete HTML), and published related SCOPE/Resultary connected-subtree and tree-halfspace results found broader general tools and different concept classes, but no theorem/table implying the specific theta support polynomial without a new case-by-case two-/three-vertex separator classification. The Resultary record with the exact same title has Git blob SHA de53d2cb69760324b516949b31c3b963539c48ba, identical to this assigned RESULT.md: it is a public mirror of the same work, not independent prior literature. A search cannot certify historical priority; equivalent unindexed terminology remains a real risk.

## value

PASS

The theta graph is a canonical minimal 2-connected noncactus two-terminal family, with three disjoint arms providing distinct two-vertex separator behaviours. The complete support polynomial and exact classification of all shattered four-sets (two pole-free distribution patterns and the one-pole pattern), including the universal nonshattering of every five-support, are natural, length-sensitive combinatorial invariants much more informative than a generic maximum VC dimension or maximum-leaf bound. The coefficient Q varies with all three arm lengths and identifies precise structural witnesses. It is neither a reparametrized prior table nor a single tiny graph or arbitrary numerical slice. A researcher studying connected-set trace ranges or separator decompositions could reasonably use these full support counts and forbidden configurations; no downstream theorem or broad new theory is necessary for this focused classification. Mathematical value is conditional on true nonimplication from prior literature, and the residual historical search risk remains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
