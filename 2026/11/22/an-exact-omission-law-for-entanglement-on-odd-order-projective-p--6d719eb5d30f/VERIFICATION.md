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

# Reproducible checks and scope

Run `python3 VERIFY.py` with the Python standard library; it has no external dependencies and prints the number of exact binary-rank comparisons for four projective planes. The algorithm creates normalized projective vectors over \(\mathbb F_p\) for \(p=3,5,7,11\), independently forms the direct faulted incidence matrix and the compressed rank-test matrix, and checks their ranks for every single gate, all disjoint two-gate choices at \(p=3\), random larger matchings, and conic-tangent patterns.

Expected terminal line: `ALL EXACT GF(2) CHECKS PASSED`. Individual case counts are 1723, 937, 1207, and 1947, totaling 5814. Observed baseline binary ranks are 12, 30, 56, 132; one-gate entropies are 13, 31, 57, 133; conic-tangent matching sizes are 4, 6, 8, 12; and corresponding entropies are 10, 26, 50, 122. All computations use exact integers; random selections use a fixed seed. The all-order theorem is certified by the argument in `RESULT.md`, not finite sampling. No external scientific validation was conducted.
