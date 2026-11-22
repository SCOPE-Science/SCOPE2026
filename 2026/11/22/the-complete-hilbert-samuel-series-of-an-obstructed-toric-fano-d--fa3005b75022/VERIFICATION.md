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

# Verification of the Hilbert–Samuel computation

Execute `python verify_hilbert.py` with SymPy installed. The checker implements the ten defining homogeneous polynomials over \(\mathbb Q\), the graded reverse lexicographic monomial order, and the published qG deformation-ring decomposition. It independently verifies that the computed twelve polynomials form a Gröbner basis by testing all 66 Buchberger S-pairs, all ten original generators, and the expected twelve leading monomials.

It then obtains the *whole* Hilbert numerator by exact lcm inclusion–exclusion over the twelve initial monomials, checks degreewise standard-monomial counts through degree ten, checks the nilradical Hilbert-series identity against the reduced union of linear spaces, and checks the two-factor/six-free-parameter formula. All computations use exact rational integers and polynomials. The direct degreewise count is only a cross-check; the proof for all degrees is the Gröbner/monomial-ideal identity.

This verifies an invariant of the specified formal qG deformation hull; no claim is made about automorphism invariants of the moduli quotient, about nearby K-stable varieties, or about historical mathematical priority.
