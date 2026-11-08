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

# Verification and reproducibility
Run `python3 verify.py` in the same directory; it uses no third-party packages. The exact expected output is stored in `verification_output.txt`.

The checker constructs SQS(8) and SQS(16) from four distinct binary vectors of zero XOR; SQS(10) is constructed using twelve affine lines augmented by infinity and eighteen four-point anisotropic circles over the ternary plane. The program confirms every triple is contained in a unique quadruple, and then performs complete one-move atomic profile checks for every ordered stationary tuple, including repetitions, at widths four and five. The confirmed catalogues are identical across orders eight, ten and sixteen at width four, and identical between orders ten and sixteen at width five. The order-eight catalogue lacks the generic fifth-point profile for four stationary nonblock points.

These calculations are finite checks, not infinite logical equivalence certificates. The theorem over all admissible orders and arbitrary quantifier depth is proved from the unique completion property and the permanent strategies in `RESULT.md`. The checker does not test all designs of a given order; the proof does not assume automorphism transitivity or any field coordinatization.
