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

# Reproducible checks

Place `verify.py` beside `boundary.json`, install dependency from `requirements.txt`, and execute `python verify.py`. The verifier regenerates the exact \(P_4\square C_4\) graph and all simplices, checks every face-poset cover and the directed acyclicity of its 10,723 disjoint pairings, computes all signed gradient-path entries, and compares the matrix to `boundary.json`.

The 12-by-37 matrix is independently tested for two integer left-kernel vectors, a determinant-minus-one 10-by-10 submatrix, and Smith factors equal to ten ones. Since the reduced CW four-skeleton is 3-connected, this certifies its attaching maps integrally, not just over a field. The original full simplicial chain complex is additionally reduced over \(\mathbb F_2\) without using the Morse matching.

The exact expected JSON output is `verification_output.txt`; success status is `P4_C4_INTEGRAL_WEDGE_PASS`. The program re-computes, rather than trusts, the stored matrix. There is no external data download. Tested with Python 3.11 and SymPy 1.14.0.

# Limits

The computation covers exactly the simple graph \(P_4\square C_4\) and no other width or boundary convention. Mod-two checks alone would not establish integral torsion-freeness. The integral conclusion uses the primitive unit-minor argument plus the exact Morse boundary. No independent audit of the proof has been performed.
