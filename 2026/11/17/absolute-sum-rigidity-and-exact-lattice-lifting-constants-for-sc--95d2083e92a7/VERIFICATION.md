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

# Verification of the absolute-sum lifting classification

The proof is self-contained apart from the published \(1^+\)-projectivity of countable \(\ell_1\) (de Pagter–Wickstead, Theorem 11.8). Every asserted inequality is analytical:

1. For normalized absolute \(\nu\), the inequalities \(\max\{s,t\}\le\nu(s,t)\le s+t\) and compactness of \(s+t=1\) establish the finite, attained geometric constant.
2. The norm of the coordinate lattice identity from \(A_\nu\) to \(\ell_1\) is exactly \(K_\nu\), with inverse norm one; the projective lift therefore costs at most \(K_\nu(1+\delta)\).
3. In the tower \(B=c\oplus c_0\), \(I_m\) changes only the first \(m\) coordinates of the first component. The quotient by \(I\) has norm \(\max\{|\lim u|,\|v\|_\infty\}\), by matching upper and lower estimates.
4. For every stage \(m\), the coordinate-\(n\) estimate on positive lifts for \(n>m\) and the limit \(u_n\to s\) give \(\|S\|\ge (s+t)/\nu(s,t)\); optimizing gives \(\|S\|\ge K_\nu\).
5. The explicit positive lattice lift \(S_0(a,x)=((a,a,\ldots),\iota x)\) has \(\|S_0\|=K_\nu\), proving attainment of the same lower bound at every quotient stage.
6. The threshold \(K_\nu=1\) forces \(\nu=\ell_1^2\); the \(q\)-sum and convex-combination formulas follow by Hölder and a one-variable minimum, including both endpoints.

No code execution, finite enumeration, numerical interpolation, or external/infinite certification is required to reproduce the proof. The cited original quotient construction and classical positive projectivity theorem remain external scholarly prerequisites; no independent review has yet been performed.
