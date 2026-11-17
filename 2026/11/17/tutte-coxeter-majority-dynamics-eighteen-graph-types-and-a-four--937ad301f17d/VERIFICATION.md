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

The mathematical rule, six-symbol duad–syntheme geometry, and exactly enumerable state spaces are defined in `RESULT.md`. Both standalone checkers use only Python 3's standard library.

Run `python3 check_duad_syntheme.py` and `python3 check_vertex_dynamics.py` after extracting these files into one directory. Their outputs are captured respectively in `check_duad_syntheme_output.txt` and `check_vertex_dynamics_output.txt`. Every asserted equality is an integer or bitwise equality. The programs enumerate 32,768 states on each bipartition shore; the global \(2^{30}\)-state conclusions then follow from the proved coordinate factorization. The second checker independently constructs explicit 30-vertex adjacency and runs 12,032 direct full-graph comparisons as an additional test, not as a substitute for the exact shore computation.

The complete-entry statistics and the eventual period refinement are checked independently by the two scripts. The 156 six-vertex graph-relabelling classes and 18 recurrent classes are checked in `check_duad_syntheme.py` by generating the 720 permutations of the base set. The result is not a claim about all other cubic graphs, nor has an external independent audit been performed.
