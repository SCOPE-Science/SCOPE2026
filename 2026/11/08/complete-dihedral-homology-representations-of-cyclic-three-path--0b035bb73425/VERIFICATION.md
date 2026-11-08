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

# Reproducibility and limitations

From a directory containing `verify.py`, run `python3 verify.py` using Python 3 with no third-party dependencies. The program directly constructs cyclic triple-avoiding faces and the vertex-permutation action. It compares all 330 dihedral character values in lengths 4 through 18 with independently enumerated signed fixed-face Lefschetz sums. It then computes the entire reduced finite-field homology of lengths 4 through 14 over both prime fields of orders 101 and 103 (22 separate instances).

The delivered `verification_output.txt` records successful execution. The transfer-matrix and orbit-geometry proof in `RESULT.md`, together with Taylan's nonequivariant theorem, establishes the infinite result. The program does not prove that no larger-length exceptions exist; only the all-parameter algebra does so. The source-based originality assessment is not an independent publication-priority certificate.
