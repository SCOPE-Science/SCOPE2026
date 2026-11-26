---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The labeled graph is the connected cubic bipartite graph obtained by adjoining the six even-vertex offset-five edges to the cycle. Independently reconstructed all 195 nonempty independent faces. An unmatched Hasse arrow points from a higher face to a lower face and strictly increases the removal-block index; matched arrows stay within one two-face block, so no directed cycle exists. The 95 pairs leave one critical vertex and four critical two-faces: the resulting CW complex has no one-cells and every two-cell attaches to the vertex, giving the integral wedge, not just field Betti numbers. To check the group independently, connectivity forces an automorphism to preserve or swap the two vertex sides; all 6! images on one side for each choice determine the other side by the distinct neighbor triples. This yields 48 permutations and center {1,z}. For each invariant independent face, selecting an entire vertex cycle of length l contributes (−1)^l(−1)^(l−1)=−1 to the augmented alternating sum before the overall sign. Summing over unions of vertex cycles, including the empty face, reproduces all eight order/trace bins, trace −2 at z, sum of traces 48, and sum of squared traces 96. Rational averaging splits off one trivial line; the complement has complex character norm one and hence is absolutely irreducible. Its trace −3 at the order-two half-turn forces all three eigenvalues to be −1. Independent exact replay: `python3 /workspace/reproductions/franklin.py`, covering all faces and group elements. The frozen script was read, not executed. No equivariant wedge or integral representation splitting was needed.

## originality

FAIL

The distinct indexed Finding 8aefb2ed39c1 explicitly gives the same nonequivariant four-sphere wedge, the same rational full-group splitting, and the same central sign for exactly the labeled Franklin independence complex; it supplies a stronger integral basis and integral action. The coverage is substantive and complete. That index path is later-labelled, so this is not a claim that its authors were first or that it was an antecedent at the time of the frozen work. The current comparison finds no distinct invariant or representation assertion beyond the stronger indexed result. The matching-complex record and Barmak theorem are not reasons to fail.

## value

FAIL

The ordinary independence topology and the full (not just dihedral) symmetry-fixed homology are worthwhile exact invariants of this standard graph. However, the exact pair of invariants is already made available by the matched statement, which gives strictly finer integral information. This separate finite certificate does not leave a new exact invariant or a substantive narrower claim to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
