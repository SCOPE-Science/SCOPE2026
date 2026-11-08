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

# Verification

Execute `python3 verify.py` with Python 3 and no external dependencies. Its reported successful output is:

`VERIFY_OK exhaustive_parameter_sets 213 root_candidate_upper_bound 101834 cyclic_cost_probes 28642 independent_partition_square_cases 78`

The program checks the maximum length of exact \(e\)-power subsequences of \((0^a1^b)^k\) by enumerating candidate binary roots and using greedy scattered-subsequence membership for all tested parameters. Its second method computes the square case from longest common subsequences of every prefix–suffix partition. It also probes the cyclic ceiling-run necessary inequality. Parameters beyond the finite search range are established by the symbolic proof in `RESULT.md`, not by enumeration. The program reports no independent proof certification or review.

Scientific boundaries: equality of the optimum length does not enumerate distinct optimal words, and the root is not required to be primitive. The source is a fixed finite binary two-run power. Public priority beyond the inspected literature is not certified.
