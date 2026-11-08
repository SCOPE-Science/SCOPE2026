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

The executable `verify_icosahedral_symmetry.py` independently constructs the 12-vertex, 30-edge icosahedral graph, enumerates all matching faces, reconstructs all 120 automorphisms by triangle propagation, computes reduced homology rational ranks using exact mod-two lower bounds and chain-complex upper bounds, computes signed Lefschetz characters, and verifies the full rational irreducible decomposition. It checks the signed boundary-equivariance identity on all nonempty simplicial incidences for every automorphism.

Execution: `python3 verify_icosahedral_symmetry.py` under Python 3.9 or later, without dependencies beyond the Python standard library. Success marker: `ICOSAHEDRAL_MATCHING_SYMMETRY_PASS`. Complete actual output is `verification_output.txt`.

The mod-two rank calculations are used only as certified lower bounds for rational ranks; integer chain-complex inequalities force equality in every degree. No assertion about torsion follows from those ranks. The character proof uses only rational homology, a complete group enumeration and exact signed chain traces. Full integral module structure and an equivariant homotopy classification are not established.
