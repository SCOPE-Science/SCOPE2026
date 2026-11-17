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

# Verification of the finite homotopy certificate

## Replay

`python3 verify_chessboard.py`

Requires only Python 3 standard-library modules. The exact expected standard output is the companion file `verification_output.txt`; the program is deterministic and contains explicit assertions for each crucial count and check.

## Exact checks

Two separately structured exhaustive recursions — column-first and row-first — enumerate the identical set of 6,310 faces including the empty face. The nonempty-dimensional vector is \((24,225,1020,2250,2160,630)\). A fixed vertex permutation and increasing-mask scan generate 3,105 disjoint matched face pairs and leave one critical vertex and 98 critical four-cells. Every matched pair is checked to be a legitimate codimension-one incidence and no simplex is reused.

A distinct pass constructs every one of the 27,090 nonempty face-cover incidences and orients them according to the matched-Hasse criterion. The topological sort visits all 6,309 faces; this certifies the nonexistence of directed cycles, the critical hypothesis of Forman's theorem. The matching-pair serialization has SHA-256 `1ac49f5ec41f4e2deaf3a255080727b3d6e624413a392a622fcafbe58fed7352`.

The full mod-two reduced boundary calculation has ranks \((1,23,202,818,1432,630,0)\), where the first is the augmentation rank. It yields reduced mod-two Betti rank 98 in degree four and zero elsewhere. Integral homotopy follows instead from the certified cell-dimensional Morse model (one zero-cell plus only four-cells), so no finite-field torsion inference is made.

## Scope and limits

This is an exhaustive certificate for the finite specified 24-square board, not an infinite-parameter enumeration or an independent external certification. The executable algorithm, its precise vertex order, the complete Hasse acyclicity test and its output are included so the integer and homotopy reasoning can be replayed. A second implementation could supply additional independent assurance. Independent audit has not been performed.
