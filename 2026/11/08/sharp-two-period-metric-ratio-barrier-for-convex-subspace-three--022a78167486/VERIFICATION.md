---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The weighted coordinate projections onto orthogonal lines give the invariant state map T_s=[[rho^2,-rho/s],[s rho(1-rho^2),rho^2]] with det rho^2. The two-period product has trace 2p^2-p(1-p)(q+q^{-1}) and determinant p^2, p=rho^2. The real quadratic Jury inequalities reduce to strict q+q^{-1}<(1+3p^2)/(p(1-p)); the other Schur inequality stays positive. The identity threshold=6+(3p-1)^2/[p(1-p)] yields exact uniform bound max(q,q^{-1})<3+2sqrt2, with -1 eigenmode at equality and real eigenvalue below -1 beyond. rho=0 nilpotent special case covered. Source SymPy verifier inspected; independent rational product at rho=3/5,q=6 gave det(I+P)=-4/125, an actual unstable witness.

## originality

PASS

General safeguarded variable-metric three-operator splitting and nonstationary Douglas–Rachford theorems require adjacent-metric controls or summable step increments that fail for a nonconstant two-period metric. Closely related published Floquet PDHG and reflected-splitting frontier theorems involve distinct state maps/step conventions; matching topical wording does not imply this explicit 3-operator line-indicator threshold. Best-of-knowledge PASS with full-text gap for 2026 source.

## value

PASS

A minimal two-dimensional convex subspace feasibility example identifies precisely when bounded positive definite periodic switching destabilizes stationary convergent operators, and gives a sharp worst-correlation threshold plus exact eigenvector obstruction. It clarifies why the adjacent-metric safeguard is structurally relevant rather than a routine method tuning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
