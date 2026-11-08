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
# Reproduction and limits

Run `python3 verify.py` with a standard Python 3 interpreter. This is a standalone dependency-free enumeration of the element commutator rowspaces in the strictly upper-triangular \(4\times4\) algebra over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7\). Finite fields are explicitly implemented, including \(\mathbb F_4\) via the irreducible polynomial \(t^2+t+1\). Matrix products are reconstructed from basis units; the program does not call the symbolic formula to calculate its empirical rowspaces. It compares each individual fiber size, its multiplicity, each codimension count, and the global count with the theorem. The program prints `VERIFY_OK_N4_CENTRALIZERS` if all assertions pass.

The finite runs independently verify the specified small-field cases only. They are not a certificate for all prime powers; the four-case rowspace proof in `RESULT.md` supplies that inference. Equal-subspace testing is by reduced row-echelon form over the actual coefficient field. Self-review of the algebraic argument was completed; no independent audit has been performed.
