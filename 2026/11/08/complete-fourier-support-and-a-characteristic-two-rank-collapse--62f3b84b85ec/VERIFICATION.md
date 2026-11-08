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

# Verification

The complete adjugate-graph Fourier theorem follows symbolically from the polynomial adjugate-change identity, elementary polar-rank computations, and an orthogonality lemma. The separate deterministic script `check_adjugate_graph.py` uses only the Python standard library, and is run by `python check_adjugate_graph.py`.

It exhaustively checks \(512\times512=262144\) exact Fourier coefficients over \(\mathbb F_2\), finding \(62609\) supported ones, and checks all predicted signs and magnitudes by integer Walsh transforms. It tests \(221\) sampled frequency pairs over \(\mathbb F_3\) by exact cyclotomic squared norms and checks polar ranks for each tested second frequency matrix. Both tests passed in the present package. They are finite checks, not an exhaustive calculation for every prime power and not an independent audit.
