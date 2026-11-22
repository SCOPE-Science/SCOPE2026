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

## Verification and scientific boundaries

The proof uses the exact partial-domain identity \(f_{k,A}^2=f_{2k,A\cap(A-k)}\), the local cyclic-binary factorization \(b_i=a_i a_{i+1}\), and the fact that doubling on \(\mathbb Z/n\mathbb Z\) is bijective for odd \(n\). Every boundary case (empty map, one-vertex orbits, full target and all-zero target) is addressed separately. The independent standalone program `verify_square_fibers.py` directly composes all partial rotation maps through degree \(10\) and exhaustively checks local binary fibers through length \(16\). To reproduce: run `python3 verify_square_fibers.py` in the directory containing this file and the verifier.

The finite computations do not certify arbitrary-degree results; the combinatorial argument in RESULT.md is the general proof. The odd-degree density estimate is not a sharp expansion and the even-degree image-size enumeration remains open in this package. Historical-priority comparisons are limited to the inspected literature and accessible indexed records. No independent audit has been performed.
