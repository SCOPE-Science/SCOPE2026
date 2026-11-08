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

The proof of the general statement is the basis-and-Cartier case analysis in `RESULT.md`. The accompanying `verify_cartier.py` requires only Python 3's standard library; run `python3 verify_cartier.py` in the extracted package directory. It builds the matrix from polynomial products, checks all \(5^4=625\) tuples over \(\mathbb F_5\), and independently checks \(3125\) translated tuples. The expected result, actually reproduced, is recorded in `verification_output.txt`.

The finite calculation cannot certify the theorem for all algebraically closed fields: that is done by the displayed symbolic fifth-power Cartier matrix and algebraic case split. Historical coverage is assessed separately and does not follow from code execution. No independent audit has been performed.
