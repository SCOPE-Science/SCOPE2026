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

# Verification

Run the standard-library program `python3 check_rees.py` from this package. It constructs the semigroup multiplication, every generator from its defining domain and formula, and separately the conjectured Brandt maps using local-group coordinates. For each of eleven finite cases it checks equality of these sets of partial maps, closure under every ordered pair of compositions, and the predicted cardinality. Six nontrivial zero-pattern types and nonidentity sandwich entries are represented. The program prints `VERIFY_OK cases=11` on successful completion.

The implementation is a finite exhaustive check for the stated test cases. It is not an exhaustive search of all finite semigroups, and cannot prove the result for arbitrary groups or arbitrary index sets. Those quantifiers are established by the explicit algebraic argument in RESULT.md. A separate mathematical audit has not been conducted.
