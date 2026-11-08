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

# Reproduction and verification

Run `python3 trust_star_check.py` from the directory containing the enclosed files, using Python 3 with its standard library. The script independently computes coalition worth by direct edge traversal, the Shapley value by exhaustive subsets with exact rational arithmetic, and the claimed core intervals for rational parameters. It enumerates all vertices and tests all coalition inequalities for the selected positive rational weights and all tested nonempty-core parameters.

Recorded execution: 157 exact-rational model/threshold cases, 1,596 tested core-box vertices, and 101,360 tested coalition inequalities; all passed. The checked cases include equal and unequal weights, ties, several leaf counts, the exact stability threshold, and both sides of the core-nonemptiness boundary.

These computations are finite checks, not an exhaustive check of all real weights, all leaf counts or all real parameters. The universal statement is established by the analytic inequalities and unanimity decomposition in `RESULT.md`. Independent scientific audit has not been performed.
