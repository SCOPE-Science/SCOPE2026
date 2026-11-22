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

# Verification and limits

Run `python3 checker.py` in Python 3 using the standard library only; successful completion prints `ALL_CHECKS_OK`. The program constructs all canonical minimizers for the oriented case under a fixed certified root and ordered relation-state partners (\(2^3\cdot3^6=5832\) encodings), asserts each has the correct 23 nonzero unordered pairs and all required two-point extension profiles, and asserts that the canonical codes are distinct. It independently evaluates the literal rank recursion on examples with \(q=2,3\), checks all 23 one-arc deletions of one 13-point example, and checks all \(32768\) labelled ordinary graphs on six vertices.

The proof, not the finite program, validates all \(q\ge2\), all converse involutions fixing zero, and all finite host sizes. Both construction and enumeration explicitly treat the 5832 count as certificate-preserving isomorphism classes; unpointed classes may have several certificates. No external independent audit or formal proof certification is claimed.
