---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The second coordinate is constant on each input orbit b. Writing the first coordinate f_b and the second sigma(b), preservation is f_b(a+h)−f_b(a)=sigma(b)−sigma(b−h). For b=0 the first difference is additive in h by composing translations, so sigma is affine with additive linear part L; the same functional equation makes every f_b have linear part L. Additivity is F_p-linearity; reconstruction also gives sufficiency and uniqueness for arbitrary t. For rank r set q=p^r and m=p^(d−r). The q second-coordinate outputs each aggregate m labels, and each label independently chooses one of m image cosets with q representatives. Exactly j occupied cosets give qj points and q^m(m)_j Stirling(m,j) choices. Multiplication over fibers and counting s and rank-r linear maps gives the claimed polynomial; at z=1 each rank summand counts N^N t choices per L,s. Full rank gives a bijection. The greatest proper image is qN at r=d−1 with every coset occupied in every fiber; all lower ranks are strictly smaller, and occupancy there is a bijection on p cosets in each fiber. This proves the gap and endpoint coefficient, including d=1.

## originality

FAIL

A distinct indexed record on exactly the same quandle explicitly proves the unrestricted endomorphism normal form in its proof, not merely a form for retractions. In that parametrization t is already arbitrary and independent on every label. The remaining claimed image-multiplicity law is a direct rank count and application of the classical occupancy formula to independent fibers; its support bound and endpoint are obtained by filling those fibers. The overlap is explicit for the normal form and by mechanical implication for the census, not a claim that the exact generating polynomial is printed in the other record. Both catalogue dates are the same and historical ordering is not established.

## value

FAIL

This is a natural image-counting invariant and the formula is correct and convenient. But in the already recorded unrestricted parametrization, the claimed increment is only independent balls-in-boxes counting and a maximal-degree bound, with no new constraints on quandle images or genuinely separate structural remainder. The narrow exact result does not meet the requirement of an independently useful unknown fact not mechanically implied by the established parametrization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
