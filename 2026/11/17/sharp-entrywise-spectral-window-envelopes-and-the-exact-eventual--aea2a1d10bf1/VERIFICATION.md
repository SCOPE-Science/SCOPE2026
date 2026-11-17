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

The analytic claim is established in `RESULT.md`: (i) spectral reduction to a positive-contraction interval; (ii) exact signed eigenvalues of the rank-two symmetric coordinate form; (iii) feasible endpoint-generating rank-one projectors; (iv) derivative sign of the onset function; (v) a fixed-generator witness of all earlier negative times. The proof explicitly handles the dimension requirement, strict positivity of the eigenvector, both spectral endpoints, closed versus strict time boundaries, and the diagonal entries.

Run `python3 verify.py` from the extracted package directory. It requires only the Python standard library and reports 14,617 exact rational and floating finite diagnostic assertions, with the explicit three-dimensional onset. The script checks projector identities, two-sided bounds on sampled finite-dimensional rank-one spectral effects, endpoint eigenpair relationships, and the persistent sign switch. Its floating tests use stated tolerances. These finite checks do not certify the theorem for arbitrary dimensions or times; the proof supplies those universal conclusions.

A separate independent audit was not performed. The originality check is qualified by possible earlier equivalent matrix-inequality formulations and limitations on access to some primary works. The theorem does not address other spectral configurations, nonnormal generators, or infinite-dimensional coordinate lattices.
