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

# Reproduction of the cyclic Rule 18 formula

Run `python3 direct_check.py` and `python3 transfer_check.py` from the directory containing these files. Python's standard library suffices. Expected messages are `DIRECT_OK` and `TRANSFER_OK`. The direct program checks every input and every output at lengths \(1\) through \(18\), including the unique zero-output maximizer. The transfer program constructs the two matrices from the local neighborhood rule independently, checks every output at lengths \(1\) through \(12\), and tests predetermined and pseudorandom examples at six larger lengths through \(180\).

The all-length justification is mathematical: long zero-run endpoints force a parity-paired output, each alternating pairing produces a product of Fibonacci interval counts, and there are exactly two such pairings. The zero-output trace of the golden-mean adjacency matrix is Lucas, with the all-zero source added. A golden-ratio estimate makes the maximum strict. Finite checks alone do not establish these universal statements.

This is a self-reviewed computation and proof package, not an independently audited result. No external certification has been performed.
