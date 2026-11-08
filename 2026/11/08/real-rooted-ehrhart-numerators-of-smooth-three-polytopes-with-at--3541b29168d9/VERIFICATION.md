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

## Exact verification

Run `python verify.py certificate.json` with Python 3 and SymPy. The verifier computes the rational Ehrhart expressions from the two five-facet classification branches, reconstructs the full Ehrhart numerator, computes the cubic discriminant both directly and through symbolic algebra, and checks all coefficients against `certificate.json`. The expected complete positive monomial lists contain 139 and 338 entries, respectively; no negative or missing monomial coefficients occur. The four-facet simplex discriminant identity is checked separately. The script also independently enumerates a finite set of lattice slices as supplementary consistency checks; these finite tests are not used to infer the theorem for arbitrary parameters.

## Boundaries

The proof assumes the smooth threefold classification and standard nonnegativity of lattice-polytope Ehrhart numerators, both cited in `RESULT.md`. Exact certificate verification requires SymPy; the certificate itself consists entirely of integer exponents and exact rational coefficients and requires no floating point. It does not establish a claim for arbitrary nonsmooth polytopes or for polytopes with more than five facets. Independent mathematical validation has not been performed.
