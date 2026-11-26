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

For each edge I computed the minimum of two Hamming distances, packed the resulting distance signatures without collisions, and separately unioned the covered edges. The exact replay checks all required cardinalities against lower counts (resolving, covering, joint) (0,4,0), (0,16,0), (64,112,0), (1280,80,0) at d−1 and finds (4,32,176,160) joint sets at d. Monotonicity excludes all smaller subsets. The checks at d−2 establish ordinary minima 3 and 4 in dimensions 4 and 5. Full translation/coordinate-permutation orbits of the representative shapes give set equality, with sizes 4; 8 and 24; 16, 64 and 96; and 160. The repaired claim compares minimum cardinalities, not the possibility of augmenting every ordinary basis. Indeed, in Q5 only 160 of 1280 ordinary 4-bases are single deletions from an optimal joint set; {0,3,5,14} in binary-integer notation is a checked nonextendible ordinary basis. The complete replacement RESULT.md is under /workspace/repairs/5/. Replay: python3 /workspace/checks/5.py. No higher-dimensional conclusion follows from these tests.

## originality

PASS

Pass is for the repaired, credited scope. The joint minimum sizes in Q2 and Q3 follow exactly from earlier product theorems, and the whole labelled Q2 row from the earlier complete-prism classification. These are now attributed rather than offered as new. The inspected statements do not cover the joint minima or the complete geometric optima in Q4 and Q5. The Q3 classification is retained as a supplementary complete census; ordinary edge dimensions and unrelated measures are not the basis for originality.

## value

PASS

Q4 and Q5 are successive standard cubes where adding a local coverage constraint provably changes the optimal size relative to pure edge identification. The complete basis geometry identifies exact placements, not merely a cheap extra case of a scalar table: three distinct four-dimensional orbits collapse to one rigid five-dimensional shape. This is a natural benchmark for the published joint parameter and for studying when and how an identification set can meet a local coverage constraint. It does not rest on the known Q2/Q3 minima or on a claim of arbitrary augmentation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
