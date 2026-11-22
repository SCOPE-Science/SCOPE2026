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

# Verification notes

The infinite classification is proved by analyzing the successor dynamics on equivalence classes; it is not an inference from finite enumeration. The proof's critical steps are: distinguished-point isolation; a unique cutoff into an eventual cycle for any nontrivial quotient of a bi-infinite successor orbit; the divisibility order formula; explicit inverse incompatibility; and the directed-union obstruction to finite generation of full modular relations.

Run `python3 check.py` in a directory containing the standalone checker. It verifies representative finite windows of 40 cutoff/period configurations and 1600 ordered pairs of configurations, including forward closure, reverse-operation controls, lattice intersections and generated joins. The script prints `SHIFT_QUANDLE_LATTICE_CHECKS_PASSED 1640 parameter_or_pair_cases` on success. Its bounded checks are sanity tests, not exhaustive verification of all integer cutoffs and congruences.

Historical priority is limited to inspected published sources, exact searches, and previously recorded scientific claims. The result has no independent external mathematical certification.
