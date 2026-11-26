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

# Reproducing the individual attraction-basin census

Run `python3 check_individual_basins.py basin_catalog.tsv` with NumPy installed. The unchanged catalog contains the least labelled phase, least period and exact basin size for each attractor. The checker constructs every successor from the graph definition, labels attractors, and uses all successive inverse-image layers to assign a unique basin to each of the \(2^{20}\) initial masks. It tests the complete period–basin-size spectrum and compares all 4,387 individual rows. It prints `Exact catalog agreement: 4387 rows` followed by the 26 spectrum rows. The computation involves no sampling or numerical tolerances.
