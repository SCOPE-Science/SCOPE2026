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

Run `python3 artifacts/verify.py` using only the Python standard library. The included `artifacts/verification_output.txt` records the exact replay on a finalized verifier copy, ending with `VERIFY_OK`.

The program explicitly enumerates all matchings and all \(2^n n!\) graph automorphisms at \(n=2,3,4\). It computes signed simplicial Lefschetz traces by orbit counting on invariant matchings (including the augmented empty face) and checks the predicted full-group trace. Independently, it constructs every simplicial boundary matrix over \(\mathbb F_2\) and checks the degree and dimension of reduced homology. Twenty more character tests are run at \(n=5\), including nontrivial blade reversals and blade permutations. The source is self-contained.

The finite tests are not a proof of the all-integer theorem or of integral torsion-freeness. Those follow from the explicit decomposition into spoke cones and the integral equivariant long exact sequence. No external reviewer or independent certification is claimed.
