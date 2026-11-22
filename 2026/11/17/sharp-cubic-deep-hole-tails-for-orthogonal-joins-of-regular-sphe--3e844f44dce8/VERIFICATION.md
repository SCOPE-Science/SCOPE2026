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

Verified the uniform S^3 Haar factorization into independent W~Beta(1,1), U~Unif[0,pi/p], V~Unif[0,pi/q]. Conditioning gives exact W-interval, with no clipping error. The minimax over W occurs at balance and U,V at their angular endpoints; precisely pq deepest directions. Near the corner the positive-part tent has slope coefficients A=2c^2 sin(pi/p)/a^3 and B=2c^2 sin(pi/q)/b^3, integral (2/c)^3/(6AB)*epsilon^3; O(epsilon^4) follows Lipschitz positive part and bounded support. Independent (4,4) tangent 3-simplex yields C=512/(3pi^2); independent numerics recovered (4,5) c=0.5324073960 and C=25.0913881588. No finite computation substitutes for the uniform all-pair proof.

## originality

PASS

The natural orthogonal-polygon code was already used for maximal four-volume and inradius calculations, but the mathematical surviving result is the complete Haar support-threshold CDF together with its sharp cubic deep-hole coefficient for all p,q>=3. Inspecting same-object normal-cone angles shows those identify the maximizing vertex, not the distribution of the maximum support value. Historical priority remains best of knowledge.

## value

PASS

A full covering-error distribution and sharp probability of near-worst directions quantify geometric robustness of a natural family of spherical codes, with the symmetric cross-polytope exact check and square-pentagon benchmark. The nonzero cubic coefficient and exact extremal count are mathematically motivated, not just renaming a known radius.

The dated certificate retains the supplied scientific assessment, sources and limitations.
