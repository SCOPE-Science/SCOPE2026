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

The standalone `verify.py` program independently evolves the local map by cyclic bit rotations. It exhaustively checks \(n\in\{1,2,4,8\}\), every stride modulo \(n\), and all binary pairs: 525,348 configuration checks over 15 size–stride combinations. The program verifies each first-return period and compares the complete labelled period histogram with the claimed exact formulas. A passing run reports `PASS: 15 dyadic size/stride cases; 525348 exhaustive states; space-time equality and cycle census`.

The mathematical proof, not exhaustive small-case enumeration, establishes arbitrary dyadic lengths, arbitrary strides and fields of order \(2^f\). Independent mathematical validation has not been performed.
