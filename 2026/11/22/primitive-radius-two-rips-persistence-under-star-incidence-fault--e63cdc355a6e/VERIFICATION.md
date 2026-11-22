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

# Verification of the incidence-star Rips filtration

The argument in RESULT.md derives all-order contractibility of the two shore complexes, the exact union-intersection decomposition, the natural Mayer–Vietoris connecting isomorphism and the primitive graph cycle-lattice inclusions. The attached standalone verifier checks the finite combinatorial inputs directly rather than assuming the stated sphere formula.

Run `python3 verify.py` using the Python standard library. It generates the projective planes of prime orders two and three, checks unique joins/intersections, deletes the first zero through q incidences of one point, recomputes every shortest-path distance, enumerates all Rips maximal cliques and full faces, compares every face to an independent two-piece construction, executes free-face collapses and calculates exact GF(2) ranks of the resulting two-dimensional boundaries. The recorded output in `verify_output.txt` was reproduced from the embedded script.

A binary boundary computation cannot detect odd torsion or prove homotopy in arbitrary order; the homotopy-pushout and primitive cycle-lattice proof supplies those integral and all-order conclusions. No independent mathematical validation has been performed.
