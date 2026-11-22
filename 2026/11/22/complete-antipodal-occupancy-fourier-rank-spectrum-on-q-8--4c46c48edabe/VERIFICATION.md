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

# Verification of the quaternion support-rank classification

The proof covers every nonempty exact support of the eight-element group, not merely the stored examples. The package has two executable checks with different implementations:

1. `python verify_quaternion_construction.py` rederives the fourteen occupancy classes, regenerates and compares all 64 canonical witnesses, verifies the scalar Fourier values and two-dimensional quaternion determinant, and confirms all designated nonzero coefficients really are nonzero.
2. `python verify_quaternion_regular.py` uses a separate quaternion multiplication table to form eight-by-eight convolution matrices and determines their exact symbolic ranks. It tests group associativity, all 24 coordinate permutations preserving scalar Fourier zero counts, and every attainable rank on each of the 255 fixed supports, making 1,148 direct rank comparisons.

Both scripts read `quaternion_witnesses.json` from their own directory and require SymPy as recorded in `requirements.txt`. Actual outputs are preserved in `verification_output.txt`, and the scripts were executed in that configuration. No approximate tolerance is used for rank decisions. The mathematical argument in `RESULT.md`, not the finite verification alone, rules out unlisted ranks via the complete four-character/two-dimensional decomposition and exact-support constraints.

Limits: this does not independently certify mathematical priority, does not test other groups, and does not substitute for an independent human or external mathematical audit.
