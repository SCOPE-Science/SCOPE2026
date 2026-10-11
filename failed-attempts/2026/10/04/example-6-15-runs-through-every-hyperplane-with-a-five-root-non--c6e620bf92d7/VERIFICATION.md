---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The finite-field algebra is correct. From \(\phi_\rho^\dagger(y)=\rho y+y^{16}\), a nonzero adjoint-kernel vector satisfies \(\rho=y^{15}\). The kernel of the fifteenth-power map on \(\mathbb F_{64}^\times\) has size \(\gcd(15,63)=3\), exactly \(\mathbb F_4^\times\), so projective normal points biject with the \(21\) singular parameters and the adjoint orthogonality identity yields \(C_\rho=y^\perp\). Hull nontriviality is equivalent to \(\operatorname{Tr}_{64/4}(y)=0\). Eliminating \(y\) from \(y+y^4+y^{16}=0\) and \(\rho=y^{15}\) gives \(\rho^5+\rho^4+1=0\). A fresh independent realization of \(\mathbb F_{64}\) confirmed 21 projective lines/singular parameters and exactly five roots.

## originality

FAIL

The primary source already supplies all load-bearing ingredients in exactly this family: the adjoint identity, \((\operatorname{im}\phi)^\perp=\ker\phi^\dagger\), the singular equation \(\rho^{21}=1\), the one-dimensional singular adjoint kernels, a general trace-isotropy criterion on the singular locus, and an exhaustive Example 6.15 count of 21 singular fibers with five non-LCD exceptions. The projective hyperplane bijection is then the direct observation that the kernel equation gives \(\rho=y^{15}\) modulo the three-element scalar kernel; the degree-five equation follows by elementary elimination of that same trace condition. Under the required implication-level standard, this is a structural repackaging of the source's complete fixed-field classification rather than a surviving original theorem.

## value

FAIL

The projective interpretation is elegant exposition, but the source already gives a complete fixed-field hull classification and exact five-point exceptional set. Passing from its one-dimensional adjoint kernels to all projective hyperplanes and rewriting the listed trace-isotropic points as one degree-five polynomial is a short finite-field reformulation rather than a new motivated invariant or unresolved boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
