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

# Verification protocol

Run `python3 CHECK.py` from the directory containing this document. Expected final line begins `VERIFY_OK`; no downloads or third-party modules are required. This checks all binary inputs through length sixteen, then restricts them to cyclic no-adjacent-one sources. It compares two independently coded synchronous Rule-90 updates and the complete nonempty output-fiber histograms, and checks iterated stabilization and second-step collapse. Reproduction of this finite check was performed on the standalone packaged source.

The all-length/all-time statement is proved in RESULT.md by the exact polynomial kernel and cyclic parity-class argument. Enumeration cannot establish the infinite claim or historical novelty. All reported review judgments are same-model; no independent mathematical audit or external certificate has been performed.
