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

# Reproduction

Using Python 3 and its standard library, run `python3 verify.py` in the directory containing this file and the checker. The checker constructs every permitted length-\(n\) word independently, forms its directed shift edge, and computes exact integer Laplacian cofactors with fraction-free elimination. It compares the exact cofactor with the closed formula, checks the entire determinant at three independent integer arguments, and counts fixed-edge Euler tours directly in six small instances without using the BEST theorem. It prints `VERIFY_OK` on completion.

The verified parameter cases include alphabet sizes \(q=2,3,4\), orders \(n=2,3,4\) where the graph has at most 64 vertices, and the additional case \((q,n)=(2,7)\). Direct traversal counts are \((q,n;U)=(2,2;1),(2,3;2),(2,4;16),(3,2;2),(3,3;864),(4,2;6)\). The checker output was reproduced from the same `verify.py` incorporated in this package. No sampled or finite determinant evaluation establishes an all-order theorem; that proof is presented in `RESULT.md`.

Scientific limits: one distinguished required symbol; labeled alphabet; all length-\(n\) cyclic windows containing it exactly once; no reversal/letter-permutation identification; not a claim about multiple required symbols. The result has undergone self-review only. No independent mathematical verification has been performed.
