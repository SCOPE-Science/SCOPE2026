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

The independent-audit channel has not been used. Reproduce finite checks with `python3 verify.py` in the directory containing the script. The script reconstructs adjacency and complement adjacency for selected small four-partite graphs, enumerates unordered vertex partitions, and tests global domination directly. Separately, it enumerates multiplicities of all nonempty proper part supports subject to vertex capacities, requiring each support type to have a complementary partner type. It checks 70 exhaustive sorted size profiles with sizes at most five and seven larger unbalanced profiles.

All checks are finite; the stated formula for arbitrary positive part sizes follows from the proof in `RESULT.md`, not the experiments. No independent mathematical audit or external certification is claimed.
