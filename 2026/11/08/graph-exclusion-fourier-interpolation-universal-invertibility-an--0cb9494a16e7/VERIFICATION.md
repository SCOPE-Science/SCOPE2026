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

Exact verification: execute `python3 path_fourier_checker.py` from the extracted package. Its arithmetic uses `fractions.Fraction` and exact quadratic cyclotomic pairs for character tables of orders two, three, and four. It constructs all independent-support indices and verifies both-sided multiplication of the declared matrix and inverse; tested path lengths are 2–8 (binary), 2–5 (ternary), and 2–4 (cyclic quaternary), fourteen instances in total. It additionally verifies the binary zero-coordinate congruence and the absence of additional inverse zeroes for the larger tested alphabets. The output is `PATH_INDEPENDENCE_FOURIER_CHECKS_PASS`.

The all-graph, all-group proof depends on character orthogonality, a blockwise tensor factorization and Möbius inversion, not extrapolation from these finite checks. Determinant magnitude follows from the block determinants. The path-zero law follows from an exact second-order recurrence. No independent audit has occurred.
