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

# Verification

The defining graph has vertices \(0,\ldots,27\), seven centers and three 7-cycles of leaves, exactly as specified in `RESULT.md`. `check_cyclic.cpp` builds the local graph and enumerates the 36 permitted four-color star templates with exhaustive domain propagation and branching. A constraint-support deletion preserves every possible full solution, because every valid full solution provides a supporting allowed tuple at each incident constraint. Enumerating all residual domain branches is therefore complete; final assignments are checked directly. Graph distances are independently computed by breadth-first search to test every candidate diameter-four clique.

`check_fano.py` separately constructs the disjointness graph on 28 noncollinear Fano triples, checks its vertex and edge counts, and verifies an explicit vertex permutation is a graph isomorphism to the cyclic model. It then enumerates whole-star assignments, rather than using the domain propagation of the first program. The full final assignment predicate checks both properness and one-or-three distinct neighbor colors; on a cubic graph this is exactly the strong odd condition.

Commands: `g++ -std=c++17 -O2 check_cyclic.cpp -o check_cyclic && ./check_cyclic` and `python3 check_fano.py`. Expected output is in `verification_expected.txt`. The reported exhaustive enumeration is finite for this one graph; no timeout or partial search is represented as a proof. The theoretical lower bound and symmetry orbit are proved in `RESULT.md`. Independent external mathematical validation has not been performed.
