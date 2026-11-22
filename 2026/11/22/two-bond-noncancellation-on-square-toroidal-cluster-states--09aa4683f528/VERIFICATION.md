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

# Computational verification
Run `python checker.py` with Python 3 and no external dependencies. The checker independently constructs the binary checkerboard adjacency matrices, removes actual edges by toggling their entries, and checks ranks by exact bit-vector elimination. It tested every two-edge set on \(C_{2m}\square C_{2m}\) for \(m=2,3,4,5\), and 1,800 seeded distinct two-edge samples for each \(m=6,7,8\); 36,480 pairwise tests passed. It tested every individual edge for all seven sizes, and checked the baseline entropy ranks. It separately confirmed the disjoint-two-edge cancellation example on \(C_4\square C_6\) (intact rank 10, each one-edge rank 11, joint rank 10).

The output is recorded verbatim in `checker-output.txt`. These checks are finite and cannot establish the universal quantifier \(m\ge2\). The algebraic proof in `RESULT.md` supplies that argument using diagonal orbit parity, kernel-evaluation separation, and rank-one/rank-two updates. No numerical floating-point approximation is required for the verification.
