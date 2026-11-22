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

# Verification of sharp Laplace-filter sensitivity

The proof in `RESULT.md` is self-contained, apart from standard spectral functional calculus, Cauchy–Schwarz, dominated convergence and the matrix-exponential Duhamel identity. The rank-one witness is an **interior derivative limit**: the perturbation by the all-ones matrix is admissible for \(|h|<\delta/n\), avoiding an invalid boundary-direction argument.

Run `python3 CHECK.py` with Python 3 and its standard library; observed output: `CHECK_OK 2100 supplementary assertions; ranks, scalar filters and dimensional cases checked.` The checker exercises 1,500 random real symmetric positive contractions, exact rank-one identities over 32 dimensions, and two-eigenvalue Fréchet derivatives for heat, resolvent, fractional inverse and positive mixtures. It does not replace the all-dimensional proof or establish literature priority. No independent audit has been carried out.
