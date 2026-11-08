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

# Reproducible verification

The proof in `RESULT.md` is the mathematical justification for all integer ring lengths. Python 3 is the only execution dependency for these standalone scripts.

- `python3 verify_direct.py` enumerates all \(2^n\) input configurations for every \(1\leq n\leq18\), tabulates exact output indegrees from the local truth table, checks the claimed maximum and complete set of maximizers, and prints `DIRECT_VERIFY_OK`.
- `python3 verify_inverse.py` implements simultaneous `10`-to-`01` swaps separately, checks inverse-swap subset counts and cyclic junction clauses against exhaustive output fibers for every \(1\leq n\leq14\), and prints `INVERSE_VERIFY_OK`.
- `python3 verify_run_formula.py` uses transfer matrices constructed from cyclic run lengths, checks the proposed alternating and near-alternating counts for all lengths through 200, and checks rotation invariance and extremal bounds on random examples; it prints `RUN_FORMULA_VERIFY_OK 200`.

The first and second scripts have independently coded forward updates. The third does not depend on either. All three checks completed with these exact success markers. No finite execution certifies the theorem for unbounded length; that quantifier is established by the written combinatorial proof. Historical novelty and independent audit are not program-certified.
