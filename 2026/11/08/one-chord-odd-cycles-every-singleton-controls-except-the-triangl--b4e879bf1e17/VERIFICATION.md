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

# Verification and reproducibility

Run `python3 verify.py` (Python standard library only) to construct each unweighted odd chorded cycle and test every possible dedicated one-vertex input with modular Krylov ranks. The embedded program was extracted and run from this package before delivery and reported:

`PASS: exact modular Krylov ranks; 320 single-vertex configurations`

The tests cover every odd order \(5,7,\ldots,35\). A nonzero determinant modulo the prime modulus proves a nonzero integer determinant, thus full rank over \(\mathbb Q\) and \(\mathbb R\). The midpoint's lower modular rank does **not** in itself establish a corresponding upper rank in characteristic zero; that conclusion follows analytically from reflection, and the exact rank formula follows by the visible even modes. The mathematical proof supplies the infinite-family result; the finite tests serve as independent corroboration for a bounded sample.

The primary publicly dated source is arXiv:1403.4868v1, submitted 19 March 2014. The proof does not depend on any downloaded paper or external executable. No independent mathematical audit has been performed.
