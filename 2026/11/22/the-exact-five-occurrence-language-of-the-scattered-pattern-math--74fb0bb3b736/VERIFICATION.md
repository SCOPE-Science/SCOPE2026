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

The primary exact certificate consists of `CERTIFICATE.tsv` and `CHECKER.py`. The certificate lists the 126 reachable states of the product of a saturated (cap six) scattered-subsequence counter and a Thompson epsilon-subset automaton for `1*01*0(1011|1101)01*01*`. It lists both transition targets from every state. The checker recalculates each transition from definitions, verifies closed reachability from the initial state, and checks agreement of the predicates “exactly five scattered copies of `001100`” and “accepted by the regular expression” on all reachable states. This is a complete all-length finite-state proof.

Run `python3 CHECKER.py` with `CERTIFICATE.tsv` in the same directory. `CHECK_OUTPUT.txt` captures the completed run; standard-library Python suffices. The script also independently counts all words of lengths 6–16 with unsaturated dynamic-programming counters. Those finite samples are sanity checks, not the infinite proof.

The cardinality formula is deduced from the unambiguous regular expression by four-variable stars and bars; it is not inferred from numerical interpolation. No independent scientific audit has been performed.
