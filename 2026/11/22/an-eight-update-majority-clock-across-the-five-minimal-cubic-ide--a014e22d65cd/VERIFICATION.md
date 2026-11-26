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

The graph inputs are connected, simple, cubic, asymmetric and pairwise nonisomorphic. The degree-three open-neighbor update uses the threshold two, so there are no ties. An independent computation reconstructed the LCF edges, matched the supplied edge catalogue, enumerated all 20,480 states across the five graphs and reproduced every field of the full census, including the individual basin-size histograms, entry histograms, and witnesses. The proof counts time from the initial configuration, and F^(t+2)(x)=F^t(x) holds exactly when the state at t is recurrent of period dividing two. All states satisfy this at t=8; maximal depths are 7,7,7,7,8 and the only states at depth eight are G5 integers 486 and 3609. Completeness of the graph class was also checked independently: by processing vertices in BFS discovery order and assigning each new neighbor the next available label, the generator covers at least one labeling of every connected simple cubic graph. At each step it considers all compatible old-neighbor choices and all feasible numbers of new neighbors. Exact distance-preserving bijection search (which preserves adjacency exactly at distance one) classified orders 4,6,8,10,12 into 1,2,5,19,85 classes and found 0,0,0,0,5 asymmetric ones. The five at order 12 match G1–G5 one-to-one. Odd orders are impossible by degree parity and orders below four are impossible for a nonempty simple cubic graph; a disconnected asymmetric cubic graph would require every component to be asymmetric, so it cannot contribute at or below this minimum.

## originality

PASS

Credit the earlier same-update Frucht baseline for much of G3 and the classical result for eventual period at most two. The supported distinct claim is the complete five-member class comparison, its sharp uniform eight-step entry time with two witnesses on G5, and the exact class basin and clock census. The inspected prior results do not give or imply that claim.

## value

PASS

The study is of the canonical smallest asymmetric cubic class, rather than five arbitrary inputs, with a standard dynamics and invariants. The complete class comparison resolves its worst-case clock, exhibits the unusually small sharp-witness set, and shows that a ranking by number of recurrent oscillating orbits does not rank the size of their attraction populations (notably G3 versus G2). The full basin and entry data are useful exact benchmarks for these minimal graphs, beyond the already known qualitative period bound and the earlier single-graph baseline.

The dated certificate retains the supplied scientific assessment, sources and limitations.
