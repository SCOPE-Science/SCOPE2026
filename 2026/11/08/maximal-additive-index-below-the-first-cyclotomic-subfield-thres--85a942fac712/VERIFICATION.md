---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The additive-increment period set T={u:g(x+u)-g(x)=g(u) for all x} is an F_p-vector subspace; the additive index is q/|T| by linear extension from T. Cyclotomic homogeneity g(hx)=h^r g(x) for h in H=(F_q*)^ell makes T invariant under H. For ell|q-1 and ell<=p, ell<=p-1, so |H|>p^(n-1) if n>=2; a nonzero T must contain Hu and hence all F_q. If T=F_q, g is linearized with degree<=p^(n-1), and agreement with a monomial on >p^(n-1) elements of H forces exactly one Frobenius term; n=1 is immediate. For odd p, f(x)=x+c x^p, norm(c)!=1, is an invertible F_p-linear non-Frobenius map with ell exactly p+1. Independent F9 presentation enumeration ell=1,2 examined all 320 presentations and found only period dimensions 0 and 2, and tested the sharpness construction; finite check corroborates the all-prime argument.

## originality

PASS

The maximal additive index dichotomy AddInd=q for non-Frobenius low-index maps is substantially stronger than Bienvenu–Winterhof 2026 §6.2 conclusion AddInd>=p; the sharp first failure at ell=p+1 is exhibited, and no equivalent full dichotomy was identified in actual relevant-source comparisons. Best-of-knowledge with Reis–Wang 2022 access risk.

## value

PASS

Sharp low-multiplicative-index rigidity for additive structure is an exact uniform algebraic boundary of a natural finite-field invariant. Excluding every intermediate additive index and exhibiting a sharp p+1 permutation counterexample clarifies how cyclotomic homogeneity constrains additive periods; it is substantially more informative than the known lower bound p.

The dated certificate retains the supplied scientific assessment, sources and limitations.
