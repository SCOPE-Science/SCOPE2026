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

# Exact verification and limitations

The analytic proof derives the Ehrhart polynomial from a lattice-slice sum, the numerator from a binomial inverse transform, and the root classification from exact discriminant formulas. The attached `verify.py` implements an exact rational/integer certificate using no external dependencies:

- The original slice sum and proposed factored formula are polynomial in \((c,t)\) of bidegree at most \((3,4)\). Their equality on a complete \(4\times5\) grid therefore proves the identity for every value of the variables, and in particular every integer \(c\ge0\), \(t\ge0\).
- The numerator identity is checked from the standard binomial transform at four parameter values; both sides have parameter degree at most three.
- The cubic discriminant formula is a degree-at-most-ten polynomial identity checked at eleven distinct parameters.
- Additional exact tests cover coefficient-sign transitions, discriminant signs, and the published \(c=12\) example. The tests are supplementary to the sign arguments in the proof.

Running the provided script outputs `VERIFY_OK 658`. This is a same-model reproducibility check; independent mathematical audit has not been performed. No claim is made about the complete class of smooth four-polytopes or about unindexed historical priority.
