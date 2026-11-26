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

With t=|z|² and the stated area normalization, the orthogonal monomial norms are the claimed beta integrals. For isometry, w=W1 lies in the space. The diagonal identities give equality of finite-measure moments after u=t^N; polynomial density and continuity give Q(t)=N t^(N−1) S_N(t)^alpha where Q sums |w_j|²t^j. For each ell≥1 compare W z^(n+ell) and W z^n: aligned output coefficients are w_j and w_(j+Nell). In the corresponding integral, the absolute sum with factor t^(Nell) is at most t^(Nell/2)Q(t) by Cauchy–Schwarz, so the complex measure used to recover F_ell is finite. Moment uniqueness and analyticity force w_j conjugate(w_(j+Nell))=0 for every j,ell; in particular polynomiality was derived rather than assumed. Logarithmic differentiation gives an identity of rational functions, even though the initial power S_N^alpha was defined on the real interval. At any nontrivial N-th root its residue equals alpha, whereas the residue of Q'/Q there is a nonnegative integer, including zero if Q is nonvanishing there. With alpha=d≥0 the consecutive support of S_N^d has d(N−1)+1 terms (all degrees are sums of d digits in [0,N−1]); the distinct-residue cap N proves d≤1, including N=2. The coefficients at the two surviving exponents have exactly the displayed moduli; no cross-phase constraints remain. Disjoint image degrees give orthogonality, and for alpha=1 the norm sum telescopes as 2N[1/(N(n+1))−1/(N(n+2))]; the alpha=0 norm is N/[N(n+1)]. Polynomial density and bounded point evaluations extend the norm-preserving map and identify it with the pointwise formula on the whole space.

## originality

PASS

The known pullback characterization and unweighted example do not constitute the complete fixed-power classification. The distinct contribution is the exclusion of every other standard exponent for arbitrary holomorphic multipliers and the full alpha=1 phase torus, with uniqueness up to phase also proved at alpha=0.

## value

PASS

The fixed power is a natural model of a noninjective disc covering; the general measure tests do not give an explicit list of weights or multiplier phases. A sharp two-exponent rigidity result, with a phase torus at the weighted endpoint, answers existence and constructs every allowable multiplier, rather than restating an isometry criterion or checking only monomial choices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
