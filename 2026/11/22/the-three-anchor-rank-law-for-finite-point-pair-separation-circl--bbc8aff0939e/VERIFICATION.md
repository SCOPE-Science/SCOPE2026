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

# Reproducible checks and limits

Execute `python3 separation_rank_verify.py` using the standard Python 3 library. The checker constructs alternating-quartet fingerprints and their distinct one-point extension types over individually named marked vertices; it solves the minimax rank recurrence independently of the closed-form theorem. All induced marked subsets of circles of orders \(0\) through \(11\) match the theorem, and exact rank-tail counts on all marked subsets through order \(16\), for levels \(0\) through \(4\), match the binomial census. The script ends with `ALL_CHECKS_OK game_n_max=11 count_n_max=16` when successful.

These tests are finite corroboration only. The proof for unbounded finite orders uses the exact split condition \(g\ge2^{k+1}-1\), the three-initial-extension observation, and a stars-and-bars bijection. No computation, external formal verification or independent audit is claimed to establish the theorem without these arguments.
