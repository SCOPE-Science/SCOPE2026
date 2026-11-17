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
# Exact finite checks and proof boundaries

Run `python3 check_geometry.py` from the same directory as this file. Only the Python standard library is needed. A successful run asserts the precise finite claims below, and reports rational interval brackets for the radical center and the least remaining facet margin.

**Exact combinatorial checks.** All \(3^6=729\) orientations/absences of six unordered node-pairs are examined, filtered for acyclicity and maximum indegree two, and mapped to characteristic imsets: 150 distinct vertices. All 94 coefficient vectors and right-hand sides are generated from the published finite facet families. Exact integer dot products check every inequality on every vertex. Modular full-rank witnesses verify affine dimension 10 and, independently for each inequality, a 9-dimensional tight face. The modular witnesses certify nonzero integer determinants, so they provide valid lower bounds on characteristic-zero rank.

**Exact metric checks.** Integer-square-root enclosure at scale \(10^{10}\) bounds all occurring square roots using exact rationals. The resulting closed rational intervals prove that the proposed center has more than \(9/200\) Euclidean extra supporting-plane clearance at all 88 noncontact facets. All six designated contacts hold by exact algebraic identities. A three-line upper bound from the four nonnegative triple facets and the two global path/clique facets proves that no other center has a larger radius. Equality and the strict certificate yield precisely the stated affine dimension and relative-interior contact classification.

**Limits.** The finite checker uses the source's complete facet families and reproduces the resulting 94 facets, but cannot establish the source's general H-description theorem independently. The result concerns this one four-node, degree-two, ambient-Euclidean realization. Numerical optimization is not a substitute for the exact upper bound and rational feasibility proof. Independent scientific audit and independent validation are not performed.
