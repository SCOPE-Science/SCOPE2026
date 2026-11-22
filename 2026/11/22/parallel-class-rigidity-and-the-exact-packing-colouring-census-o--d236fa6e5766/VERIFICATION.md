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

# Reproducibility notes

The mathematical proof is in `RESULT.md`. The two standalone, standard-library Python files `verify_packing.py` and `verify_geometry.py` are independent finite corroborations; neither proves the general statement by enumeration.

Run `python3 verify_packing.py`: direct incidence and shortest-path enumeration for the affine plane of order three, testing all 8,876 independent choices of the colour-one class and legal colour-two/three subsets. The output reports maximum combined occupancy 15, exactly 12 maximizing first-three-class triples, palette 9 and 8,640 optimum named colourings.

Run `python3 verify_geometry.py`: independent finite-field constructions at orders three and four, including nontrivial four-element-field multiplication. It checks affine incidence axioms, diameter, colour validity, exhaustive point-subset equality cases, and residual point-deleted regular connectivity. Outputs report palette sizes 9 and 15 respectively.

These computations were rerun successfully against the actual packaged artifact contents. The all-order proof rests on finite affine-plane axioms and elementary matching/counting arguments; the computation is not a certificate for arbitrary order. No independent scholarly audit has been performed.
