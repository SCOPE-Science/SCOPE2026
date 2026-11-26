---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

There are 30 normalized Hermitian vectors of support two and 135 of support four, giving 165 points. The tangent hyperplane section at any such point is a cone over a smooth Hermitian plane cubic, and different vertices cannot share more than one line. In a Hermitian frame around an incident line, linearizing the cubic on nearby lines gives two free first-order parameters; requiring the line to continue passing through a given point imposes a linear form whose projective coefficients are that point. Distinct points thus give transverse intersection, so the off-diagonal intersection is one or zero as claimed. Adjunction gives square −3 since K_S is the Plücker class and the genus-one plane cubic has degree three. For the incidence computation, the orthogonal quotient at a point is a three-dimensional nondegenerate Hermitian space with nine isotropic points, giving 36 neighbours. Orthogonal complements of the span of two distinct points have respectively a two-dimensional radical (adjacent) or are nondegenerate of dimension three (nonadjacent), giving 3 or 9 common neighbours. The resulting identity A²=27I−6A+9J, with trace A=0, gives 36,3,−9 of multiplicities 1,120,44; subtracting 3 gives the stated characteristic polynomial. Rank 45 and b2=45 give rational Néron–Severi spanning by the divisor class map. The arithmetic projector at eigenvalue −9 gives trace (15·15−5·30+165)/60=4 and fixed span of dimension 25 including the trivial summand. An independent finite-field enumeration checked all graph and conjugation counts; it does not substitute for the intersection proof.

## originality

FAIL

Cheng's prior incidence-divisor lemma explicitly gives the geometric intersection rule for these very divisors, not merely their existence. Specializing to a cubic threefold and q=2 gives A−3I directly; its spectrum follows mechanically from the standard Hermitian point-graph parameters. Rank saturation is then an immediate combination with the published Picard rank and b2 bound, not a new generator theorem. The literal 165-curve spectrum and spanning package need not be printed as a named prior theorem for this coverage to hold.

## value

FAIL

The configuration is natural and this is a useful exposition of it. As a distinct finding, however, the proposed geometric invariant is already given by a general rule on the same divisors; the spectrum is a routine strongly regular graph deduction and the span dimension just saturates a published rank. The frozen scope leaves no independently useful unknown exact invariant or new structural consequence, for example an integral index computation, that could carry a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
