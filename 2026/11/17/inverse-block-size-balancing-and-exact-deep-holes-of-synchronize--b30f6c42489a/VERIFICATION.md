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

# Reproducibility and boundaries

Run `python verify_block_parity.py` using Python 3 and the standard library. This code enumerates all binary cube vertices and all parity-synchronized codewords for these ten block-size profiles: `(1,1,1)`, `(2,2,2)`, `(1,2,3)`, `(2,2,3)`, `(1,1,2,2)`, `(1,2,2,2)`, `(2,2,2,2)`, `(1,1,1,1)`, `(2,3,3)`, `(3,3,3)`. For every cube vertex it constructs the exact rational projection from the theorem, tests the defining Euclidean normal-cone inequality against *every* codeword, and verifies the squared-distance formula and maximum over parity profiles. It confirms that the nearest-point expression lies in the convex hull via the explicit two-distribution construction in `RESULT.md`; the normal-cone inequalities separately certify that this feasible point is nearest. Expected final line: `PARITY_BLOCK_HAUSDORFF_KKT_PASS`.

Optionally run `python verify_qp.py` with NumPy and SciPy. It independently minimizes squared distance over all nonnegative convex-combination coefficients summing to one, using the codewords only and not the proposed projection as a constraint or initial point. It checks all violating cube vertices for `(2,2,2)`, `(1,2,3)`, `(2,2,3)`, and `(1,1,2,2)`, with absolute squared-distance tolerance `1e-8`, and prints `PARITY_BLOCK_INDEPENDENT_QP_PASS`. The largest observed discrepancy was below `2e-13` in these tests.

These are *finite* checks, not an exhaustive proof for arbitrary block sizes and block counts. The all-parameter correctness argument is the explicit lower-bound/equality construction and residual-variance proof in `RESULT.md`. No Lean, human expert, or independent external audit has been performed.
