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

# Verification of the finite certificate

Run `python3 checker.py` from the directory containing the embedded file. It uses only the Python 3 standard library.

It checks exact field arithmetic modulo three, full rank of the generator and Gram matrix, twenty-five distinct normalized nonzero projective columns, the complete Hamming weight enumerator over 243 messages, every unique reduced-echelon subspace for ranks one to five (2663 subcodes total), all 2300 column triples and all 12650 quadruples. The assertions cover every coefficient of the displayed support census, both low-weight dual counts, and all local-repair exceptions. The expected output consists of four lines beginning `PASS:`. This is exhaustive for the specified finite code, and it does not certify any global classification of all codes of these parameters.

The mathematical reason the subspace enumeration is complete is uniqueness of reduced row-echelon bases. Dual weight-three and weight-four supports are complete because every nonzero ternary coefficient can be normalized to one and the other coefficients are in \(\{1,2\}\). An independent review has not been performed.
