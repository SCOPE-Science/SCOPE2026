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

The bundled `checker.py` builds the commutator operator on every upper-triangular matrix unit and composes it directly. It exhausts all strictly upper-triangular matrices in the specified finite odd fields, compares pointwise with the cut criterion and then with the closed counting formula. It also tests the first characteristic-two counterexample.

The ordinary proof, not the finite enumeration, establishes the infinite family. The algorithm does not assess nonreduced scheme structures or the completeness of historical literature searches.

Reproduction: `python3 checker.py` from the folder containing the extracted files. Expected terminal marker: `UPPER_TRIANGULAR_SANDWICH_DIRECT_ADJOINT_PASS`.
