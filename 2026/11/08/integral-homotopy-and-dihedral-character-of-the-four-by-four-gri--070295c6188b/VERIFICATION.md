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
# Reproducibility and verification

Run `python3 verify.py` using only the Python 3 standard library. The program is deterministic. It constructs the graph from its edge rule, enumerates all independent quadruples, tests every one of 65,536 candidate face masks by a second method, constructs all 30,319 discrete-Morse pairs, and tests acyclicity of all 469,288 cover relations on all 60,723 nonempty faces. It then computes signed reduced Lefschetz traces from the complete face set and independently counts invariant three-subsets of the nine grid cells for all eight dihedral transformations.

The executable was actually run and its precise output was stored in `verify_output.txt`. Its final line is `ALL_VERIFY_OK`. No external mathematical proof assistant or independently audited certification is claimed.

Finite computations here are exhaustive over this specific sixteen-vertex complex. They do not establish formulas for arbitrarily large grids, equivariant homotopy equivalence or integral representation-isomorphism assertions. The discrete Morse cell dimensions prove the homotopy statement by the standard finite-complex theorem; the character calculation uses the simplicial Lefschetz identity and rational representation character theory.
