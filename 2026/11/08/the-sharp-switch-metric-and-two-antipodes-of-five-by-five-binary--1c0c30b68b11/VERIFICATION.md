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
# Executable verification

From the directory containing these files, run:

```
python3 verify_switch_5x5.py
g++ -std=c++17 -O2 -Wall -Wextra verify_switch_5x5.cpp -o verify_switch_5x5
./verify_switch_5x5
```

The Python program independently enumerates ten choices of five-bit row masks for each of five rows subject to five column-sum tests. It asserts \(2040\) states, \(26100\) reversible switch edges, orbit counts \(1440\) and \(600\), full orbit-specific shell profiles for **each** state, eccentricity histogram, \(1440\) diametral pairs, and the entire unordered pair distance histogram. It uses BFS over the complete generated graph and no stored distance database.

The C++17 program independently enumerates unions of edge-disjoint permutations, deduplicates them, constructs legal checkerboard switches without calling the Python generator, and checks edge reversibility, degrees, all shortest-path distances from both orbit representatives, and exactly the two displayed cyclic antipodes. One standalone source per method suffices to reproduce its own run.

Observed successful terminal lines:

```
PYTHON_EXHAUSTIVE_PASS states=2040 edges=26100 radius=5 diameter=6
PYTHON_DIAMETRAL_PAIRS 1440
CPP_SYMMETRY_PASS states=2040 edges=26100 canonical_distance_profiles_valid=true
CPP_ANTIPODES_PASS two_cyclic_shifts=true
```

The exact proof requires checking the complete finite graph. Agreement between independent enumerations and symmetry reduction is supporting evidence and does not constitute formal independent scholarly audit. This verification does not claim an all-order theorem or certify literature priority.
