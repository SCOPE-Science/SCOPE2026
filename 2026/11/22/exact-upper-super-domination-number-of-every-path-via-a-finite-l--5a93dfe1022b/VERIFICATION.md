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

## Reproducible checks

Run `python3 verify.py` using Python 3 and no external packages. The checker constructs the nine-symbol local predicate from external private-neighbor definitions; directly enumerates all possible selected subsets on paths of orders 2 through 13; verifies that the complement is an inclusion-minimal super dominating set exactly when the selected set is maximal open-irredundant; and tests the sharp integer formula in those cases. It checks the periodic construction and local factor stabilization, then BFS-enumerates all reachable automaton states, transitions and allowed finalizations and computes exact integer shortest-distance potentials.

Actual result:

```
INDEPENDENT_DIRECT_GRAPH_CHECK_PASS n=2..13 cases= 16380
SEVEN_RESIDUE_CONSTRUCTION_PASS block=0010100 tails=1,01,001,0110,00110,001010
BELLMAN_FORD_CERTIFICATE_PASS states=233 edges=403 termination_edges=58 minimum_cost=0
VERIFY_OK
```

The unrestricted inequality depends on finite enumeration and exact potentials for one finite directed graph, not on a bounded list of path lengths. The unrestricted constructive half uses the nine-window finite-factor argument. These checks are self-review only; no independent audit has been performed.
