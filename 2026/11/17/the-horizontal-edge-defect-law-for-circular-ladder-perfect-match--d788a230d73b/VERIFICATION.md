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

The proof in `RESULT.md` is an unrestricted integer-homotopy argument. `verify_horizontal_defect.py` independently enumerates every perfect matching for widths \(3\le n\le14\); for \(3\le n\le10\) it also explicitly builds every face, checks the exact union and the independence-path intersection for even widths, and reduces the full simplicial chain complex over \(\mathbb F_2\). It compares all Betti ranks to the stated four-part homotopy formula. Eight full chain-complex instances include \(67{,}639\) total faces. The larger widths use exact facet partition only. Output is in `verification_output.txt`. There is no integer Smith-normal-form calculation in this verifier: integrality follows from the proven homotopy decomposition, not from modular computations.

Reproduce with `python verify_horizontal_defect.py` from a directory containing this package's extracted files. No packages beyond the Python standard library are required. Finite verification is not an infinite proof, and a self-review does not constitute an independent audit.
