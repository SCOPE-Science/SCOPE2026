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

# Reproducibility and limits

Run `python3 checks/verify.py` from the unpacked scientific folder. It uses Python 3 and no external libraries.

It reconstructs extinction probabilities \((1/12,3/4,3/4,3/19)\), the common exact gradient \((12,12,12,12)\), and the negative Hessian
\[A=\begin{pmatrix}36&9&9&0\\9&12&3&0\\9&3&12&0\\0&0&0&12\end{pmatrix}.\]
The four leading principal minors are positive. Exact Gaussian elimination yields \(A^{-1}{\bf1}=(-1/126,1/14,1/14,1/12)\) and the derivative \((-2,18,18,21)/55\). A separate floating-point finite difference near \(B_\star\) corroborates the first-coordinate derivative. The checker also verifies 1,057 rational two-taxon stationary configurations algebraically.

The general two-/three-taxon theorem, the exact one-sided monotonicity on boundary faces, and the binary-ultrametric perturbation are proved mathematically in `RESULT.md`; no finite numerical sample is used to assert them universally. The independent audit status above is a disclosure, not a claim of external certification. Historical priority against broader resource-allocation theory is not established exhaustively.
