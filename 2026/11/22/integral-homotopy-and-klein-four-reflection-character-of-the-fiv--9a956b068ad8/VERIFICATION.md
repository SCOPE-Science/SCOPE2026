---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and scope

Run `python3 check_grid_reflections.py` with Python 3.10 or later and no additional packages. It enumerates the independent five-subsets to construct the total five-cut dual, implements the cited lexicographic element matchings, and counts invariant nonempty faces by unions of orbits of each reflection. The character comes from the signed simplicial Lefschetz sums and homological support. The signed sums and the four multiplicities are checked exactly, not sampled. The matching reproduction documents why the rank and ordinary wedge are treated as input from prior work and its consequences, not as the claim. The range is this single finite grid and the stated rational representation. `CHECK_OUTPUT.txt` records the expected lines for this script.
