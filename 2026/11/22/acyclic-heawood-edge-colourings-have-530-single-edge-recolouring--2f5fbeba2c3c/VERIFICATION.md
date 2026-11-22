---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

Build the included standalone programs with `g++ -std=c++17 -O3 verify_incremental.cpp -o check_incremental` and `g++ -std=c++17 -O3 verify_incidence.cpp -o check_incidence`, then run `./check_incremental` and `./check_incidence`.

Both programs enumerate the twenty-one Fano-plane incidences without external data, canonicalize by colours at one degree-three point, and independently construct every allowable single-edge recolouring. The incremental verifier uses edge-by-edge recursion and prefix two-colour path tests; the incidence verifier uses point-by-point injections and six full-graph disjoint-set forest tests. Each produces the following agreed values: 119784 canonical acyclic states, 599760 directed arcs, 299880 undirected edges, zero quotient loops, component histogram `1x392 14x112 42x24 40040x1 76776x1`, and frozen-state count 392. The independent implementation also checks 230336 canonical proper colourings before the acyclicity filter, and fails with a nonzero exit if its exact certificate assertions are violated.

The archived output contains additional colour-class histograms and sample-source eccentricities. These sampled distances do not certify a diameter and no such diameter is included in the mathematical claim. This is a finite, exhaustive, same-model computation-based proof, not an independent scholarly audit or a statement about arbitrary cubic graphs.
