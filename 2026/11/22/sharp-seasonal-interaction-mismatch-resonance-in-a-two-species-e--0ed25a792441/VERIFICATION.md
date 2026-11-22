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

# Verification

The mathematical proof is provided in RESULT.md. Its critical identities are: the frozen eigenvalues \(-\kappa\varepsilon\pm i\sqrt{(b+\varepsilon p u)(c+\varepsilon q u)}\); the exact commutator \([B,H]=(pc-bq)\operatorname{diag}(1,-1)\); and the rotating-frame average \(C=(DK-\delta J)/2\) satisfying \(C^2=(D^2-\delta^2)I/4\). Boundedness of the rotating-frame coefficient on one period gives the uniform quadratic remainder; this, not finite sampling, justifies the limiting statement.

Run \(\texttt{python checker.py}\) after installing NumPy, SciPy and SymPy. The program symbolically checks the commutator, frozen determinant and averaged spectral square, integrates fundamental matrices across a sequence of small amplitudes, compares resonant and nonresonant frequencies, and tests detuning and the exact commuting case. Numerical integration error and finite-amplitude corrections limit the computational evidence; equality boundaries and nonlinear populations are not verified.

No independent external scientific audit or validation has been performed.
