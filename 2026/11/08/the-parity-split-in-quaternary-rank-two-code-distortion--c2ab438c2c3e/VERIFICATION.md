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

# Verification of the quaternary rank-two classification

Run `python verify.py` with Python 3 and no third-party dependencies. The script uses exact integer arithmetic for \(\mathbb F_4\) and exact rational arithmetic for distortion. It enumerates the 60 projective permutations from all invertible two-by-two matrices over the four-element field and checks equality with the alternating permutations of five objects. It also verifies the Frobenius transposition and the two nonisometric length-ten examples.

The script checks all nonzero codeword weights of each explicit generator, verifies the common weight enumerator, and computes the exact distortion \(100/81\). It exhaustively tests repeated-profile orbit predictions for shorter lengths and tests the sharp distortion formula for 150 distinct-weight profiles at lengths 10 through 21. An observed successful replay prints `CHECK_OK`. These finite computations are checks of the argument, not exhaustive proof for arbitrary length. The all-length classification follows from the projective parity action and the inversion inequality in `RESULT.md`.

No outside certification or independent audit is asserted. A separate literature priority assessment remains open, particularly for unpublished or unindexed discussions of rank-two code equivalence.
