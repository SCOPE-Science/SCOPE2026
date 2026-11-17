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

The bundled `f4_quotient_verify.py` uses Python 3 and SymPy for **exact** integer and rational computations, and it requires no external datasets. Run `python3 f4_quotient_verify.py`. The bundled `f4_quotient_verification_output.txt` is the actual output from execution against the packaged script.

It enumerates all \(1152\) signed rational reflection matrices, all \(24\) reflections, all \(105\) noncrossing elements, and all \(103\) proper elements. It constructs every rank-increasing chain, identifies each conjugation orbit and independently reproduces the orbit counts by fixed-chain Burnside sums. It builds the complete signed cellular boundary matrices and checks their exact composition. Their Smith nonzero diagonal entries are eighteen \(1\)'s for \(D_1\) and sixty \(1\)'s for \(D_2\). No non-unit integral invariant factors occur. This yields \(H_1=0\), \(H_2=\mathbb Z^{12}\) and Euler characteristic \(13\).

The fundamental-group and homotopy steps invoke the published shellability result, the standard orbit-space fundamental-group theorem, Hurewicz and the homological Whitehead theorem. The program does **not** independently prove those general theorems; its role is the complete finite calculation at type \(F_4\). Its success indicator `F4_COXETER_QUOTIENT_PASS` is a computational check, not independent publication certification.

No all-rank statement, exhaustive bibliography, or independent audit is certified.
