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

# Finite verification scope

Run `python3 checker.py` using Python 3.9 or newer. It enumerates every nonempty family of nonempty outcome subsets for one, two and three labelled outcomes, filters exact common full union, independent cross intersections, and opposite-action capacities. For each surviving pair it tests all pointwise admissible deterministic matrix fillings and compares row and column outcome supports.

The expected lines are `outcomes 1 admissible 1 nonrealizable 0`, `outcomes 2 admissible 4 nonrealizable 0`, `outcomes 3 admissible 282 nonrealizable 54`, and `CLONE_FREE_FIRST_OBSTRUCTION_OK`.

The proof in RESULT.md supplies the mathematical equivalence of these finite tests with the theorem's definitions, explicit realizations for every smaller candidate, and a symbolic impossibility proof for one three-outcome instance. This verifies only the small finite domains; it does not certify general higher-outcome claims. Independent audit has not been performed.
