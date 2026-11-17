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
# Verification notes

The proof checks the local Dirichlet operator for \(D_\theta^2+1\) directly; it does not infer a continuous theorem from finite computation. The Green kernel has zero boundary values and its distributional second derivative has the prescribed unit jump. Computing its supremum and integrated absolute value yields the exact two local constants. The full-circle curvature variation of \(q(x)=|\langle v,x\rangle|\) is exactly four, with one atom of mass two in each selected antipodal cell. Substituting these atoms proves equality in both claimed inequalities.

Standalone \`verify.py\` uses only the standard Python library. Invocation: \`python3 verify.py\`. It passed 372 deterministic checks of the kernel integral formula, maximal inequalities, nonuniform-fan geometry, and saturation examples. It samples finitely many meshes and quadrature nodes; those tests are diagnostics and do not replace the universal analytical argument. Independent audit was not performed.
