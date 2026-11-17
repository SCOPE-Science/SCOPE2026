---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

PASS — Direct coefficient extraction from F^6 over characteristic seven gives diagonal Hasse–Witt entries (lambda,lambda,mu) with lambda=2b(a-2)^2((3b^2+4)a+4b^2+1) and mu=4(b^2-2a)(a+b^2+1)(a-2b^2-1). On the stated smooth open set U, factor exclusions give exactly five irreducible smooth reduced divisor components, no same-group intersections, and seven simple transverse crossing points. Independent F49 arithmetic exhaustively checked all 2401 ordered pairs and gave 2163 smooth, with strata 7,84,128,1944, exactly seven superspecial and nonzero crossing Jacobian determinants. Symbolic plane coefficient verification source was inspected; full algebraic-closure completeness follows from the factorization and branch exclusion, not from F49 enumeration. Diagonal Frobenius semilinearity makes p-rank the number of nonzero diagonal factors; a-number is 3 minus matrix rank.

## originality

PASS

PASS with explicit partial prior coverage — the previous general three-parameter normalized Ciani quartic result already determines the 23 superspecial Hasse intersection points in characteristic seven, and specialization b=c accounts for the seven superspecial points here. They are NOT new in isolation. The assessed surviving result determines the entire positive-dimensional reduced nonordinary divisor of the natural D8-symmetric two-parameter subfamily, its five components, seven transverse singularities as divisor incidence, four p-rank/a-number strata and coefficient counts over F49. These full rank loci are not provided by the earlier finite superspecial-point scheme. No prior full decomposition of this slice was found.

## value

PASS

PASS — The geometry of Hasse-divisor components and their rank strata in a natural involution-symmetric genus-three family is a meaningful arithmetic-geometric classification; it records where ordinary degeneration occurs and how geometric components intersect. Explicit F49 coefficients give a checkable finite-field invariant. Value is in the divisor and rank stratification, NOT restating the seven known superspecial points; no unmarked isomorphism-class claims are made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
