---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Independently enumerating the 13 points and line incidences gives no nontrivial blockers of sizes 0–5 and 234 of size six, a single projective orbit with stabilizer size 24. Solving via all sign patterns on the seven nonzero evaluations of a form with a fixed zero set gives 567 candidates. The evaluation matrix on those 13 points has rank 12; the rank-six restricted matrix in the frozen proof and its nine-dimensional kernel are consistent with the separate reproduction. Euler's degree-four identity in characteristic three makes the homogeneous gradient vanish exactly at singular points. Testing its ideals on disjoint affine strata by exact Gröbner bases leaves 222 geometrically smooth forms; a separate exact Buchberger reproduction agreed. Independent polynomial substitution shows that the frozen representatives have disjoint stabilizer orbits of sizes 24 nine times and 6 once, with union equal to the smooth candidate set. Multiplication by 234 gives 51,948 and the displayed global orbit sizes. Point counting in independent explicit extension fields gives (N2,N3)=(12,33),(10,33),(16,30),(8,27),(10,36),(14,39),(12,42),(12,36),(16,45),(12,18), with N1=6 in every row. Newton identities and the genus-three functional equation give all the displayed coefficients, with ten distinct pairs (c2,c3). For the Jacobians, the zeta numerators are the reciprocal Frobenius characteristic polynomials, so distinctness gives nonisogeny over F3.

## originality

PASS

Pass is for the arithmetic separation and the attached Weil data, not for the incidence/orbit census in isolation. An earlier comprehensive orbit table already determines the ten embedded classes and the total 51,948 by a direct filter, which was actually performed. It omits counts over F9 and F27. The abstract LMFDB isogeny table does not label realizations by these quartic equations. No inspected earlier exact table matches these ten quartics to their polynomials or supplies an implication that the ten polynomials are distinct without the additional arithmetic computation.

## value

PASS

The natural genus-three locus is singled out by minimal projective blocking incidence, not by an arbitrary coefficient slice. Merely recovering the ten orbits from the earlier dataset is not an independent contribution. What matters is the exact image of the locus in Jacobian isogeny classes: even with common N1, no two of the ten arithmetic types coalesce. The two new extension counts per class and the resulting invariant give a complete checkable answer to that natural collision question; this is not a recomputation of the flex table or the abstract isogeny catalogue.

The dated certificate retains the supplied scientific assessment, sources and limitations.
