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

# Reproducibility and limits

The standalone file `verify_rule150.py` uses only Python 3's standard library. Run `python3 verify_rule150.py` in a directory containing this file. It exhaustively constructs the source language at all lengths from three through eighteen, counts each nonempty inversion fiber, checks all counts against the theorem, and computes every single-step output independently using both a tuple implementation and a cyclic integer-bit implementation. It also checks all-time stability at selected odd ring lengths, invertibility at ring lengths not divisible by three, and the six-periodic second-step witness at ring lengths 6, 12, 18 and 24.

Recorded result from the packaged program: `VERIFY_OK exact_lengths=16 iterate_cases=45 second_step_witnesses=4`.

The complete all-length theorem depends on the written recurrence and polynomial argument in RESULT.md. Exhaustive finite testing is not an infinite proof; the independent mathematical audit has not been performed. The full text of a plausibly related 2007 unrestricted inverse-rule paper was not available for comparison, which leaves an explicit literature-priority limitation.
