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

Execute `python verify.py` from the directory containing this file and `verification-output.txt`. The program uses only the Python standard library. It enumerates every admissible \(r\)-element face of the defining multipartite join, independently constructs the graph from the exact disjoint-union/face predicate, performs breadth-first component searches, and checks the full bipartite edge sets and component counts. It then computes the integral graph cycle ranks by edge minus vertex plus component and compares with the symbolic closed formulas.

Seven tests passed: part-size tuples `(2,2)`, `(2,3)`, `(2,2,2,2)`, `(1,2,3,2)`, `(2,2,2,2,2,2)`, `(2,1,3,2,2,1)` and `(2,2,2,2,2,2,2,2)`. The largest directly enumerated graph has 1,120 vertices, 8,960 edges, 35 components and integral cycle rank 7,875. The saved terminal output records each case and its PASS status. Tests with two parts use \(r=1\) as a boundary sanity check, not as an assertion of the main \(r\ge2\) theorem.

The arbitrary-parameter isomorphism is proven analytically from complementary color supports. The integral representation is proven by row-and-column zero edge matrices and natural orientation reversal, rather than extrapolated from these finite cases. There is no independent mathematical audit or certification.
