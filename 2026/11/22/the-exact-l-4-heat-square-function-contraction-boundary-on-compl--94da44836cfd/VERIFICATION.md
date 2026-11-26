---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and scope

The proof derives the heat cross coefficient from the exact integral \(\int_0^\infty t\lambda\mu e^{-(\lambda+\mu)t}dt=\lambda\mu/(\lambda+\mu)^2\). The resulting fourth-power deficit proves the full boundary and equality cases for nonzero real or complex Hilbert spaces. The \(\delta=1/4\) real scalar witness can be embedded along a unit vector whenever a part contains at least three vertices. In the zero Hilbert space the inequality is vacuous for all part sizes.

Run `python3 checker.py` for finite reproducibility checks using the standard library. The script uses the derived spectral coefficients; it checks the real witness and deficit expansion with exact fractions up to part sizes twenty and uses floating-point tolerances for sixteen complex samples in the four contractive cases. The script does not replace the heat-integral calculation or the all-size proof.
