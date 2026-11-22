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
# Reproducibility and finite validation

Execute `python3 verify_pathbox_neighborhoods.py` using the standard Python 3 library. The program constructs the Cartesian product graph directly as coordinate tuples, generates every open-neighborhood concept by graph adjacency, enumerates all possible supports up to four vertices, and computes the realized traces without using the structural classification. It compares the resulting coefficient vectors with the algebraic formulas for the supplied lengths and raises an error on disagreement.

Twenty-one representative cases were checked, from paths through five-dimensional binary boxes, with vertex-set sizes at most 36. The tests include all \(2^k\) trace requirements for each enumerated support, not a randomly sampled subset. The successful replay ended in `ALL_PATHBOX_NEIGHBORHOOD_CHECKS_PASS`. Representative independent coefficient vectors in degrees zero through four are `(1, 12, 26, 0, 0)` for `(2,2,3)`, `(1, 16, 40, 8, 0)` for `(2,2,4)`, `(1, 27, 99, 40, 0)` for `(3,3,3)`, and `(1, 16, 48, 64, 0)` for `(2,2,2,2)`.

The verification is exhaustive for the listed *finite* boxes and *only* those boxes. Universal correctness comes from the combinatorial proof in `RESULT.md`. Source-priority checks remain literature-dependent; no independent audit or certification is represented by the checker.
