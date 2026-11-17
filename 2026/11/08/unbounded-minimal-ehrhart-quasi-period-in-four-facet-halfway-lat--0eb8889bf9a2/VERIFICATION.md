---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The determinant-q integer map (x,y)->(u=x,v=x+qy) bijects lattice points with congruent integer pairs u=v mod q within an N=t+1 (even t) or N=t (odd t) consecutive-integer interval. Counting residue occupancies yields exact all-t formula, including t=0. Constituent polynomials have linear coefficient 2delta/q, forcing any period T even. At odd residue s=q, constant term zero requires r_(q+T)=0, hence q|T. Therefore 2q|T, and the formula supplies 2q, proving minimality; direct facet checks show primitive normals, area 1/q, no facet lattice points.

## originality

PASS

Qualified PASS: the demonstrated nonunimodular family and exact sharp minimal period are not consequences of inspected unimodular Pick-type or half-integral-vertex findings; general Ehrhart period bound alone only gives divisibility.

## value

PASS

It addresses a natural arithmetic boundary: primitive facet normals at half-lattice offsets do not control minimal Ehrhart period without unimodularity. A complete explicit q-family demonstrates unbounded sharp period under strict geometric constraints, rather than a random numerical table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
