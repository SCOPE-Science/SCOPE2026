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

Independently reconstructed the proof over any odd finite field. After diagonalizing the action on m/m², project each chosen generator lift onto its required sign with (I±F)/2. The resulting eigen-coordinates have invertible tangent map, hence give an automorphism by the finite filtration. This yields one identity-linear orbit per specified tangent matrix. Counting commuting nonlinear coefficients sign by sign gives centralizer dimension sum(rO_j+sE_j); quotienting the entire tangent kernel yields q^{e_r}. The tangent similarity multiplicity is g_d/(g_rg_s), and the fixed algebra's vector-space basis after conjugation is precisely the even-parity monomials. This computes dimensions with multiplicities, not fixed-algebra isomorphism types from dimension alone. For N=2L+1, multiply monomials of degree 2k−1 by a negative variable to inject into the opposite parity of degree 2k. The even monomial consisting of a positive variable alone to degree 2k is missed by the injection from odd monomials, producing a gap at least sL for 0<r<d; r=0 has exponent zero. Excluding degree one can only widen the gap. For N=2L, write 2e_r=D−(s−r)S with S the signed count in degrees 2 through 2L−1. It is the coefficient of t^{2L−1} in (1−t)^{−(s+1)}(1+t)^{−r}, minus 1+s−r. Factoring out (1−t²)^{−min(r,s+1)} leaves a positive convolution when r<s, an odd-degree zero coefficient when r=s+1, and an all-negative odd-degree convolution when r>s+1. The subtracted constants cannot remove strictness for L≥2: in the positive case k=s+1−r≥2 the leading binomial grows without bound; in the negative case k=r−s−1≥1 the convolution has L odd-degree contributions of magnitude at least k. Thus e_r is uniquely D/2 at r=ceil(d/2): for r=s the multiplier is zero, and for r=s+1 the signed count is zero. The strict gaps diverge and the GL factors are constant in N at fixed d and q, establishing both probability limits. Separate direct monomial enumeration reproduced the four (e,f) pairs (0,20),(22,13),(24,10),(18,7) for d=3,N=4 and (0,35),(43,22),(48,19),(63,22) for d=3,N=5. Read the supplied scripts and recorded outputs as supporting evidence without executing the frozen verifier. Its N=3 composition regressions are not proof of the claimed higher-jet domain.

## originality

PASS

Tame formal linearization is prior and the exact d=2 parity census is prior. The extension to all higher embedding dimensions, including the explicit fixed-dimension spectrum and uniquely balanced-negative even-order type with diverging gaps, is not covered by the inspected comparison results.

## value

PASS

This gives exact population weights and fixed-dimension multiplicities for a natural two-parameter family of finite automorphism groups. The parity switch now compares all higher-dimensional signatures and distinguishes the favored sign in an odd-dimensional nearly balanced split, which is invisible in the earlier two-variable case. The growing gaps explain typical involutions at large truncation order; this is substantive beyond repeating classical linearization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
