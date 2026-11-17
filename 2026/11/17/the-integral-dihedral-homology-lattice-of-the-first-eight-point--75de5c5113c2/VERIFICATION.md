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

The script `verify_sg24.py` uses only the Python standard library and terminates on any failed exact arithmetic assertion. Run `python3 verify_sg24.py` alongside this document. The recorded run is provided in `verification_output.txt`.

It independently enumerates the full simplicial complex (244 nonempty faces), derives all sixteen relative triangle cells and twenty chord edges, verifies a unit-determinant rank-thirteen boundary minor, checks the exact primitive kernel basis, and recomputes the signed octagon rotation/reflection action on the integral kernel. A four-cycle of integral classes is checked to generate the entire kernel with exactly one primitive sum-zero relation; the cyclic coinvariants are verified by gcds of integer minors. Separate full-face signed Lefschetz calculations test all sixteen group elements without relying on the reduced chain presentation.

The output marker is `STABLE_KNESER_2_4_INTEGRAL_DIHEDRAL_LATTICE_PASS`. The known nonequivariant concentration outside degree two is supplied by the cited Braun theorem, rather than extrapolated from finite experiments. No independent third-party review was performed.
