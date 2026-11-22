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

The finite result is checked by three accompanying, independently structured standard-library Python programs: `check_direct.py`, `check_indegree.py` and `check_symmetry.py`. They have been executed against the files packaged here and reproduced `direct_output.txt`, `indegree_output.txt` and `symmetry_output.txt`.

The first program enumerates all 4096 trajectories and builds orbit basins directly. The second constructs all 4096 transitions from a separate Petersen-to-Tietze graph construction and uses indegree stripping to recover all periodic orbits and their transient ancestry. The third enumerates every graph automorphism using the unique triangle and all permutations of the six remaining vertices; it then verifies equivariance and the spatial orbit counts.

The witness 31 has trajectory 31, 198, 22, 192, 16, 0, 0, giving a sharp first-periodic-entry time of five. The programs prove a finite 12-vertex classification, not any claim about all graphs of a given order or a uniform infinite family. The literature comparison remains subject to unindexed equivalents; independent external validation has not been performed.
