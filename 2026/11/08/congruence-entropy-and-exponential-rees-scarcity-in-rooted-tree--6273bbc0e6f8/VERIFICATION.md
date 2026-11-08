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

# Reproducibility and limits

Run `python3 verify.py` with Python 3 and no external dependencies. The command computes exhaustive hereditary-set and eligible-vertex counts and independently computes the bivariate recursive polynomials; it also constructs graph inverse semigroup multiplication tables for small graphs and exhaustively tests all equivalence relations for multiplication compatibility. The expected terminal line is `VERIFY_OK`.

For complete binary trees of heights \(0,1,2,3\), the checked congruence/Rees pairs are \((2,2),(7,5),(62,26),(3967,677)\). For complete ternary trees of heights \(0,1,2\), they are \((2,2),(12,9),(1762,730)\). The direct semigroup test for a two-leaf outward fork finds \(7\) distinct congruences; the algorithm verifies multiplication compatibility of every partition of its \(10\)-element graph inverse semigroup.

The verifier does not establish Wang's general classification, all-height correctness, or the logarithmic asymptotic estimates. The classification is a cited prerequisite, and the global conclusions are established by the proof in `RESULT.md`. No external independent audit has been performed.
