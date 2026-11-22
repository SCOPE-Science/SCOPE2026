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

# Reproduction and limits

The two standalone source files in `verify/` were actually compiled or executed and checked:

- `python3 verify/check_direct.py` emitted `PETERSEN_DIRECT_PASS faces=5886 facets=1930 facet_orbits=19 bad_cotrees=70` after exhaustive forest/connectivity, cycle-type, orbit, purity and exchange tests on all 32768 possible edge supports.
- `c++ -std=c++17 -O2 -o /tmp/petersen_check verify/check_traces.cpp && /tmp/petersen_check` emitted `PETERSEN_TRACES_PASS trees=2000 faces=5886 facets=1930`. It reconstructs the graph and counts traces directly from all 2000 spanning trees, without using the first program's forest/complement criterion.

The graph is defined internally as \(KG(5,2)\) with a canonical edge order. No input files, randomness, external packages or network access are needed. Computation proves the finite graph result by exhaustiveness of explicitly bounded loops, not any unbounded generalization. The cycle and group interpretations are explained in the proof. These source checks are not independent external scientific validation.
