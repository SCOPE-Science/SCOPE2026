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

# Reproducible finite verification

Extract `checks/verify_noncrossing_arcs.py` and `checks/cubic_zeros_n6.csv` to the same `checks/` directory and execute `python3 checks/verify_noncrossing_arcs.py` with Python 3.8 or later. Only standard-library modules are used.

The checker independently constructs the 132 admissible six-vertex arc subsets using (1) restricted-growth words for all set partitions, discarding crossings, and (2) exhaustive iteration over all 32768 arc subsets with direct crossing/endpoint tests. Their sets must agree exactly. Exact integer Walsh butterflies produce the entire spectrum. Independent direct evaluation of all 32768 character sums over all 132 supported vectors must agree coefficient by coefficient. Tests verify Parseval, odd/even congruences, the degree-by-degree zero counts, the two lowest-degree bands, the minimum nonzero magnitude four, and the complete supplied list of 25 cubic null frequencies.

The all-size degree-two positivity is proved by Catalan containment counts and inequalities in RESULT.md; its validity does not rest on finite computation. All degree-zero, one and two values are strictly positive for every \(n\ge5\). The complete rank/nullity is asserted only at six vertices. No independent audit has been performed.
