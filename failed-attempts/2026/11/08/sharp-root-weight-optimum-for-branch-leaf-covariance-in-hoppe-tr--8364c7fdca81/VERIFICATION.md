---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The independent Hoppe parent choices give P(parent_i=root)=θ/(θ+i-2). For nonroot j, its no-child survival probability telescopes to (θ+j-2)/(θ+n-2). Summing cross covariances of root-child indicators with no-child indicators yields C_n=θ(n-1)(n-2)/(2(θ+n-2)²) for all θ>0 and n>=2. Direct differentiation has sign n-2-θ, giving unique θ=n-2 maximizer and value (n-1)/8 for n>=3; at n=2 covariance 0 for all θ. The critical θ_n/n→α limit is α/[2(1+α)²], while other regimes come from dominance of the same exact formula. Independent full rational parent-history enumeration n<=8 at θ=1/2,1,3,7/2 corroborates.

## originality

FAIL

The full October 18 published Hoppe joint-Gaussian theorem contains exactly the same finite-size cross covariance formula, explicitly remarks that it is uniquely maximized at θ=n-2 for n>2, and supplies the same linearly scaled limit K(α)=α/[2(1+α)²]. This is earlier, broader mathematics (it additionally establishes a nondegenerate bivariate CLT). The present optimizations and asymptotic side regimes are straightforward calculus on the previously displayed same formula; no distinct nontrivial claim survives.

## value

FAIL

The Hoppe root-branch/leaf cross covariance and unique weight optimizer are natural useful invariants, but every main finite and critical-asymptotic conclusion is already an explicit part or elementary consequence of the October 18 bivariate-Gaussian theorem. Rephrasing its auxiliary calculus as a separate optimum is insufficient new mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
