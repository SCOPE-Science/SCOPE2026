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

Run `python verify_direct.py` and `python verify_structure.py` using Python 3.10 or newer. Neither has third-party dependencies. `direct_output.txt` and `structure_output.txt` contain exact captured outputs from the supplied programs.

The direct implementation enumerates all \(inom{24}{8}=735471\) eight-subsets of the four-by-six rook graph and all legal exchanges. It also identifies the minimum size and tests every nondegenerate rectangular rook board having at most 24 cells. The independent structural implementation builds the optimum classes by degree patterns and explores the finite 54-word graph by breadth-first search. Both agree on \(3189\) minima, \(2880\) exchanges, \(2109\) singleton components, \(20\) nontrivial 54-state components and nontrivial diameter \(5\).

The finite first-mobile cutoff follows exhaustive enumeration over the claimed bounded domain. The classification and exchange restrictions for the four-by-six board additionally have explicit mathematical proofs. Historical novelty is not certified by these computations. All review is same-model; independent audit has not been performed.
