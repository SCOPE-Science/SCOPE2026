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

Each local XOR update is an involution, so the hub-first sweep is invertible and has no transients. The exact petal recurrences h'=h+sum(a_i+b_i), a_i'=a_i+b_i+h', b_i'=a_i follow by in-place order. For odd k, aggregate (h,s_a,s_b) has Q=I+J with J^3=0, one size-three Jordan block; deviations give k-1 irreducible order-three A modules. For even k, the invariant kernel of the three aggregate coordinates evolves by A, while N=T^3+I has image in a two-dimensional constant-petal subspace and rank exactly two from exhibited vectors; hence N^2=0 and T^6=I. The rank/nullity formulas and Möbius inversion recover every primitive-period population including k=1. Independent graph-level enumeration gave P_d for k=1:{1:2,2:2,4:4}; k=2:{1:2,3:6,6:24}; k=3:{1:2,2:2,3:30,4:4,6:30,12:60}; k=4:{1:2,3:126,6:384}; k=5:{1:2,2:2,3:510,4:4,6:510,12:1020}.

## originality

PASS

Best-of-knowledge new exact sweep-period census and hub-petal parity effect for fixed asynchronous self-inclusive XOR updates on friendship graphs. Previously published graph-family result treats synchronous A/B parity semigroups; prior Rule 150 scan census applies to simple cycles, not a bouquet of triangles. Their statements do not imply this fixed hub-first sweep module decomposition.

## value

PASS

The friendship graph is a natural triangle-bouquet network, and hub-first updates are a reproducible asynchronous policy. Exact all-k primitive-cycle populations and the parity change from maximal period six to twelve resolve a concrete finite-field dynamics classification beyond general invertibility and classical cycle-graph results; the k=1 boundary and fixed-power formula are substantive and reusable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
