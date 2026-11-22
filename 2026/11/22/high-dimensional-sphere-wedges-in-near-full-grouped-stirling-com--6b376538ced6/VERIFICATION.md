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

The proof uses two exact structural reductions (cubical cells to a thin-diagonal complement, and star products to a join with diagonal facets removed), then an integral relative homology computation and homotopy Whitehead argument. The required assumption \(r\ge4\) is used to preserve the two-skeleton after deleting top facets.

Reproduce finite checks with `python3 verify_grouped.py`. The code uses only Python standard-library modules. It verifies exact integer \(\partial^2=0\), mod-two boundary ranks, and compares distinct cubical and simplicial models in 15 cases, of which five are in the theorem range. Mod-two ranks alone do not rule out torsion; the integral wedge proof does. No external mathematical validation has been performed.
