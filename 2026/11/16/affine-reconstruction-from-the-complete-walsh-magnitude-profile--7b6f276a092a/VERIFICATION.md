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

# Exact verification

Run `python3 CHECK.py` using Python 3.10 or later. The script uses only the Python standard library and prints `CHECK_OK relation_spaces_1_2_4_8=1_42_175_30 all_7_subsets_F2_4=11440 affine_orbits=6` on successful completion.

It exhaustively constructs all affine-relation subspaces of length seven with even weights and minimum nonzero weight four. The counts of subspaces of respective sizes one, two, four, eight and sixteen are 1, 42, 175, 30 and 0. It checks complete dual weight distributions and six coordinate-permutation orbits, and independently evaluates every unnormalized Walsh coefficient of all 11,440 seven-element subsets of the four-dimensional Boolean group.

For the four-cube, the exact class counts are: 240 for affine dimension three (seven relations of weight four), 6,720 for affine dimension four with three weight-four relations, and 4,480 for affine dimension four with relation weights four, four, six. All counts sum to the complete binomial total 11,440. The script separately checks the MacWilliams coefficient identity by integer binomial sums on canonical relation spaces. No floating point, randomness, inaccessible datasets or unprovided code are needed.

**Proof limit:** these finite checks cannot establish the theorem for every larger ambient dimension. The mathematical proof supplies the dimension reduction, six-type classification, complete realization and dual weight-enumerator calculation. The check does not establish historical novelty or independent mathematical validation.
