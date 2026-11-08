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

# Reproduction of finite proof certificates

Invoke `python3 crown_d5_verify.py` with SymPy available. The program has no internet dependencies and reconstructs the board directly rather than trusting a precomputed face or boundary list.

It enumerates all \(780\) faces including the empty face, then uses the displayed fixed pivot order to build the toggle matching. Deleting the single empty-face pair gives \(382\) ordinary face pairs and \(15\) critical cells: one zero-cell, one two-cell and thirteen three-cells. It verifies all \(2{,}500\) covers and acyclicity by a \(779\)-face topological sort. Complete exact rational ranks of the five augmented boundary operators are \((1,19,111,208,44)\). These ranks force zero integer degrees in the Morse differential, hence the wedge-of-spheres homotopy type.

The eight-triangle integral sphere used to identify the degree-two symmetry is built directly from three incompatible pairs of squares. Its boundary is zero; exact Gaussian elimination modulo three against all \(265\) three-simplices verifies that the class remains nonzero. Images under a label transposition and board transposition are compared modulo boundaries; opposite character signs are also explicitly excluded.

For all \(120\) simultaneous label permutations and both choices of board transpose, it counts *oriented setwise-fixed faces* and verifies the derived character formula against the reduced Hopf trace. This is exhaustive because these \(240\) transformations are the full graph-automorphism group.

The embedded `verification_output.txt` is the recorded actual stdout of the code. Nothing here replaces an independent scientific review. The complete integral third-degree representation, extensions beyond five labels and equivariant homotopy type remain unproved.
