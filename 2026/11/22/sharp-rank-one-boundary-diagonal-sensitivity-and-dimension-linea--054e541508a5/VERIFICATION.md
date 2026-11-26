---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

At P-eta Q the isolated eigenvalue 1 has derivative u^T H u and its eigenvector derivative orthogonal to u is QHu/(1+eta), giving PHP+(PHQ+QHP)/(1+eta). At the limit the first diagonal output pairs with the symmetric coefficient matrix P E+E P-P E P for E=e_1 e_1^T. Its sum of absolute entries is exactly the scalar support norm over symmetric H, since the elementwise sign matrix is symmetric. For p=u_1^2 and s=sum_{j>1}|u_j| this gives 2p-p^2+2 sqrt(p)(1-p)s+p s^2; equality in Cauchy–Schwarz gives the profile and the stated sign witness. Its derivative is positive to 1/4, strictly decreasing from there to 1/2 and negative at 1/2 for n>=3. In (1/2,(n+1)/(2n)) the factor (4p-1)sqrt((1-p)/p) is at least one by squaring; thereafter the two terms in the derivative are nonpositive with one strict. This proves the unique maximizer, and n=2 has its limiting max at 1/2. The nonsingular directional quotients are actual two-matrix lower bounds; only afterwards is eta decreased to zero. Frobenius nonexpansivity supplies the upper bound n, not an exact unrestricted coefficient. The critical equation gives p_n=1/2-1/(2 sqrt(n))+O(1/n); in rescaled coordinates z=sqrt(n)(p-1/2) the constant-order term of F_n is 1/2-z-z^2, hence 3/4 at the maximizing z. An independent adjoint-norm and LAPACK central-difference check (/workspace/reproductions/frozen_diagnostics.py 4) passed all 54 determinate differences. The frozen program was inspected but not executed.

## originality

PASS

Best of current knowledge for the exact rank-one-positive flat-negative limiting diagonal profile in dimension n>=3 and its optimizing geometry and expansion. Credit the general PSD projector differential and the previously known n=2 results. The conclusion about unrestricted linear order is a corollary here; it is not an exact unrestricted modulus or a claim of priority for dimension growth across all projection sets.

## value

PASS

Frobenius nonexpansivity alone leaves open whether individual coordinate errors can accumulate with dimension. This boundary class demonstrates the linear growth via actual finite perturbations, determines the precise coefficient for the class and identifies the spread of eigenvector mass causing the amplification. The exact unrestricted constant remains open in the record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
