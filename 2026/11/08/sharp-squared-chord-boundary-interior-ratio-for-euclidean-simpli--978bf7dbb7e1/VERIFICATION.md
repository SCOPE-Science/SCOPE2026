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

# Computational and analytic checks

The analytic proof in `RESULT.md` establishes all dimensions and all nondegenerate shapes. The script `verify.py` is only a supplementary check and requires Python 3 and NumPy. Execute `python3 verify.py` in the directory containing this document. It checks the Euclidean face-area weights via singular values; calculates the two independent-point moments directly using barycentric Dirichlet pair-product expectations; compares these with the closed-form geometric identities for 280 sampled simplices in dimensions 2–8; checks the explicit two-cluster family for dimensions 2–10; and separately performs a Monte Carlo test of a nondegenerate four-simplex with smaller boundary than interior mean squared distance. The completed run returned `SIMPLEX_SURFACE_SECOND_MOMENT_OK 1204`, with a four-dimensional sample ratio `0.9685456401027323` and sharp infimum `0.9375`.

The tested examples do not establish either universal validity or absence of a better extremum. The Gram-determinant and analytic limiting calculations, strict face-normal inequality, and Dirichlet second-moment identities in the written proof do so. The numerical illustration in four dimensions is not an exact interval certificate; existence of a strict reversal for sufficiently small positive parameter follows analytically from the sharp limiting value.

No independent external validation has been performed. The historical novelty assessment remains provisional and does not certify that inaccessible publications lack equivalent results.
