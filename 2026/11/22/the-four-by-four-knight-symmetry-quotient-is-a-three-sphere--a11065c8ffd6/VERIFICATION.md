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

# Finite verification

Run the four commands documented in RESULT.md with a C++17 compiler and Python 3.9 or later. The first program enumerates the 24 attack edges, all 1,364 nonempty faces, the eight geometric actions, and all orbit-chains. After 411,365 elementary free-face removals, its `quotient_reduced.txt` contains the surviving cellular boundary matrices and the surviving barycentric face flags. The identical file is supplied for inspection; regenerate it before the Python checks for an end-to-end test.

The integer check validates all adjacent boundary compositions, then performs integer elementary unit-pivot cancellations. Its terminal result is `KNIGHT4_D4_INTEGRAL_HOMOLOGY_OK` with 21, 81 and 79 cancellations. This proves integral homology without relying on field-only rank calculations. The fundamental-group script checks oriented edge endpoints and triangle face-orbits, then applies 81 legal generator-eliminating Tietze substitutions, ending with `KNIGHT4_D4_PI1_TRIVIAL_OK`. The independent Burnside check gives `KNIGHT4_D4_BURNSIDE_OK` and the flag-orbit f-vector `(217,4801,35910,126666,239340,249840,136080,30240)`.

The finite computations certify precisely the four-by-four geometric quotient. Homotopy equivalence follows only after the mathematical arguments for topological collapses, Hurewicz and Whitehead are applied. No independent mathematical audit or validation has been performed.
