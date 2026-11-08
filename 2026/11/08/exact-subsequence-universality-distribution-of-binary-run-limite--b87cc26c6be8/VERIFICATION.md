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
# Reproducibility and scope of computational checks

Run `python3 verify.py` with Python 3 and no third-party packages. Successful output:

`VERIFY_OK r=1..8 n=0..44 cells=4232 direct_words=49872 full_alphabet=true minimal_profiles=true`

The program constructs the coefficient table of the rational generating function by its exact integer recurrence. It separately counts the same statistic via a run-bounded finite-state digit scan. It verifies every coefficient for the stated lengths and run parameters. It then directly enumerates all allowed words through length twelve for each run bound, tests universality by the actual condition that *every* ambient-binary target of a given length embeds as a scattered subsequence, and compares this with a separate greedy-arch implementation. A further independent first-run recurrence checks the total constrained-language counts. The program checks the exact minimum-length profile through universality index nineteen.

These checks are finite and cannot prove the formula for all integers or exclude an overlooked equivalent theorem. The full formal-state proof, boundary characterization, and analytic-rate argument are in `RESULT.md`. No externally independent scientific audit or formal verification has been performed.
