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

# Exact checks and scope

Execute `python3 verification/verify.py` from the package root. It uses only the Python standard library. The program directly builds the six-by-six Cartier semilinear matrix for the differential basis in `RESULT.md`, composes iterates using Frobenius square roots, and computes finite-field ranks by Gaussian elimination. Its finite-field squarefreeness test uses the polynomial Euclidean algorithm and formal differentiation.

The exhaustive \(\mathbb F_4\) computation considers every coefficient tuple of a monic degree-seven polynomial, retaining precisely the squarefree tuples; it finds 9,216 rank-four cases, 2,304 rank-two cases, and 768 rank-zero cases, each matching the complete predicted six-term Cartier rank sequence. It also checks three explicit \(\mathbb F_2\) witnesses and 898 cases over \(\mathbb F_8\), including all possible values of the sixth-degree coefficient on the proposed rank-zero locus. Its complete recorded stdout is `verification/output.txt` and ends `ALL_CHECKS_PASSED`.

A finite-field computation is not a proof for arbitrary algebraically closed characteristic-two fields. The infinite quantifiers, smoothness, differential basis, semilinear matrix formula, rank-one twisted composition and graph geometry are handled by the explicit algebraic proof in `RESULT.md`. No independent scientific validation or formal certification is asserted.
