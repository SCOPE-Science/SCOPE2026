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

# Verification of the finite prescribed-triple spectrum

Run `count_reverse.cpp` and `count_forward.cpp` independently under a C++17 compiler, then `witness.py` and `verify_tables.py` under Python 3, as described in `RESULT.md`. Both compiled programs were run to completion. Their standard outputs agree on `TOTAL 141120 NON 1856 MAX 37 EXTREMA 1` and on the full exact `TRIPLE_HIST` with 23 nonzero finite values. The first program also gives the 205 distinct nonzero pairs in `joint_spectrum.csv`, confirms the independently previously published full-reset length histogram, and lists uniquely normalized boundary maps. `verify_tables.py` checks the full 23-bin frequency table, all 205 joint frequencies, their reset-threshold and triple-time marginals and the expected extrema. Python forward search verifies the hardest Černý triple \(\{1,4,6\}\), its 37-letter word, and the same-reset-threshold counterexamples.

The reverse program parameterizes by duplicated image, collision pair and bijection of the other inputs. The forward program instead independently enumerates multiset permutations, then searches 56 distinct start triples per transformation. Each BFS exhausts at most 255 nonempty subsets and does not impose a word-length cutoff. Neither program depends on third-party packages, reference tables or network resources.

The certificate proves the stated **finite** classifications only, conditional on ordinary code execution and arithmetic semantics. The mathematical argument for exhaustiveness and shortest paths is stated in `RESULT.md`; finite execution does not imply results beyond eight states. Code-to-claim and CSV totals were explicitly checked, including that the 23 finite bins total 139264 and the nonsynchronizing bin contributes 1856. External independent scientific review has not been performed.
