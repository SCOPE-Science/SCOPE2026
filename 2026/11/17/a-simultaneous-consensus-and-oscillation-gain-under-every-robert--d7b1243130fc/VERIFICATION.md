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

State definition is exact: 2^19=524288 bit assignments; open-neighbor strict majority with incumbent tie retention. Reconstructed 19×4 adjacency and 38 edges. Exhaustive integer successor maps give baseline (H,C,U,T)=(6508,2166,295138,11); edge-class (1,2) gives (3772,2670,309046,11), (1,3)=(3584,2478,310832,12), (3,9)=(3620,2490,312052,12), (3,10)=(3622,2518,311104,12). Python automorphism calculation gives four orbits of multiplicities 2,12,12,12, totaling all 38 edges; C counts cycles (half of primitive period-two state population), U counts initial states whose terminal attractor is 0 or 2^19−1. Independent full state-space vectorization reproduced all five tuples and the source C++ visits all 38 deletions. Hence exhaustive finite theorem, not sample or asymptotic impossibility claim.

## originality

PASS

Classical symmetric threshold theorems guarantee eventual period≤2 but do not yield exact 19-vertex orbit/basin census or simultaneous edge-response inequalities. The published analogous Chvátal-graph one-edge study concerns distinct 12-vertex graph and different two-cycle behavior.

## value

PASS

A full exhaustive one-edge perturbation classification on the natural smallest 4-regular girth-five cage reveals the simultaneous enhancement of unanimous convergence and period-two oscillation despite loss of fixed points; these are competing natural observables. It is a motivated exact finite classification across all 38 edges, not an arbitrary tiny sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
