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

# Verification and reproducibility

Extract `checker.py` together with the Markdown files, and execute `python3 checker.py`. The checker uses only Python's standard library and `fractions.Fraction`: it computes exact Bernstein matrices and their column sums, enumerates every nonconstant binary input on three through nine sites, verifies computed ratios against the analytic sandwich, and checks the weighted Gini cut comparison on a range of exact rational probability vectors.

The exact exhaustive cut totals for degrees two through eight are 6, 14, 30, 62, 126, 254 and 510, respectively (1,002 cuts). Their exact norms are `1`, `88/81`, `37/32`, `3781/3125`, `1217/972`, `1058952/823543` and `688641/524288`. These are finite diagnostics and are not extrapolated to assert an exact formula at every degree.

The general column-mass theorem, strict amplification for every degree at least three, and the sharp asymptotic operator constant are analytic consequences of the proof in `RESULT.md`. The mathematical proof specifically covers the unbounded dimension parameter, which no finite program execution can certify by itself. Rechecking sources and mathematical priority independently is outside the scope of this verification.
