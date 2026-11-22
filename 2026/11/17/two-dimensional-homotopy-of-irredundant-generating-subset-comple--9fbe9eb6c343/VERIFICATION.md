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

The exact generated-subgroup formula gcd(n, rotation exponents, reflection differences) determines membership under deletion of every element. It gives only the three listed triangle classes and rules out independent four-subsets, including p=2. The core on order-p, order-q and reflection vertices is two-dimensional with f0=n+p+q-2, f1=3n(p+q-2)/2+h and f2=2nh, n=pq, h=(p-1)(q-1). An explicit spanning tree plus all corresponding triangle relations kills pi1, so Euler characteristic and integral Hurewicz/Whitehead imply a wedge of beta2 two-spheres. Each primitive-order rotation attaches n spokes (n-1 new circles) and each reflection pair differing in both residues contributes an independent edge circle, yielding beta1. Independent subgroup-oracle enumeration p,q=(2,3),(3,5) gives (V,E,T)=(11,47,24),(29,323,240) and computed betas (16,3),(172,117). This checks finite boundaries, not unrestricted primes.

## originality

PASS

Best-of-knowledge finding after comparing actual statements and consequences, not titles. The four structured checks and specific full/partial source inspections below separate previously known inputs from surviving contributions.

## value

PASS

A complete homotopy and free fundamental-group classification for a natural group-theoretic simplicial complex over an infinite squarefree dihedral family, with explicit torsion-free integral ranks and the even-prime boundary. Its face predicate is irredundance, sharply different from the previously studied nongenerating Frattini complex; the natural mixed-dimensional wedge and complete classification are motivated structural invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
