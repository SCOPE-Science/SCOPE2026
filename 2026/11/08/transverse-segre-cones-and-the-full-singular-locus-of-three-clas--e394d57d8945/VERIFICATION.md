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
# Verification and limits

The proof in `RESULT.md` derives a Zariski-local scheme isomorphism on each permitted nonzero-cross-Plücker chart with a product of an affine space and the affine rank-one \(2\times c\) determinantal cone. Thus its claims for every positive triple of class sizes are not extrapolations from finite computation.

Run `python check_charts.py` with Python 3 and SymPy. Its exact symbolic checks cover 30 triples in the ranges \(a=1,2,3\), \(b=1,2\), \(c=1,2,3,4,5\). It checks normalized column minors, a nonzero rank-one-point Jacobian rank of \(c-1\) and zero Jacobian at the vertex when \(c\ge2\), and ten coefficients of the Hilbert series identity. Expected terminal messages: `EXACT_CHART_AND_JACOBIAN_CHECK_OK 30`, `SEGRE_HILBERT_SERIES_AND_MULTIPLICITY_CHECK_OK`, `CHECK_OK`.

These checks do not prove global absence of additional singularities; that follows from coverage by the three Plücker chart types in the written proof. The full Jacobian singular scheme, positive-characteristic analogues, higher-rank positroids, and independent audit remain outside scope.
