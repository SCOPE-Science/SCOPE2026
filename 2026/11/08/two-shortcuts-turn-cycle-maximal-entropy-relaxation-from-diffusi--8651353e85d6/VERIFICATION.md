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

# Verification instructions and scope

Run `python3 verify.py` in the same directory as this document. Only the Python 3 standard library is needed. The verifier constructs the unweighted, symmetric adjacency matrix for cycle lengths \(2L\), including one and two shortcuts, and diagonally decomposes it by a standalone symmetric-Jacobi method for \(5\le L\le14\). It also independently computes the Green-function resolvent eigenvectors, scalar secular roots, and several larger-length asymptotic ratios.

In the reviewed package the output was:

`VERIFY_OK 131 assertions; q0= 0.5436890126920764 lambda0= 2.3829757679062373 C= 4.94735937855514`

The explicit trigonometric cycle spectrum, rank-two perturbation bound, Green function, strict resolvent monotonicity, interlacing, and Poincaré bounds in `RESULT.md` supply the infinite-family proof. The finite checker does not certify all graphs, all parameters or any total-variation mixing statement. Independent external audit has not been performed.
