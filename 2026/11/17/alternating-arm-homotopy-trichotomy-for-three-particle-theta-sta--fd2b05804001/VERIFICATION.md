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

Run `python3 three_particles.py` in the same directory. The verified output is `verification_output.txt`. No third-party packages are required. The program enumerates configuration cubes, finite-group orbits of all face chains, the exact boundary incidences, and valid elementary collapses. It also checks the residual cycle in the three-arm alternating case and the connected closed surface with Euler characteristic two in the four-arm alternating case. All labels, orbits, and choices of free faces are deterministic. The all-arm deduction is a mathematical consequence of at-most-three-arm support and three-transitivity, rather than an infinite computation.

The calculation proves a classification only for the **defined cubical discretizations** under ordinary geometric group quotients. It does not independently verify an equivariant deformation equivalence to unrestricted continuous configuration spaces. Source novelty checks cannot exclude all unpublished or unindexed equivalences.
