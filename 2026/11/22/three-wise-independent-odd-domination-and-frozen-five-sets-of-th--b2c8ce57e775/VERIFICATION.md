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

The file `verify_direct.py` constructs the graph with its 18-cycle and nine chords, evaluates the closed-neighborhood parity equation on all 262,144 vertex subsets, checks every triple of vertices and all membership patterns, reproduces the complete minimal-set family and its pair intersections, and measures the three-replacement graph by independent breadth-first searches. It also checks nonexistence of connected odd-dominating solutions.

The file `verify_algebra.cpp` independently constructs the Pappus graph with its LCF representation and checks the matrix rank (11), nullity (7), seven kernel vectors and all column-XOR tests of support at most three. Its own complete 262,144-subset enumeration confirms 18 weight-five, 92 weight-nine and 18 weight-thirteen solutions and the geometric minimum-set family.

The source files can be run using `python3 verify_direct.py` and `c++ -std=c++17 -O2 verify_algebra.cpp -o verify_algebra && ./verify_algebra`, requiring no third-party packages or downloads. Both were replayed after extraction from the delivered package and passed.

The structural argument proves the minimum-set characterization and uses independent finite rank certificates to determine the whole weight spectrum. All exhaustive computations are finite and complete; there is no claim about infinite families, external expert certification or independent audit.
