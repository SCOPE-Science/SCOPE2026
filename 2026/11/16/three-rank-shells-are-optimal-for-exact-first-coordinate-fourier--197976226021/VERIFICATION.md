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
The Python 3 file `check_rank_shell.py` uses SymPy symbolic rational simplification to verify normalization, the first two moment conditions, their variance, and the forced inadmissible second shell location. It also exhaustively enumerates every matrix in six small prime-field ensembles: \((q,n)=(2,2),(2,3),(2,4),(3,2),(3,3),(5,2)\). For each, matrix rank is computed by exact modular Gaussian elimination; character-exponent residues of rank-one and rank-two frequency representatives are verified to be exactly uniform under the proposed rank-mixture probabilities.

Execution command: `python check_rank_shell.py` from the extracted artifact directory, with SymPy installed. The observed exact-arithmetic labels were `SYMBOLIC_MOMENTS_AND_TWO_SHELL_OBSTRUCTION_PASS` and `EXHAUSTIVE_RANK_SHELL_CHARACTER_ORTHOGONALITY_PASS` in each of six configurations. These finite exhaustions do not prove the all-\(n\), all-prime-power theorem; the group-invariance and kernel-counting proof in `RESULT.md` supplies that scope. Character values in nonprime finite fields are covered by the analytical proof, not by the enumerator.

External independent validation has not been performed.
