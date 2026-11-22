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

# Verification and limits

The accompanying `verify.py` uses only the Python standard library. It explicitly creates the directed arc list of the cyclic doublet digraph, tests every color class for directed cycles by a topological-removal algorithm, and compares the resulting proper-color count with the claimed polynomial on each tested size/palette pair. It also checks all exact binomial identities used in the root argument and the odd-parameter Descartes sign-variation count for parameters 3 through 80.

Executed command: `python3 verify.py`.

The successful output ends with `SYMBOLIC_COEFFICIENT_AND_DESCARTES_CHECKS r=3..80 PASS` and `VERIFY_OK cases= 13`.

The mathematical result for *every* integer parameter at least three is proved symbolically in `RESULT.md`. Exhaustive enumerations of small instances do not establish any unbounded quantified statement or exclude unknown historical coverage. The negative roots are located by strict signs and Descartes' rule, rather than numerically approximated. No independent audit was performed.
