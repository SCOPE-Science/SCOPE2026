---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Rebuilt both graphs on all signed states −3200,…,3200 directly from the rational map formulas, with exact nearest-even rounding. Moving the even integer shift ±512 outside the outer rounding preserves ties, including the negative-state ties. The inner formulas agree and the outputs, including those at −640, 0 and 640, stay in the domain. Floyd cycle detection followed by backward breadth-first traversal from each cycle found exactly the stated period/basin pairs: A (34,238), (40,6163); B (8,68), (20,2830), (24,253), (24,442), (28,1404), (28,1404). The basin sizes exhaust the state count for each map and the maximum depths are 107 and 80. In integer coordinates the unrounded outer values differ by |i|/320≥2, so even after rounding every outer state changes successor and no inner state does; this gives exactly 5122 changes independently of the census. This does not test or identify an FPGA arithmetic pipeline.

## originality

PASS

The inspected prior work supplies the real map and the seven-fractional-bit motivation, not the census for the two exact arithmetic semantics. The conclusion is limited to the checked sources, including a full-text access limitation for the originating article.

## value

PASS

Seven fractional bits is a source-motivated resolution, and the controlled comparison changes only the coefficient encoding. The whole-grid census provides a concrete check on claims about robustness of long-run behavior that trajectory examples cannot supply: the cycles, basin weights and longest transient change, not just individual iterates. It is an exact comparison of two numerical models, not empirical hardware validation or a claim at other resolutions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
