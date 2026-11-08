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

Run the included standalone checker with `python3 verify.py`. It requires the Python standard library only. The checker independently builds every scattered subsequence of each finite input, intersects their sets, tests all possible one-letter insertions for maximality, and compares the resulting set with the constructive description. It checks the exact length multiplicities, total cardinalities and independent greedy-budget identities.

The completed run reported `VERIFY_OK host_cases 46 common_words 170625 maximal_words 494 budget_tests 106600 symbolic_count_levels 25`. It covers all adjacent swap positions for tested alphabet sizes from four through seven, with power length restricted for exhaustive feasibility. The coefficient identity was checked through exponent 25. These finite checks corroborate but do not establish the infinite theorem. The proof in `RESULT.md` supplies the universal argument; the generating-function diagonal is justified algebraically by a formal residue.

No independent audit or external mathematical certification has been performed.
