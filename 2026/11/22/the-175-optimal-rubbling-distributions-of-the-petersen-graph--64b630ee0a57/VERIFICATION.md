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

# Reproducibility record

The Petersen graph is specified as the graph of all two-element subsets of a five-element ground set, with edges for disjoint pairs. A state is a ten-entry nonnegative integer vector. Each rubbling move consumes two pebbles from neighboring sources (possibly the same source) of the destination and creates one pebble at the destination. The initial vertex is also reachable by the empty sequence when occupied. Reachability is assessed for each target independently.

Execute `python3 check_rubbling.py` to check all weak compositions of totals zero through four, the complete rubbling and pebbling-only census, the induced forest spectra and all natural label-permutation orbits. Execute `g++ -std=c++17 -O2 check_rubbling.cpp -o check_rubbling` and then `./check_rubbling` for an independent queue-based traversal over the legal state space. The code includes exact integer assertions of the recorded classification and has no third-party dependencies.

The expected totals are 286 states of weight smaller than four with zero fully reachable, 715 states of weight four, 175 rubbling-solvable, 10 pebbling-solvable, and 17 permutation orbits. The six four-singleton shapes have multiplicities 5, 60, 15, 10, 60, 60 in the order printed in `RESULT.md`, with precisely the first four solvable. `orbits.csv` is a redundant tabulation; the programs do not read it and can reconstruct it.

The verification establishes a finite claim for the specified graph, not a general theorem about all graphs. It does not independently certify literature priority.
