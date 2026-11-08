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

Run `python verify.py` with Python, NumPy and SciPy installed. The verifier uses an explicit normalized Gaussian block and QR decomposition on the diagonal test family, computes the exact-zero lookahead, executes the row-norm deletion loop corresponding to Algorithms 3--4, and compares the true Frobenius projection error with the number of deleted columns. It independently samples the chi-square distributions defining the two stages and checks selected large-block asymptotic regimes.

The finite checks do not establish any infinite-dimensional or all-block-size claim. Those statements follow from the full analytical proof in `RESULT.md`, including the endpoint gamma-density calculation. The unusual initial-stop branch is not assigned a returned-basis meaning; the exact law applies to the defined second-lookahead event. No external independent validation has been performed.
