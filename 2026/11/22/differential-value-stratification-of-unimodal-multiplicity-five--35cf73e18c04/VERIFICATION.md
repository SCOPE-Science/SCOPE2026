---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Theorem 3/Table 2 and §§5.1–5.2 of the normal-form source cover exactly the four stated multiplicity-five unimodal semigroups and permit the stated coefficient domains. The image of differentials is preserved by the formal chain rule; an invertible reparametrization preserves order. Differentiating a ring element of positive value n gives differential value n in characteristic zero. Computing the semigroup complements gives conductors 10,10,14,12 and the displayed gap lists. In the first two semigroups distinct generator values and the first nonconstant coefficient contribution at value at least 10 exclude all gaps; for ⟨5,7,8⟩ the only possible nonconstant contribution below value 12 is a multiple of x dx with value 10, so no value 11 arises. For ⟨5,6,9⟩ only gap 13 needs a jet calculation: coefficients modulo t^9 are spanned by 1,x,y. Of the resulting products, dx,dy,dz,x dx have distinct leading values 5,6,9,10; the remaining products in coefficient degrees 10,11,12 have rows (6,7,8b),(5,5,5b),(0,6,13), with determinant 60b−65. In the discrete family the rows are (6,0,8c),(5,0,5c),(0,6,0), determinant 60c. The first two columns have rank two in either case, so a pivot in coefficient degree 12, i.e. differential value 13, occurs exactly for b≠13/12 or c=1 respectively. The conductor gives the full tail of differential values, and the valuation filtration counts colength by the missing positive values. This checks all parameters symbolically, including the exceptional exclusion stratum.

## originality

PASS

The justified distinct claim is the evaluated differential-value stratification of these normal forms, particularly the exact excluded coefficient in the continuous family, not the analytic classification or a new computation algorithm. No different inspected source supplies the same evaluated invariant; priority is provisional.

## value

PASS

A recent natural complete analytic classification supplies the scope rather than an arbitrary finite sample. Within a positive-dimensional moduli family the normalized differential invariant identifies an exact exceptional stratum that the semigroup cannot see. The full low-multiplicity census also closes the remaining possible gaps and gives the colength usable without repeating the differential calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
