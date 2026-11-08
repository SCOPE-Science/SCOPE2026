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

# Reproduction

From a directory containing `verify.py` and `formulas.json`, run `python verify.py` with Python 3 and no nonstandard package dependencies. The exact execution completed with `VERIFY_OK: symbolic coefficient checks 474 exact grounded-matrix comparisons 4155`.

The script reconstructs all eight rational objective functions symbolically from the biclique block inverse and Sherman–Morrison formulas, verifies rational-function equality with the coefficient tables, proves the eight denominator polynomials positive over the relevant domain, and checks all difference-polynomial coefficient signs on the unbounded parameter regions. A separate grounded-Laplacian Gauss–Jordan routine confirms individual objective functions for all vertex pairs on 45 distinct biclique sizes (total 4,155 leader pairs).

The exhaustive *symbolic* coefficient tests, rather than the finite graph tests, support the infinite classification. They depend on the derivation that every two-leader pair belongs to one of the eight symmetry classes. The selected partitions have at least three vertices per part; no assertions about different budgets, other defect patterns or nonunit conductances follow. Independent mathematical audit has not been performed.
