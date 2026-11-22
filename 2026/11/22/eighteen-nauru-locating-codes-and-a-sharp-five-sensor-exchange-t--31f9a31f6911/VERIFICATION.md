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

The complete 24-vertex adjacency list is reconstructed in both bundled standalone checkers from the outer cycle, spokes, and inner step-five edges. `check_all_masks.cpp` enumerates all 1,271,626 subsets of cardinality at most eight and checks every omitted vertex trace without heuristic pruning; output: `VERIFY_FULL_OK tested=1271626 minima=18`. `verify_nauru.py` independently searches all 245,025 outer-four/inner-four subsets, checks the two explicit families, the 153 pairwise intersections, the reconfiguration edge rules, all 18 breadth-first-search eccentricities, and the incidence-cycle decomposition; output: `VERIFY_OK 245025_BALANCED_CANDIDATES 18_MINIMUM_CODES 3C6_THRESHOLD4 CONNECTED_THRESHOLD5_DIAMETER2`.

The elementary counting argument proves the lower bound of eight before enumeration. Enumeration proves exactness on the fixed finite graph, not on any infinite family. The two search implementations use different source languages and enumerate different candidate universes. Their agreement is a reproducibility cross-check, not independent external validation. The included programs require only a C++17 compiler and Python 3 standard library. Scientific publication priority has not received independent certification.
