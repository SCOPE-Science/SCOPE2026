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

# Finite and uniform verification

`verify_rook.py` reconstructs the edge-midpoint witness facets and all nonempty faces for the two seed widths, produces a deterministic pivot matching, checks the entire oriented Hasse graph has no directed cycle, and carries out the integral Morse boundary reduction with exact integer coefficients. It requires only the Python standard library. `verification_output.txt` is the recorded run of that exact program. Separate original-complex mod-two boundary elimination returned reduced ranks 4 in degree five for width three and ranks 1, 16 in degrees four, five for width four.

The all-width assertion is not a computational extrapolation: a map sending every extra column to column zero fixes the first four columns and preserves both Čech facet forms (full row plus two columns; full column plus two rows). The induced map splits integral homology. No external/independent verification has been performed; only the documented self-review are represented.
