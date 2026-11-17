---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

Run `python verify_catalan.py` with Python 3 and the standard library. The corrected checker tests finite residue coverage at small prime powers, exact factorial-unit modular arithmetic, prescribed sparse-seed carry valuations, stabilization of high-block units, and a regression example demonstrating that the original fixed-window congruence was false. It prints `VERIFY_OK` on successful bounded tests. The unlimited assertion rests on the three lemmas in the corrected `RESULT.md`, not this finite test. Earlier reviews are historical evidence and do not constitute independent or formal certification.
