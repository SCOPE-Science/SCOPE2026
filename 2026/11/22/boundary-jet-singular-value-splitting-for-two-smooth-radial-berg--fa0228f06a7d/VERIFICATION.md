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

The proof reconstructs the exact Fourier-block beta covariance from normalized monomials, establishes the centered first and second gamma moments, and uses a Gram exterior-product to extract the small singular branch. All asymptotic quantifiers fix the weight and smooth pair as degree tends to infinity. The boundary two-jet determinant is assumed nonzero.

Run `python checks/check_jet.py` with the `mpmath` package installed. It checks 267 exact rational relations for the polynomial benchmark and 4 high-precision asymptotic comparisons for the nonpolynomial exponential example; the result is `PASS 271 finite exact-rational and high-precision assertions`. These checks are finite and do not certify the infinite-dimensional statements.

Literature priority is assessed against accessible scalar Hankel papers and closely related published polynomial-covariance and poly-Bergman commutator results. The scalar regular-weight article was accessible only in part. There has been no independent audit or external proof certification.
