---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Run `python3 verify_finite.py` in the source directory. This standalone standard-library script constructs the icosahedral edges exactly in the quadratic integer ring, checks all 4096 labeled spin masks and all twelve single flips per state at each of the seven field representatives, and compares the complete weak, strict, and ground-state inventories. It checks connectivity as well as induced degrees for the low-field family; ten states have a down-spin hexagon and ten an up-spin hexagon, with two triangles on the opposite sign class. It checks external degrees for the middle-field family and antipodality for the high-field family. `RESULT.md` supplies the threshold and energy-comparison arguments that extend the exact table to all nonnegative fields. Neither checker nor proof addresses thermal lifetimes, multi-spin escape or historical priority.
