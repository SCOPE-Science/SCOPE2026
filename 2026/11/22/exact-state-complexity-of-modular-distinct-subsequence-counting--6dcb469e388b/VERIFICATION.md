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

The finite checker `checker.py` reconstructs the reachable complete automaton for each modulus from 2 to 20 and independently partitions states by their accepted suffix languages. All state counts agree with the claimed formula. It separately enumerates distinct subsequence sets for binary input words up to length ten and compares acceptance modulo each modulus, with 38,893 direct comparisons and 9,538 transition checks. Its output is reproducible by running `python3 checker.py` without third-party packages. The full proof is algebraic; these finite tests do not establish the statement for every modulus. No independent review was performed.
