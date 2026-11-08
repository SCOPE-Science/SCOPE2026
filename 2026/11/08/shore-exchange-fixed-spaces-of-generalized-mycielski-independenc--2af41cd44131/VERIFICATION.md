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

# Mathematical reproducibility

Run `python3 verify.py` in the same directory as `RESULT.md`. The program uses only Python 3 standard-library modules and directly creates the generalized Mycielskian edges and involution, without trusting precomputed face lists. It verifies orbit admissibility, incompatibility graphs, equal-neighborhood domination, 4,434 invariant faces across 21 graph-orbit examples, mod-two reduced Betti numbers of 12 fixed-point complexes by boundary-rank computation, and 29 signed simplicial Lefschetz checks including direct full-graph invariant-face enumeration in eight cases. The recorded execution is `verify_output.txt` and terminates in `ALL_VERIFY_OK graph_orbit_cases= 21 invariant_faces= 4434 GF2_cases= 12 signed_Lefschetz_cases= 29`.

The code checks finite cases only, so it does not prove the theorem for all sizes or give an infinite certifier. The unrestricted proof is supplied mathematically in RESULT.md, with Carnero Bravo Proposition 10 as an openly acknowledged independent prior source for the nonequivariant ranks. The quotient homology calculation uses exact rational transfer/coinvariants, not an integral torsion computation. Independent mathematical validation has not been carried out.
