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

# Verification
The attached Python 3/SymPy script computes the source's eleven-vertex polygon, signed area, and integrated score quadratic in exact rational/symbolic arithmetic. It checks the identity \(E=5/18+(p-q)^2(3-4p-5q)/9\) and several rational boundary and interior substitutions, including three hexagonal-edge cases. Execute `python check_frege_moment.py` with SymPy installed.

These finite and symbolic computations verify the polynomial identity, not historical novelty or ergodic convergence. Existence of the invariant polygon, its fundamental-domain property and equidistribution for rationally independent vote shares are supplied by Conze–Janson–Öberg's published preprint. The universal lower bound is justified analytically by root-lattice nearest-point inequalities. The scope excludes arbitrary nonergodic boundary orbits and gives no finite-time convergence rate. No independent mathematical audit has been performed.
