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

# Reproducibility and scientific limits

`torus_character_verify.py` is standalone Python 3 standard-library code. Run it from a writable folder and verify that `torus_character_data.json` and stdout match the bundled references. It enumerates 25,531 independent subsets (including the empty set), constructs 200 distinct toroidal symmetry permutations, computes the entire fixed-orbit reduced Lefschetz trace histogram, and independently evaluates oriented simplicial traces for four representative group elements. It checks both character-averaging equations. No randomness, floating point operations, or external data are used. The code's exhaustive checks establish this finite 200-element calculation only; identification of reduced alternating trace with degree-four homology uses the cited prior ordinary homotopy theorem.

Expected standard output:

```
TORUS_5X5_200_SYMMETRY_TRACES_PASS
augmented_faces=25531 distinct_group_elements=200
histogram={"-1": 116, "1": 75, "4": 8, "9": 1}
full_invariants=0 translation_invariants=1
independent_signed_simplex_crosschecks=4
```

The integer trace formula does not provide the integral automorphism module or a general grid-size theorem. No independent external audit is claimed.
