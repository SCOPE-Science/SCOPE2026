---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Inspected the exact 21 listed integral 3-vectors, the 37 supporting 3D facet planes, all 37^2=1369 side facets and two base facets of the specified 8D free-sum/pyramid embedding. The seven active side normals with positive weights 14,3/2,3/2,1,1,9,9 plus base weights 111,74 cancel every center coordinate, giving R<=222/(257+14sqrt15+3sqrt23+2sqrt770). A symmetric center satisfies seven active equalities; an independent enumeration of all 37 facets and 1362 nonactive side slacks produced positive minimum slack 0.002278226939043... . The original VERIFY.py implements exact rational sqrt intervals via isqrt, not just floating comparisons; its code was read. Differences of three swapped active pairs have determinant 148, fixing the two 3-blocks and establishing uniqueness. The max squared facet normal 1525 gives origin-centered ball radius 1/sqrt1525. Independent high-precision approximate checks corroborate exact analytical inequalities; this exhaustive finite construction is self-contained for one specified polytope, not an infinite family.

## originality

PASS

The 44-vertex/1371-facet 8D reflexive polytope and pyramid/free-sum facet construction are Hofscheier-Nill prior work. They do not give its nine-facet active Chebyshev center, radius radical or 22.7x origin comparison. Searches of matching geometric invariants and published Resultary records found only different polytopes. Novelty is strictly the metric calculation for the original coordinate embedding, not the combinatorial counterexample.

## value

PASS

An exact Euclidean inball and nine-contact certificate for a uniquely distinguished small-dimensional counterexample to reflexive facet bounds is a naturally motivated metric invariant. The large separation from lattice-origin radius quantifies the difference between lattice facet normalization and Euclidean centering. Full 1371-facet feasibility, uniqueness and sparse contacts are nonroutine and independently useful although the theorem covers one canonical polytope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
