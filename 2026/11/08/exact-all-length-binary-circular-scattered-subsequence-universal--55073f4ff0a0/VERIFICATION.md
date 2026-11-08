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
# Verification scope

To reproduce, run `python3 verify.py` in the same folder. No external packages or network are required. The script tests every binary word through length 12 against actual scattered-subsequence universality for every cyclic rotation, independent circular maximum-matching dynamic programming, and the closed-form counts. It checks the normalization and maximal-index boundary for every length through 500. Expected final line:

`VERIFY_OK exhaustive_words=8190 length_range=1..12 symbolic_lengths=1..500`

The finite tests are corroboration, not a proof of the infinite-parameter formula. The proof depends on the binary greedy-arch lemma, the cyclic transition matching equivalence, the unique-state property of the transfer matrix on proper edge subsets, and the explicitly subtracted even full-cycle overcount. No external independent audit is recorded.
