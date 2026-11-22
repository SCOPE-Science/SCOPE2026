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

# Reproducibility and verification scope

Run `python3 verify.py` with the Python standard library; its expected full output is `verify_output.txt`. The run must end with `ONE_NODAL_QUARTIC_FROBENIUS_CHAMBER_CLASSIFICATION_OK`.

The program reconstructs the integral Picard intersection form for the five-point blowup, all thirteen negative curves and the root reflections. It generates the complete \(1920\)-element Weyl group without relying on external classification packages, filters the \(48\) maps fixing the unique \((-2)\)-root, and matches them with \(S_4\times C_2\) labels. Every one of the \(8192\) possible negative-curve subsets is checked both by exact determinant signs on nested principal blocks and by an independent Schur-complement condition; exactly \(285\) survive. Invariant masks yield ten exact size-polynomial profiles and the class-size weighted Burnside orbit count of \(30\); direct orbit enumeration independently agrees.

Geometric completeness of the negative-curve list and the descent correspondence require the mathematical proof in `RESULT.md`; mere execution of the finite checker cannot establish those facts. There is no assertion that all ten abstract Frobenius types occur for every finite field, nor any independent validation or certification beyond these reproducible calculations.
