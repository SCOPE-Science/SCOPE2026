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
# Reproducibility

Use Python 3 with NumPy and SciPy; run `python check_cycle_robustness.py` in the directory containing the standalone code. The expected success line is

`CYCLE_VERTEX_ROBUSTNESS_PASS exact_n=158 independent_qp_n=16 cutoff=6 plateau_squared=11/12`

The exact rational calculation checks complete supporting inequalities, exact norms, contact cardinalities and contact identities for every integer \(3\le n\le160\). The independent floating-point quadratic-programming comparison minimizes over all \(2n-1\) remaining root vertices for \(3\le n\le18\). The program does not perform exhaustive verification at all dimensions; the all-dimensional statement is proved symbolically in `RESULT.md` using the path Gram matrix and an exact projection certificate.

## Scientific limits

The metric and normalization are those of the standard-root Euclidean embedding of a simple unweighted cycle. Similar-looking affine polytope presentations need not preserve the Euclidean margin. Historical priority remains provisional; no independent mathematical audit or external certification has been performed.
