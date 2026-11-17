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

The proof's exact finite certificate is `pappus_fixed_certificate.json`. Execute `python3 pappus_fixed_core.py verify pappus_fixed_certificate.json` with Python 3 and its standard library, from the directory holding the code and certificate. Its output is included in `pappus_fixed_output.txt`.

The verifier independently rebuilds the 18-vertex 27-edge graph and its full 216-element automorphism group; exhaustively generates the 380 subgroups and 44 conjugacy classes; constructs geometric fixed-point orbit complexes; checks each of the 1,616 matched face pairs, every one of the 13,096 face-poset covers, and every critical-cell signature. It checks the aggregate table equals 380 and 44. `python3 pappus_fixed_core.py generate pappus_fixed_certificate.json` can regenerate the deterministic certificate.

This finite experiment is not being extrapolated to an unbounded family: completeness is justified by full permutation and subgroup-generation algorithms, and the homotopy conclusion uses a mathematical fixed-point-model argument plus the acyclic discrete-Morse theorem. No expert or independent mathematical audit has been performed. Substantive publication-priority uncertainty remains.
