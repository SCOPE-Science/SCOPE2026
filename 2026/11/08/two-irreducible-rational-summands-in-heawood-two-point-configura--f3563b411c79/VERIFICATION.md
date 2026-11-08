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

# Reproducible verification

Execute `python3 verification/verify.py` with Python 3.10 or newer. The program uses only the standard library and defines the Fano incidence graph directly; no external graph library, remote service, precomputed certificate, or historical file is required.

The program independently constructs the cubical cellular boundaries and checks their composition is zero; traverses the one-skeleton; enumerates all twenty-eight six-cycles and obtains eight independent lifts; checks second-boundary rank exactly over \(\mathbb F_3\) and \(\mathbb F_{101}\); constructs an explicit fourteen-vector kernel over \(\mathbb F_{101}\); and enumerates the entire order-\(336\) symmetry group via linear maps of \(\mathbb F_2^3\) and point-line polarity. It checks chain naturality for every symmetry, compares direct top-kernel traces with signed cellular Lefschetz traces for all symmetries, computes the conjugacy classes and verifies representation inner products.

The verification is finite and exhaustive for this one graph. The rank argument in the proof, not extrapolation from finite fields, establishes its rational homology dimensions. This does not constitute an independent mathematical audit, rule out unindexed earlier publications, or certify a more general theorem. The exact expected stdout is in `verification/expected_output.txt`.
