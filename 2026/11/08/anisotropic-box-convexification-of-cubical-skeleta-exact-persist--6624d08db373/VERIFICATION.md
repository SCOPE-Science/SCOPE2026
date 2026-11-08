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

## Checks reproduced
The standalone `check.py` program uses Python standard-library arithmetic and performs 50,114 exact assertions. Cubical boundary ranks were enumerated over a field for every dimension through six; this is an auxiliary finite check. The closed-form Euler characteristic and death-multiplicity identity were checked through dimension 79. Exact rational membership and missing-volume formulas were compared through dimension seven.

## Proof boundaries
The all-dimensional statement follows from the coordinatewise membership characterization, a strong deformation retraction, standard CW-skeleton connectivity, and finite-product gap volumes. No computation beyond the checked finite range is asserted to be exhaustive for all dimensions. Topological surjectivity uses an explicit coordinate-face section; it is not inferred from the rank sequence alone.

## Reproduction
Use `python check.py` with Python 3.10 or newer. No network, nonstandard packages, external data files, or unprovided helper scripts are required.
