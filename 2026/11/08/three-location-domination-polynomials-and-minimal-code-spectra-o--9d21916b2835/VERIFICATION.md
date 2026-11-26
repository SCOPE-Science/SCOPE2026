---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Run `python3 verify.py` with the standard library. Direct checks from the closed-neighborhood definitions cover 5,376 labelled vertex subsets of each graph for orders \(n=4,5,6\). They check every coefficient of the prism self-location polynomial, its inclusion-minimal spectrum and the shared prism/crown self-location polynomial, as well as equality of the two solid-location families. Success ends with `VERIFY_OK subsets_per_graph=5376`. These finite tests corroborate but do not replace the all-order proof.
