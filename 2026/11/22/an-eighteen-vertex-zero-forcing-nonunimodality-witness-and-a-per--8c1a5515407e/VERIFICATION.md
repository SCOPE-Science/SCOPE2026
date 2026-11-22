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

# Reproducible checks

Compile and run: `g++ -O2 -std=c++17 verify.cpp -o verify && ./verify`.
Run independently: `python3 quotient_check.py`.

`verify.cpp` expands the 12-block quotient at the base parameter and applies the original graph forcing rule for all 262144 white subsets. It checks symmetry, connectivity, 105 edges, the full polynomial, and the three strict coefficient values \(690,678,680\). This is exhaustive finite verification, not a heuristic sample.

`quotient_check.py` tests all 4096 subsets of the 12 blocks and counts their successful vertex selections at missing-block cardinalities 3, 4 and 5. It verifies the respective triples of mask counts \((214,247,214)\), base multiplicities \((680,678,690)\) and affine expansion slopes \((112,64,68)\). The analytic proof in RESULT.md verifies that the quotient procedure characterizes every zero-forcing set and that the membership of successful masks does not change with the expansion parameter. Thus the infinite claim does not depend on enumerating unbounded graphs.

The only unsolved minimum-order question is whether some graph with fewer than 18 vertices has a nonunimodal zero forcing polynomial. No such negative statement is certified here. Independent audit and global prior-literature completeness were not performed.
