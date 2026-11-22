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

# Reproduction and limits
The independently built C++17 LCF model and Python three-direction incidence model each have 18 vertices and 27 edges; the latter is isomorphic to the standard Pappus-graph generator. The direct C++17 checker exhausts all 8,568 five-subsets for each edge-failure pattern, and the Python checker exhausts the 18 minimum dominators and all 351 two-edge and 2,925 three-edge candidate deletions. Both produce exactly 171 destructive triples, partitioned into 18 vertex stars and 153 matchings. The Python orbit audit traverses all 216 graph automorphisms and returns orbit sizes 9, 18, 36, 108. Re-run the included program files with their commands in RESULT.md. This is a finite computer-assisted proof, not a proof for any other graph family. No independent scholarly verification was performed.
