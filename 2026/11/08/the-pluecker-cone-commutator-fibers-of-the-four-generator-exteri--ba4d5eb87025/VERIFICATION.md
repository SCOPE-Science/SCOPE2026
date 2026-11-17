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

For E=Lambda(F_q^4), q odd, even components central and each input has 8 even coordinates, giving q^16 free pairs. Writing odd input u+alpha, v+beta, the commutator is exactly 2(u wedge v+u wedge beta+alpha wedge v). The six degree-two coordinates satisfy the one Plucker Pfaffian equation iff decomposable. A fixed nonzero bivector has q(q²−1) ordered u,v pairs, while the zero bivector has q^4+(q^4−1)q dependent pairs. The top-degree linear form on 8 alpha/beta variables is rank one for (u,v)!=(0,0), yielding q^7 inputs per t, and rank zero for the zero pair, yielding the exceptional zero-fiber q^8. These facts yield all four cases and commuting probability q^(-4)+q^(-5)-q^(-9). Alternating rank<=4 gives width two, and rank four forbids width one. An independently coded F3 wedge-frequency enumeration found exactly 261 output bivectors, zero pair count 321 and each nonzero simple fiber 24, matching q formulas. This finite test corroborates, not replaces, the proof for all odd prime powers.

## originality

PASS

Earlier all-arity exterior-four commuting-variety theorem already supplies the commuting probability at m=2 and structural adjoint ranks; this portion is not new. Its actual full theorem does not compute the image of a NONZERO commutator, all nonzero fibers, or the Plucker image cone with free top coordinate. Classical Plucker relation and SL2 counting are known; the uniform full associative-commutator fiber distribution is best-of-knowledge original. Same-family five-generator enumerations and general polynomial-image papers do not logically imply the stated four-generator distribution without new specialization.

## value

PASS

An exact, nontrivial finite-field commutator map image and every fiber for a familiar noncommutative sixteen-dimensional algebra is a natural complete classification, including central-axis exceptions and width. It gives quantitative refinements of the published commuting-tuple law. It is not merely rediscovering the Plucker equation or counting commuting pairs; its substantive object is full fiber geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
