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

# Verification procedure and limits

Run `python3 verify.py` with Python 3; no third-party libraries are required. The program builds the two-particle adjacency and the proposed full dark projector as integer matrices, verifies the exact polynomial matrix identities, reconstructs the bright subspace independently by Krylov iteration from every collision basis vector over two prime fields, and checks all normalized symmetric-pair survival values for sizes \(3\le n\le10\).

Expected output begins with `VERIFY_OK n dimension dark_rank bright_rank` and has rows `(3,9,3,6)`, `(4,16,8,8)`, `(5,25,10,15)`, `(6,36,17,19)`, `(7,49,21,28)`, `(8,64,32,32)`, `(9,81,36,45)`, `(10,100,49,51)`.

Integer calculations were completed successfully. They check finite instances but do not alone establish the formula for every \(n\); the uniform all-\(n\) argument is the Fourier-sector proof in `RESULT.md`. No independent external scientific audit has been performed.
