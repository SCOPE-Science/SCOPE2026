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

# Reproducibility and limits

Run `python3 verify.py` in the same directory; only the Python standard library is required. Recorded output is in `verification_output.txt`.

The script independently enumerates all twelve grid edges and all matchings, then verifies exact face counts \((12,44,56,18)\), a complete acyclic 62-pair matching and the five remaining two-cells. It checks the full oriented Hasse graph, not just critical-cell counts. It enumerates signed fixed simplices of all eight square symmetries, constructs the quotient by acting on chains in the first barycentric subdivision and computes integer boundary-square identities and the mod-two boundary ranks \((19,68,54)\). These are complete exhaustive finite checks of the specified simplicial objects.

The group orbit-space fundamental-group theorem, the characteristic-odd transfer argument, the exclusion of integral torsion using universal coefficients, and the final Whitehead argument are mathematical deductions reviewed separately. A finite computation is not claimed to establish any theorem for larger grids. Independent audit has not been performed.
