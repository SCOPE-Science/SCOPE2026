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

All lifted generating vertices are exposed within their unique color face. Squared distance of any pair is |S delta T|+2*1_(colors different), at most d+2. Equality forces colors distinct and S,T complementary. A set and its complement are both upper ideals if and only if each is a union of comparability components. The count a(I)=e(P|I)e(P|I^c) counts extensions with suffix I; empty/full contribute k(k-1) pairs, proper complementary I contribute half sum squares. For a chain the only farthest pair is empty/full. Independently enumerated antichains d=2..5 and recovered diameter pair counts 3,42,744,18600.

## originality

PASS

Qu–Lee’s 2026 paper on precisely this Cayley construction proves the facet-normal and big-M lifting descriptions in a reduced indicator coordinate system; it does not give the full one-hot Euclidean diameter graph or component-union multiplicities. Reduced and full-one-hot lifts are affinely equivalent but not isometric, so facet statements cannot be directly specialized to the present metric. The standard order-ideal suffix criterion is credited. The other Euclidean diameter records found concern different polytopes. Accepted best-of-knowledge.

## value

PASS

A canonical metric-specific lift has a natural full farthest-pair graph, with a topology-sensitive classification and exact multiplicities controlled by linear extensions and disconnected comparability components; complete classifications of geometric extremal graphs are useful even when the ambient bound is elementary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
