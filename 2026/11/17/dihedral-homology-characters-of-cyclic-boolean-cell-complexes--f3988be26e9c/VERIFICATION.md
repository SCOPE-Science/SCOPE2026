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

Exact finite verification uses `verify_boolean_cycles.py`, run from the same directory with Python 3 and no external dependencies. This program constructs cells from injective words, uses directed induced edges to identify commutation classes, calculates cellular incidence maps over integers, and checks the dihedral action including orientation signs. It validates the chain-complex condition in orders 3–8, chain-equivariance for two rotations and two reflections in orders 3–6, both-modulus top boundary ranks in orders 3–7, and all 66 rotation/reflection traces in orders 3–8.

The independent computations reproduce the dihedral character formulas, not just the ranks. The numbers of nonempty cells in orders 3–8 are 15, 44, 120, 319, 840, 2204; the corresponding top cell counts are 6, 14, 30, 62, 126, 254. The top rational ranks inferred from earlier theory are 2, 5, 9, 16, 27, 45, and direct modular boundary checks corroborate the first five. Full-dihedral invariant ranks are 0, 1, 0, 2, 2, 3.

The source-level proof supplies the unbounded parameter argument; computations cannot establish the theorem for all cycle lengths. Rank agreement over two finite fields is corroboration rather than an integral Smith certificate; no integral-lattice classification is claimed. The proof depends on the published wedge-of-spheres theorem and the ordinary cellular Lefschetz trace formula.
