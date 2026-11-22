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

# Proof checks and reproducibility

* The operator matrix is \(S-B^{-1}S\), where \(B=D+aS\), and \(B^{-1}\) exists by the factorially dominated Neumann series of \(aSD^{-1}\).
* The monomial inverse-basis coefficients were obtained by triangular inversion and the complete adjacent mixed moment by aligning basis indices.
* The density integral is an exact application of two beta identities, Tonelli's theorem and the product-variable Jacobian, not a numerical reconstruction.
* Moment determinacy for positive and complex finite measures on \([0,1]\) follows from polynomial density in continuous functions.
* Any representing disk measure must obey the angular variation inequality; the contradiction follows from the explicit small-radius bound and the strictly positive total radial mass.
* `CHECK.py` uses only the Python standard library and verifies 421 exact-rational identities for finite series truncations, selected integer parameters and moment indices. This cannot certify the infinite-dimensional theorem by itself.
* The published original all-constant-family question appears in the 2022 article's final discussion. Historical priority remains qualified; independent review has not been performed.
