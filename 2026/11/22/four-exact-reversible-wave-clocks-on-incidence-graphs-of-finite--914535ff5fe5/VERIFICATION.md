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

# Reproducible checks

`python3 verify_partial_geometry.py` requires Python 3 with only the standard library. It directly constructs and verifies thirteen finite partial geometries, the binary antiflag identity, predicted sharp wave orders, adjacency-Jordan multiplicities and 312 fixed-space comparisons for time indices 1 through 24. Its completed stdout is in `verification_output.txt`. All matrix arithmetic uses exact GF(2) row bit operations.

`python3 verify_small_orbits.py` independently iterates every state on two small incidence graphs using actual neighbor parity and stored past state, without matrix powers. It verifies 4,096 and 65,536 labelled states and their exact primitive-period histograms. Its stdout is in `verification_orbits.txt`.

The proof of the universal period law and full rank-based formulas is in `RESULT.md`. These tests verify concrete realizations and do **not** constitute an exhaustive search over arbitrary partial geometries. Characteristic-two extension fields are handled algebraically by scalar extension. Independent audit has not been performed.
