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

# Finite matrix checks and limitations

Run `python3 check_product_fibers.py` with a standard Python interpreter. It computes the Gaussian-binomial/Möbius formula using integer arithmetic, separately enumerates all pairs of square-zero matrices satisfying all four zero-product identities for \(b=0,1,2,3\) over \(\mathbb F_2\) and \(b=2\) over \(\mathbb F_3\), and directly tests the four original factorization identities over \(\mathbb F_2\) for the nonzero rank-one target in dimension four. The direct factor test enumerates every candidate satisfying the target's necessary image/kernel restrictions and accepts a pair only if the original equations hold. Its entire output is in `verification_output.txt`. Additionally, `check_five_binary.py` enumerates all parameter choices for the rank-one nonzero product fiber in dimension five over the binary field and checks the original equations for each of the predicted 672 pairs. That separate output is in `direct_five_binary_output.txt`.

These finite tests are not a proof in arbitrary dimension. The general result follows from the independent block-bijection and subspace Möbius arguments written in `RESULT.md`. No independent audit or external certification has taken place.
