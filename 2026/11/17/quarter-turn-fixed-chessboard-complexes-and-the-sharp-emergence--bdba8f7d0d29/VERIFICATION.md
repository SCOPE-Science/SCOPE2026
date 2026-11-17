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

Run `python verify.py` using Python 3.10+ and SymPy 1.14. The program constructs each orbit of quarter-turns on squares, independently tests nonattackingness, identifies two alternatives per pair of antipodal label pairs, and exhaustively checks the correspondence between two-orbit compatibility and disjoint matching edges for every board order from one through fourteen. It exhaustively constructs the face vectors of the corresponding twofold matching inflations and their odd-board cones.

For matching complexes on two through seven graph vertices, it constructs signed integer augmented simplicial boundary matrices and computes Smith normal forms over the integers. All nonzero Smith invariant factors on matching complexes through six are units; the seven-vertex matching complex has exactly one factor three, in the boundary from two-dimensional simplices, with boundary ranks \((1,20,85)\). Its one-dimensional homology is consequently \(\mathbb Z/3\mathbb Z\), and its two-dimensional free rank is twenty. These verify the critical finite published input directly.

The program outputs exact JSON statistics and terminates with `QUARTER_TURN_CHESSBOARD_EXACT_CHECK_PASS`; the expected byte-for-byte output is embedded as `verification_output.txt`. No randomized numerical methods or finite-field proxies are used in place of integer Smith reductions. The finite checks alone cannot establish the uniform PL equivalence for infinitely many board sizes; the explicit orbit-barycenter proof does so. The general integral splitting is due to the cited published inflation theorem.

Independent audit: not performed.
