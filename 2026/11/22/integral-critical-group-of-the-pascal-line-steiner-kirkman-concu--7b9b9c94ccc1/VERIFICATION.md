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

# Reproducible exact checks

Run `python3 verify_pascal.py` and `python3 verify_geometry.py` in a directory containing the two bundled scripts. No third-party Python modules or external data files are required. Both programs were run on their embedded definitions and completed with the following success messages:

- `PASCAL_60_COMBINED_CONCURRENCE_CRITICAL_GROUP_VERIFIED_OK`
- `EXACT_RATIONAL_PASCAL_GEOMETRY_VERIFIED_OK`

The first program independently generates all 60 canonical hexagons, all 20 Steiner triples, all 60 Kirkman triples, and full relabelling orbits of the two published sample triples. The two constructions agree. The integer graph is connected, eight-regular, and has 240 edges. A 59-by-59 reduced Laplacian determinant is computed using fraction-free Bareiss elimination for roots 0, 17 and 59, with identical result \(2^{71}3^{13}5^8 11^{16}\). Local Smith valuations are computed over four prime-power rings, with all 59 factors including units and with independent roots. The elementwise products of local factors reproduce the listed 23 invariant factors.

The second program constructs the six rational conic parameters \(0,1,3,9,27,81\), checks Pascal's three opposite-side intersection points lie on the same line for all 60 hexagons, checks the Steiner and Kirkman triple concurrence relations, and verifies all 80 named points are different. This is a witness for the generic hypothesis, not an assertion that every sextuple is generic.

Finite computations here are exhaustive for an explicitly bounded 60-vertex object, and the proof explains why those operations present its actual integral divisor-class quotient. They do not establish broader statements about arbitrary families or special characteristics. No independent mathematical validation has been performed.
