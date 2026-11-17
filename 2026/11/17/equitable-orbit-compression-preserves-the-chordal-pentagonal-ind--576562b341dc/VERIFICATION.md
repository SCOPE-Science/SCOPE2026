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

# Reproducible checks

Run `python3 verify.py`. The script uses only Python 3 standard-library modules and no downloaded data. For every labeled simple graph on up to five vertices with no forbidden induced cycle, the checker enumerates all independent equitable vertex partitions, verifies that their quotients have no forbidden induced cycle, enumerates every cyclic automorphism subgroup arising from every individual graph automorphism, and compares its invariant independent vertex subsets with all faces of the orbit-conflict graph. Four further cases test genuinely noncyclic generated subgroups.

The accompanying `verification_output.txt` reports 906 eligible graphs, 1695 equitable partitions, 3633 group actions including 2727 nontrivial actions, and 24273 fixed/model face comparisons, all passing. These are independent finite checks of definitions and logic, not certification of the infinite statement. The proof's shortest-cycle argument is required to pass from the finite checks to every finite graph. No independent audit has been performed.
