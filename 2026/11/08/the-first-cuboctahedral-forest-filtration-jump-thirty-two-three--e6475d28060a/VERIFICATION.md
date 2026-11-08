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

# Reproducible finite verification

Run `python3 verify.py` with a standard Python 3.9+ interpreter. All inputs, including the 12 cube edges and the two pivot permutations for each filtration level, are constructed or explicitly given by the script; no graph library or network data are required.

Membership is checked independently by selected-neighbor degrees and connected-component traversals on all 4096 masks. The augmented face-poset acyclicity tests cover all 264 and 1524 Hasse edges at levels zero and one; ordinary (nonempty-face) acyclicity is checked separately after unpairing the empty face. Both matchings at level zero yield four critical two-faces; both at level one yield 32 critical three-faces. After unpairing, each ordinary Morse matching has exactly one additional critical vertex. Thus the integral homotopy results are supplied by the discrete-Morse CW theorem.

Direct mod-two simplicial boundary elimination from the original unreduced chains confirms four degree-two and 32 degree-three homology generators respectively. Direct relative-chain elimination gives 36 degree-three generators for the quotient. These field calculations independently cross-check the enumerations and cofiber count; they are not used to infer torsion-freeness or homotopy equivalence. The cofiber homotopy type follows from the null-homotopic inclusion between established wedges of spheres.

Recorded successful console output, including all critical masks and counts, is in `verification_output.txt`. Expected terminal marker: `CUBOCTAHEDRAL_FOREST_FILTRATION_JUMP_VERIFIED`.

Independent external audit has not been performed. Possible unpublished or unindexed equivalent results are not ruled out by the computational verification.
