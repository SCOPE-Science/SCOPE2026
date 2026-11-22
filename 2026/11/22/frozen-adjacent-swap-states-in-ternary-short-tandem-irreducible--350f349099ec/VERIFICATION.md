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

The self-contained `checker.py` runs with Python's standard library: `python checker.py`. It independently tests all admissible ternary-difference sequences of length two through eighteen against actual adjacent swaps, and enumerates all literal ternary words through length eleven. It checks the forbidden \(aa\)/\(abab\) predicate, the maximal-run criterion and the Fibonacci frozen-count formula; the run completed without an assertion failure.

Finite checks verify only the listed lengths. The unbounded assertion is supported by the local-swap and run classification proof in `RESULT.md`. There is no independent review or formal proof-assistant certification.
