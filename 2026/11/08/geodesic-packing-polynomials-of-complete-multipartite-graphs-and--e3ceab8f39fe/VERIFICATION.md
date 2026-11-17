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

In a labelled K_{n1,...,nr} with every ni>=2, every maximal geodesic is precisely a length-2 path with two endpoints from part i and a center from a different part j, since every edge extends. A directed q_ij array of path types leaves u_i=ni-2sum_j q_ij-sum_j q_ji unused in part i; multinomial allocations, pairings and path-center bijections count it with A(q)=prod ni!/[2^k prod u_i! prod q_ij!]. A family is inclusion-maximal exactly when no unused two vertices in one part coexist with an unused vertex of another. This yields both exact integer polynomials over all feasible q and the maximality filter. For all doubleton parts, choosing k endpoint-pair parts and injecting k centers into the 2(r-k) other vertices gives the claimed falling-factorial P. Inclusion maximality gives two disjoint unused occupancy cases and exact M coefficient formula; its nonzero size spectrum is all integers ceil(r/2)..floor(2r/3), so purity iff r in {2,3,4,5,7}. Direct independent arithmetic confirmed M_6=960z^3+360z^4, M_7=12600z^4, plus all-doubleton coefficient formula through r=8. The argument proves all r and part vectors without relying on finite enumeration.

## originality

PASS

Manuel–Brešar–Klavžar introduced geodesic packings, and an October 13 published complete-multipartite theorem already determines the exact maximum gpack for arbitrary part sizes, including doubleton max floor(2r/3). This prior maximum is not novel. Neither the inspected primary article nor the complete October 13 theorem enumerates all packings, inclusion-maximal packing families, their cardinality spectrum, or the reentrant purity set {2,3,4,5,7}. Those survive as the new mathematical claims. Related P3 packing, induced path cover, and geodesic transversal notions were distinguished.

## value

PASS

Complete inclusion-maximal enumerators and a nonmonotone purity exception for a canonical multipartite family answer natural exact packing-complex questions unavailable from the earlier scalar optimum. The r=6 nonpure versus r=7 pure return is a meaningful structural classification, not an arbitrary finite sample or table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
