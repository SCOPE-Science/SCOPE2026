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
# Computational verification and proof boundaries

Run `python3 verify_distance.py` and `python3 verify_locality.py` with standard Python 3 in the same directory. The bundled outputs were produced by running those unmodified scripts.

The first program performs breadth-first search in the binary adjacent-swap graph and checks the exact transport distance for **all 66,196 ordered equal-weight pairs** at lengths 1 through 9. The second program enumerates all nonempty sets of binary blocks for each block length 1 through 4 and checks that any set whose second concatenation power is two-error-correcting remains correcting at powers 3, 4, 5. The safe-set counts are respectively 2, 4, 17, and 91, and all 342 corresponding later-power checks passed. It also explicitly verifies the sharp block-length-one witness.

The proof of all lengths is mathematical, using prefix imbalances, deletion of repeated levels and a cross-splice reduction; no finite range is asserted as exhaustive for arbitrary block lengths. Separate scientific reports contain detailed assumptions, derivations, comparisons and residual risks. The findings have not been independently audited.
