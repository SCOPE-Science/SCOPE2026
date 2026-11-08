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
# Verification and reproducibility

`checks/verify.py` enumerates all faces of the closed-neighborhood complex directly from the bipartite adjacency matrix for \(n=7,8,9,10,11\). It separately generates the two shore covers, checks their exact intersection as a graph, independently computes the combinatorial Alexander dual of cycle independence sets, verifies the complete two-skeleton, and calculates reduced simplicial homology over \(\mathbb F_2\) by exact bitwise Gaussian elimination. The expected nonzero ranks are \(22\) and \(2\) in degrees \(2,3\) at \(n=7\); \(33\) and \(2\) in degrees \(2,3\) at \(n=8\); \(46\) and \(4\) in degrees \(2,4\) at \(n=9\); \(61\) and \(2\) in degrees \(2,5\) at \(n=10\); and \(78\) and \(2\) in degrees \(2,5\) at \(n=11\).

Run `python3 checks/verify.py` with Python 3 and no extra packages. Its recorded output is `checks/verification_output.txt`. Every reported finite check passed. The complete integral statement is proved in `RESULT.md`; no integer homology is inferred from the modular computation, and finite verification cannot establish the unrestricted quantifier. Independent external mathematical verification has not occurred.
