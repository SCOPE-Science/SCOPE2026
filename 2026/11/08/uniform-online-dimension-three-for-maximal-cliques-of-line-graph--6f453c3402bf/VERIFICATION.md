---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Reproducibility and limits

The proof is self-contained: each pair of distinct edge-queries belongs to at most two maximal intersecting edge families; a putative depth-four mistake tree would require four such positive-positive witnesses. On complete graphs, maximal intersecting edge families are precisely full stars and triangles, and the eight patterns for each three-edge star/triangle support have explicit witnesses.

`python check_max_clique_learning.py` runs an independent enumerator for all nonempty graphs on up to five labeled vertices and for complete graphs on four, five and six vertices. It verifies exactly 1094 graphs in the general test and the coefficient lists in the paper. This tests representative instances, not the infinite theorem.

No external/independent audit has been conducted. The known structural star/triangle classification is distinguished from the new shattering and learning-theoretic conclusions; historical priority cannot be guaranteed from a bounded literature search.
