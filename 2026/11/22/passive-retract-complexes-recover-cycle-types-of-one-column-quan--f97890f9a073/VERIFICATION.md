---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Extend the permutation by fixing 0. Every right translation is either the identity or this permutation; right translations preserve the flag of whether an input equals 0. This gives self-distributivity, as well as idempotence and bijectivity of each right translation. Nonidentity makes 0 intrinsic. A map into the positive elements has trivial target operation, so the homomorphism equations say exactly that it is constant on each positive permutation cycle, with f(0) freely chosen. Composition-idempotence says it fixes its entire image. For a nonempty proposed image T of size s, these requirements are compatible exactly when T is a partial transversal. Then s cycle values are prescribed, r-s cycle values and f(0) are independent choices in T, and there are s^(r-s+1) maps. The top degree of either polynomial is r, including when r=1. Dividing the weighted coefficients by the known factors recovers the elementary symmetric functions; the monic polynomial with those coefficients recovers all lengths, including repeated lengths and fixed points. A bijection fixing 0 is an isomorphism exactly when its positive restriction intertwines the permutations. For (4,4) and (2,6) the ordinary polynomial agrees and the rank-2 coefficients are 32 and 24. The finite verifier and recorded checks were inspected, not executed; the proof covers all sizes and counts maps onto each specified image, not just counts by rank.

## originality

PASS

Cazet's conjugacy classification and ordinary polynomial are known; the closest Hom theorem also supplies the single-cycle case. The distinct claim is the prescribed-image census and the two complete passive invariants for arbitrary cycle profiles. The checked transformation-centralizer and Alexander constructions impose different homomorphism laws and their image classifications do not specialize to the stated family.

## value

PASS

The passive stratum is intrinsic rather than an arbitrary choice of labelled subsets. Its complete embedded image description and per-image multiplicities give two readily computed complete invariants that separate actual collisions of the ordinary polynomial. This is more than a new proof of the known conjugacy classification: it shows how much the intrinsic retract data sees, with no enumeration of all self-maps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
