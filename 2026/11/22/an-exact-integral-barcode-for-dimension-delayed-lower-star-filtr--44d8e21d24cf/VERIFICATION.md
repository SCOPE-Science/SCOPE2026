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

# Verification and reproducibility

The complete proof is the filtration-preserving triangular integral change of basis written in `RESULT.md`. Its leading simplex coefficients are all one and the inverse introduces no later cells; direct two-term differential blocks prove the integral interval decomposition and the transition maps. A separate implementation performs ordinary column-reduction persistence over prime fields directly from simplicial boundaries, without using the proposed cone chain basis.

Run `python3 verify_cone.py` from the extracted package directory (standard Python library only). The tested program enumerated 315 weighted cones with 2 to 8 vertices, random finite simplicial bases (also full simplices), tied vertex weights, and strictly increasing nonuniform dimension delays. For each of three distinct coefficient primes, 2, 3 and 5, the independently reduced complete barcode matched the formula: **945 successful comparisons**. The fixed random seed is 1729.

These checks do not test infinitely many complexes or constitute an independent mathematical audit. They cannot show the statement for arbitrary dimensions, establish novelty or replace the proof. The apex-minimum condition is essential, as demonstrated by the one-edge counterexample in `RESULT.md`.
