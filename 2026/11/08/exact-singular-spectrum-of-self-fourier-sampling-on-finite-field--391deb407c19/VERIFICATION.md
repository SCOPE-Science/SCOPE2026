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

# Computational verification and proof limits

`python check_rankone_self.py` with Python 3 and NumPy constructs all rank-one matrix entries independently, forms the exact specified complex additive-character samples and checks numerical singular values with multiplicities against the theorem. Tests include seven field/size combinations over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), and \(\mathbb F_5\), and the successful invocation prints `RANK_ONE_SELF_FOURIER_PASS`. The checker uses floating point SVD, so its finite computations alone are not a certificate of an infinite-family theorem. The exact mathematical proof relies on projective character orthogonality, Gauss sums, and projective incidence common-neighbor identities described in `RESULT.md`.

Checks do not establish historical priority, full-spark minor nonvanishing, or an independent audit. Original full-text comparison to Delsarte (1978) remains unavailable; related formulas are accounted for as classical inputs.
