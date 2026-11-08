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

# Reproduction

Execute `python3 verify.py` in a directory containing the enclosed program. It uses only Python 3 standard-library modules and constructs the bipartite Kneser graph \(H(5,2)\) from five labels.

The program checks each of the following exhaustively: 6,211 nonempty faces; the full 3,103-pair augmented matching; the absence of directed cycles among all 30,380 Hasse covers; five zero signed integral Morse coefficients; 240 natural \(S_5\times C_2\) automorphisms and an independent all-automorphism backtrack; fourteen conjugacy-class values; equality of orbit-polynomial and signed fixed-face Lefschetz sums for all 240 elements; and nonnegative-character multiplicity forcing the degree-four sign line.

The output should agree byte-for-byte with `verification_output.txt` for an appropriate Python 3 implementation, including the final marker `DESARGUES_240_SYMMETRIES_EXACT_CHARACTER_PASS`. `character_table.csv` gives the fourteen distinct group classes and both degree-wise characters in a readable table.

## Boundaries of verification

This exact enumeration proves only the stated finite graph computation, not a family-level theorem or a classification of the integral degree-five representation lattice. The algorithm is a checkable finite proof of the Morse and character identities, not a replacement for independent mathematical review or a global publication-priority determination.
