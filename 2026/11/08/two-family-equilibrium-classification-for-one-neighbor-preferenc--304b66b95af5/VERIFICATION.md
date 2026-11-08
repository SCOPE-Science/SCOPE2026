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

Run `python3 verify.py` with Python 3 and the standard library. The script checks every bit-pattern allocation of a cycle of size 3 through 16 against the literal, unrestricted, unilateral relocation test. It also checks the independent structural predicate, exact formula for every admissible population size, and the exact existence criterion. There are 131,064 exhaustive patterns, plus 600 reproducible larger random patterns. The code raises an assertion if any comparison fails and prints `PASS` lines upon success.

The analytic proof in `RESULT.md`, not these finite tests, supplies validity for arbitrarily large cycle sizes. The independent mathematical audit is not performed. A literature search cannot prove that every possible equivalent published formulation has been located.
