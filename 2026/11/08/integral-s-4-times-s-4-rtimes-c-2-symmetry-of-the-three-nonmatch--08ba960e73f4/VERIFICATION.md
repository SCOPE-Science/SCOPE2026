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
# Reproducible exact checks

Run `python3 verify_bnm_3_44.py` with Python 3. No nonstandard packages or downloaded inputs are needed.

The script constructs the complex from all 96 forbidden three-matchings, checks all 3017 augmented faces and all 13504 Hasse covers, and exhaustively topologically sorts the directed graph of the 1504 matched pairs. There are exactly nine critical 3-simplices. It verifies the chain boundary of nine six-cycle join sphere generators, calculates 564 signed unit-pivot eliminations, and confirms the integral basis determinant -1. It tests the exact nine-by-nine integral action matrices for all 576 row/column permutation pairs, the bipartition exchange, all sixteen three-by-three subboard generator relations, and independently sums signed simplicial Lefschetz contributions for all 1152 group elements.

The supplied `verification_output.txt` was captured by running this actual script. These checks certify a finite chain calculation within the same review, not an independent mathematical audit. They do not establish equivariant homotopy information or extrapolate beyond the four-by-four board.
