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

`python3 verify.py` performs finite direct checks using only the Python standard library. It enumerates every cyclic class and tests every rotation for being a scattered subsequence of the fixed linear permutation-power host, independently of the weak-descent acceptance criterion. It also builds the weighted transfer trace directly by dynamic programming, applies the divisor/totient Burnside average, and checks exact near-maximal defect formulas by enumerating cyclic collections of strictly increasing arcs. On successful completion it prints `PASS: exhaustive_qk_cases= 11 length_cases= 76 boundary_cases= 60 transfer_matrix_and_Burnside_exact`.

The mathematical theorem for all integers is established by the greedy embedding argument, cyclic weak-descent Burnside identity, and defect decomposition in `RESULT.md`; it is not inferred from the finite test grid. The check does not cover general hosts, variant alphabet orders, or independent external validation. An independent scientific audit has not been performed.
