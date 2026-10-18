---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For g=x²−1 over F2, Frobenius gives g^N(x)≡x^(2^N) for even N, x^(2^N)+1 for odd N. Thus F=(g^N)^2+c≡x^(2^(N+1)) for even N and x^(2^(N+1))+1 for odd N. Even N constant F(0)=c≡2 mod4; odd N shifted constant F(1)=c≡2 mod4. Hence the unshifted/shifted monic polynomial is 2-Eisenstein for every N>=0. With f=x²+c and g=x²−1, published Theorem 1.8 has rad(2)|2 and g^i(0)=0,-1 alternately; its squarefree list for N>=1 is exactly {c,c+1}. Its second prime test 4∤((-c)²+c)=c(c+1) automatically holds. Independent full exact integer polynomial expansion for c=2,6,10,14,22 and N=0..4 checked all parity coefficients and constant valuations. Tests support but do not prove the infinite statement; the symbolic induction and cited conditional theorem do.

## originality

FAIL

DECISIVE STRONGER PRIOR COVERAGE: this is a single-polynomial iterate in disguise. With f(x)=1−x² and g(x)=x²−1, for every m>=1 one has f^m(x)=−g^m(x). Therefore F_(c,N)(x)=−(f^(N+1)(x)−(c+1)). König–Smith–Wolske arXiv:2412.10358v3, Theorem 4.2, already characterizes all dynamically monogenic iterates of f=1−x^d. Substituting d=2 and a=c+1 gives c,c+1 squarefree and (−c) not congruent to 1 mod4; the latter is automatic for c≡2 mod4. Thus the principal infinite monogeneity classification is an immediate special case of the published 2025 theorem, which also supplies dynamical irreducibility when those conditions hold. The extra irreducibility for nonsquarefree parameters comes from an elementary parity Eisenstein check but does not rescue the overall final classification from substantive prior coverage.

## value

FAIL

The mathematically substantive infinite monogeneity iff is a direct specialization of the stronger 2025 dynamically monogenic theorem after an elementary conjugacy. What remains beyond that published implication is a standard parity/translation 2-Eisenstein calculation for a particular residue class; it is not an independently motivated structural classification or nonroutine research advance. A true proof and reproducible examples do not establish independent value for a covered core result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
