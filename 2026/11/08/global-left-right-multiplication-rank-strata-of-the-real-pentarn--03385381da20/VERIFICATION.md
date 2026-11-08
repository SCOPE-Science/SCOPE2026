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

# Verification record

The executable `check_pentarnion.py` is an exact-arithmetic checker using Python and SymPy. Invoke it in the same directory with `python check_pentarnion.py`.

The checker constructs the multiplication tensor from the defining products, independently obtains the full left/right matrices, and checks \(\det L_p=N(p)F(p)\) and \(\det R_p=N(p)F(\bar p)\) as polynomial identities. It also verifies the expanded cubic identity, the singularity-driving gradient identity, rank-three left and right exceptional witnesses, their opposite-sided invertible ranks, a rank-four example, and both determinants and rank categories on 405 integer-coordinate test vectors.

Recorded successful output is in `verification_output.txt`:

`VERIFY_OK polynomial_factorizations=2 gradient_identity=1 exact_integer_vectors=405 exceptional_left_rank=3 exceptional_right_rank=3`

A finite integer grid is not a proof for all real elements. The global rank stratification follows from the displayed exact polynomial identity, positivity of \(N\), the real sum-of-squares singularity argument and the adjugate rank bound. The checker needs SymPy, not any internet service or external data source. Independent expert validation has not occurred.
