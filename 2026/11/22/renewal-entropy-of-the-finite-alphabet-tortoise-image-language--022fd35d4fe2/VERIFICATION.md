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

The finite verification script is `verify_tortoise_entropy.py`. Running `python3 verify_tortoise_entropy.py` uses only the Python 3 standard library and reproduces `verification_output.txt`.

It compares the map's recursive formula against a separate stack simulation and the language grammar on all words over alphabets of sizes two and three through length nine and size four through length seven. That is 52,389 input words, counted separately from the empty word. It also compares the exact binary and ternary output counts, tests forbidden-pattern exclusion, checks the four-letter sextic, and numerically locates the two algebraic growth rates. All tests passed.

Finite exhaustive verification supports, but does not prove, the all-length language and renewal-entropy theorem. The general statement follows from the grammar, unambiguous marker renewal sublanguage, coefficientwise bounds and rational pole analysis in `RESULT.md`. No numerical evidence is used as a substitute for these steps.
