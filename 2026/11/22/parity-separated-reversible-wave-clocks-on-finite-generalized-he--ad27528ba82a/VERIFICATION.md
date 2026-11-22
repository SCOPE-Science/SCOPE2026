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

# Verification of the exact hexagon wave clock

The proof in `RESULT.md` is an all-geometries theorem based on the distance-algebra recurrence. The included `check_distance_algebra.py` recomputes the modular distance powers and verifies the degree-seven or degree-six annihilator with a nonzero top-distance coefficient, for both parities of the order parameter.

The independently implemented bit-matrix `check_wave.py` constructs the adjacency of the actual twelve-cycle (a thin boundary generalized hexagon, not part of the theorem's \(q\ge2\) scope). It also constructs faithful cyclic algebra modules corresponding to each derived minimal polynomial. For each of these three finite test matrices it computes the two-level wave's exact order by matrix exponentiation and independently compares every fixed-space nullity up to that order with the derived primary-Jordan formula. The runs yielded \(12\), \(48\), and \(12\), respectively, with \(72\) exact nullity comparisons total. The cyclic modules are algebraic models, not alleged geometric realizations.

Reproduction from this package requires only Python 3. Run `python3 check_distance_algebra.py` and `python3 check_wave.py`. These tests have been executed successfully on the included scripts. The code does not enumerate unbounded graph families or replace the exact geodesic argument. Independent external validation has not been performed.
