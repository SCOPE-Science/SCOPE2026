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

# Finite and structural verification

Run `python checker.py` with Python 3; no external packages are required. The checker constructs every graph on up to six labeled vertices, every seven-vertex graph with at most six edges, and every relabeling of the listed six-edge witness. Its `ALL_RANK_THREE_CHECKS_OK` output requires the absence of a rank-three graph through six vertices, zero seven-vertex witnesses with fewer than six edges, exactly 5040 six-edge seven-vertex witnesses forming one permutation orbit, and finite rank exactly three for the displayed graph under a separately programmed recursive rank definition. It also verifies the rank-three test fails for every five-vertex component with one isolated extra vertex. All finite checks are exhaustive within those ranges only.

The infinite-order edge extremum and universal forcing cutoff are proved structurally in RESULT.md, not by extending finite enumeration. The inequality \(6\le N(3)\le7\) does not decide the exact value. Historical priority and mathematical correctness were self-reviewed; neither has an independent audit.
