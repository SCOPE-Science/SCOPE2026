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

# Verification record

The standalone script `verify.py` builds each graph from nonempty bit subsets of \([r]\) up to cardinality \(r-t\), with adjacency calculated directly from bitwise disjointness. It separately checks the equivalent subgroup-order construction with integer least common multiples for selected prime products, and does not use the proof's singleton-clique connectivity argument.

Exhaustive deletion sets of cardinality \(0,1,2,3\) were checked for \((r,t)=(4,2),(5,2),(6,2)\), including identifying every minimum cut: \(176+2626+29317=32119\) exhaustive cases. For \((7,2)\) and \((8,3)\), all minimum-degree vertices and all predicted cuts are checked and a seeded sample of smaller deletions is tested (respectively 120 and 280 cases), giving \(32519\) deletion tests in total.

The script validates that all predicted minimum cuts isolate their corresponding vertex and leave one other component, that distinct minimum-degree vertices yield distinct cuts, and that the full support/complement adjacency equals the subgroup-product least-common-multiple condition. The output file `verify_output.txt` records the observed counts, concluding `VERIFY_OK deletion_cases= 32519`.

These tests are finite corroboration. The symbolic proof in `RESULT.md` establishes the claim for all permitted \(r,t\); it does not assert failure for smaller ranks. Neither code execution nor this record is an independent mathematical audit.
