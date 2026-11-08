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
The exact analytical certificate is the three displayed Jury inequalities in RESULT.md. Their validity uses only \(0<r<1\), \(0<\delta<1\), and \(-1\leq w\leq1\), which are fully quantified and proved in the result. At \(\delta=1\), the same inequalities give a strict gap for \(w<1\). The opposite stability implication uses the uniform mode's determinant \(\delta>1\).

`verify.py` uses only the Python standard library. Run `python verify.py`; the script checks rational polynomial identities for a finite grid, boundary-mode inequalities, Fourier eigenvalues of true periodic Moore tori, and two-root numerical bracketing for \(C_r>2\). The enumerated computations are independent corroboration, not the proof of universality. No independent scientific audit has been performed.
