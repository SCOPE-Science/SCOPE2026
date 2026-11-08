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

The supplied `verify_rook_3colour.py` contains all source needed to reproduce the finite checks with standard Python 3.9+; run `python verify_rook_3colour.py`. The code directly enumerates every vertex subset on six boards, totaling 1,413,632 subsets, and tests the three-degree and maximality conditions. A separate graph-coloring backtracker explicitly constructs induced rook-graph adjacency and verifies three-colorability and inclusion-maximality for every subset on boards of sizes 3-by-3 and 3-by-4. A separate labeled binary-matrix degree recurrence calculates the coefficients and checks examples.

Actual output:

`VERIFY_OK graph_colorings=3x3,3x4 exhaustive_degree_enumeration_cases=6 total_candidate_subsets=1413632 exact_margin_counts=PASS`

Calculated samples: `M(4,4)={10:16,11:144,12:24}`, `M(4,5)={11:40,12:4320}`, `M(5,5)={13:700,14:10800,15:2040}`. Regular-matrix counts at orders 3 to 7 are 1, 24, 2040, 297200, 68938800, matching the independently indexed classical labeled sequence.

These finite checks neither establish the infinite result by themselves nor certify publication priority. The unrestricted claim depends on the explicit proof in RESULT.md. Independent mathematical audit has not been performed.
