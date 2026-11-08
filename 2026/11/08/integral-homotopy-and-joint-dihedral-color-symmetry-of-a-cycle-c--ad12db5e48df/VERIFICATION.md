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

# Verification
The standalone file `verify_c8_k3.py` is the entire standard-library Python 3.10+ checker. From the directory containing the files, run `python3 verify_c8_k3.py`; compare the stdout with `verification_output.txt` (exactly). It enumerates the entire face set and oriented face-poset Hasse digraph, validates complete acyclicity of the specified Morse pairs, recomputes all six-by-eight integral attaching coefficients and a unit five-by-five minor, and computes 24-vertex original-boundary mod-two ranks independently.

The second symmetry calculation checks all 96 elements of the natural \(D_8\times S_3\) action against graph adjacency, then computes signed reduced Lefschetz numbers from permissible vertex orbits using exact independence-polynomial recursion. The one-dimensional fourth-homology character candidates are exhausted, and the only viable fifth-homology character is identified via its norm and the degree-three representation dimensions.

These are finite computations, not an infinite-family theorem. The integral conclusion uses integer cell cancellation and the standard discrete Morse equivalence, not solely a finite-field rank calculation. The verification does not constitute independent formal certification or a global publication-priority proof.
