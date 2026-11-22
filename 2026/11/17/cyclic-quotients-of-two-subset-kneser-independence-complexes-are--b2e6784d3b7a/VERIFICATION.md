---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For each n≥5 with gcd(n,6)=1, X_n=Ind(KG(2,n−4)) has simplex classes: star at a common ground label or one exceptional three-edge triangle. The union of star simplices equivariantly retracts to the once-subdivided complete graph, and attaching the exceptional triangles yields a C_n-equivariant homotopy equivalence to the full 2-skeleton of the (n−1)-simplex. Every nonidentity translation order≥5 acts freely on ≤3-element simplex supports; quotient is CW with one vertex, m=(n−1)/2 edge orbits and F=(n−1)(n−2)/6 triangle orbits. The selected (0,j,j+1) triangle orbit relators eliminate x_j=t^j for 1≤j<m; (0,m,m+1) yields t^n; all remaining triangle relators have signed length in {−n,0,n} and slide off the degree-n attaching cell. Result M(Z/n,1)∨((n−1)(n−5)/6)S², including true integral π1 and homotopy type. Independently reconstructed exact chosen orbit counts and attaching exponents for n=5,7,11,13,25: quotient cell vectors (1,2,2),(1,3,5),(1,5,15),(1,6,22),(1,12,92), sphere ranks 0,2,10,16,80. Complete proof is elementary gluing/2-cell cancellation, not extrapolation from finite checks. Boundary gcd(n,6)=1 excludes orders 2,3 stabilizers.

## originality

PASS

Best-of-knowledge originality after actual statement-level comparison: new scope not logically covered by primary work or published stronger indexed analogues; prior constituent lemmas and any exact known special cases are explicitly acknowledged.

## value

PASS

Exact integral homotopy decomposition and unbounded cyclic first-homology torsion of a natural symmetric quotient, not just an existing rational quotient Betti table or unquotiented sphere count. The explicit all-width cell reduction is usable where rational character methods lose torsion and homotopy data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
