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
# Reproducibility of the two-adic necklace fiber theorem

Run `python3 verify.py` with standard Python 3. The verifier reconstructs Möbius values and Euler totients by elementary integer arithmetic, evaluates the necklace polynomial by modular exponentiation, and enumerates complete residue histograms for eleven odd squarefree indices through \(2^{11}\). It checks both normalized odd branches and the even branch as finite permutations at seven precision levels, as well as nine distinct odd nonsquarefree lengths at modulus eight.

Observed output: `VERIFY_OK squarefree_lengths=11 residue_entries=45034 local_branch_bijections=231 nonsquarefree_lengths=9 finite_level_fibers=PASS`.

The proof is unrestricted in the squarefree odd length and modulus exponent. Finite checks cannot prove these universal quantifiers; the theorem depends on the coefficient-divisibility estimate and isometry arguments in `RESULT.md`. No external or independent audit was performed.
