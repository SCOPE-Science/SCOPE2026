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

# Verification of the Hamming-graph finite-variable classification

## Mathematical proof checks

The proof is given in `RESULT.md`. Its necessary steps are the permanent \(k\)-pebble coordinatewise equality-pattern invariant (one fresh target symbol always exists when the alphabet size is at least \(k\)); the fact that this invariant preserves every equality and adjacency atomic formula; the three-name recursive definition of bounded graph distances and diameter \(d\); the fact that a maximal Hamming clique is a coordinate line of size \(q\); and a separate permanent two-pebble invariant distinguishing complete from noncomplete members. All parameter ranges, threshold equalities, and the resulting relative minimal width were checked in the displayed proof.

## Executable finite checks

From a directory containing `check_hamming_logic.py`, run `python check_hamming_logic.py` and compare its standard output byte-for-byte with `logic_check_output.json`. The program uses only Python's standard library. It constructs orbit representatives of \(k\)-tuples of vertices under coordinate permutations and symbol permutations, computes all one-pebble replacement relations, and refines the resulting bisimulation partition using *sets* of successor colors, not multiplicities. It compares both finite orbit systems under the same coloring.

The recorded run contains 14 cases spanning widths two, three and four and multiple dimensions/alphabet sizes, with 0 discrepancies between the orbit-game refinement and the theorem. In particular, it tests the boundary between alphabet sizes three and four at both widths three and four. Orbit enumeration is an exact finite computation for those sample graphs; it is not a substitute for the universal pebble strategy.

## Integrity and limits

No independent mathematical audit or certification has been performed. The source code and JSON output are complete standalone reproducibility artifacts for finite cases. The full theorem is proved by the mathematical arguments in `RESULT.md`.
