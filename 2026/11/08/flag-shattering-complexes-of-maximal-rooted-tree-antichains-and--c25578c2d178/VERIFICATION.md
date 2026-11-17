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

PASS. RESULT.md defines frontiers as maximal ancestor antichains meeting each root-leaf path once, restricts to nontrivial finite rooted trees, and constructs G_T with ancestor-comparability edges and additional leaf-versus-other-child-subtree edges. Every shattered set avoids these pairs. Conversely, for any independent support and 0/1 labeling, take positive queried nodes plus parents of negatively labelled leaves, then complete uncovered paths by their leaves; independence ensures this is a valid frontier realizing the pattern. Replacing selected leaves by their parents injects independent supports into antichains of internal vertices, proving VCdim equals the number of terminal internal nodes. Binary-comb frontiers F_0,...,F_m form nested threshold queries, so Ldim=floor(log2(m+1)) by balanced cuts and the 2^d-hypothesis upper bound. Root/nonroot recursion gives Phi_{b,h}=z+Phi_{b,h-1}^b (h>=2), with base 1+(b+1)z. Independently constructed frontiers on 873 parent-labelled trees of sizes 2..7 and directly computed all trace-shattered sets and conflict graph, all agreeing; inspected pinned check_frontiers.py, whose wider recorded tests are not taken as proof. Single-vertex exception is correctly excluded from the G_T theorem.

## originality

PASS

PASS qualified. Earlier rooted-tree polynomials count maximal antichains, not all shattered query supports; the 2026-11-02 complete level-regular frontier result determines VC=Ldim on a restricted family but does not imply the all-tree pair-obstruction complex nor logarithmic Littlestone gap on non-level-regular combs. Tree path-membership and maximal-independent-set concepts have different hypotheses. Detailed all-graph constructive proof supplies a distinct classification; absolute priority under hierarchical prefix-code language remains open.

## value

PASS

PASS. The exact flag complex of all vertex-query shattered supports is a natural structural object for complete prefix-code/frontier learning classes, determines every support count and VC dimension, and the binary comb yields a sharp unbounded gap between static and adaptive dimensions within a familiar concrete concept family. Neither the graph obstruction theorem nor that growing gap follows by mere renaming of maximal-antichain counts; motivates exact learning complexity beyond a finite anecdote.

The dated certificate retains the supplied scientific assessment, sources and limitations.
