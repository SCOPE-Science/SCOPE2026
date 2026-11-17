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

# Verification of the exact periodic census

The proof of the all-parameter and all-period claim is the torus-kernel/Burnside/itinerary argument in `RESULT.md`. Its only external mathematical premise is the specified conjugacy and Fatou classification of Fletcher and Martin, arXiv:2611.08773v1, Section 6.

Run `python3 verify.py` to repeat finite, exact modular tests. The checker treats a point on the torus as a pair of residues modulo a sufficiently fine integer grid; it tests whether multiplication followed by an optional coordinate reflection returns either the same point or its simultaneous negative, and identifies the two points of each pillow class. For eleven small expansion/reflection examples, these direct classes match the determinant formula. It also checks each symbolic word for five parameter pairs and periods through eight, and checks Möbius inversion divisibility.

Observed standard output:

```text
VERIFY_OK modular_pillow_instances=11 binary_words=2550 primitive_n_up_to=8
EXAMPLE_d2_m3 fixed_J_n_1_to_5 [13, 169, 2197, 28561, 371293]
FINITE_CHECK_ONLY proof_of_all_periods_is_analytical
```

The finite checks do not certify infinitely many words, higher dimensions, or the existence of the global quasiregular map. The exact infinite theorem follows from the proof in `RESULT.md`. Independent audit has not been performed.
