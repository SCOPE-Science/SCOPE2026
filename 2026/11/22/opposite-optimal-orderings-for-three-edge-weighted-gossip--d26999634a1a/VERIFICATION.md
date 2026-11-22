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

# Reproducibility and verification

The standalone `verify.py` runs using Python 3 and SymPy. Invoke `python verify.py` in the directory containing it; no data files, network access, or unpublished external dependencies are needed.

The checks performed here included the exact symbolic identity
\[
E_{(a,b,c)}-E_{(a,c,b)}=4abc(1-a)(c-b),
\]
reversal invariance, reconstruction of six rational four-by-four update products, the order-independent determinants \(\prod(1-2p_i)^2\) and \(32\prod p_i(1-p_i)\), and exact isolation of the three nontrivial squared singular eigenvalues for each order. A rational witness \((1/8,1/4,3/8)\) certified the strict opposite middle-position rankings for the Frobenius and top singular-value losses. Another 24 distinct rational triples were checked across all six orders.

The general proof does **not** rely on testing random coefficient grids, floating-point root rounding, a search for negative examples, or the absence of literature matches. The determinant identity on the mean-zero space and the monotonicity argument establish the all-real-parameter claim analytically, including coincident parameters. The verifier checks finite test instances and symbolic algebra, not the completeness of a worldwide literature survey.

Self-review: passed. Independent audit: not yet performed.
