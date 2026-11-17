---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

The monomial coefficient matrix is b_{nk}=(n+1)/(n+k+1)*sqrt(w_n(beta)/w_k(alpha)). In compact range -1<alpha<0,beta>alpha+2, the head k<2^L can be approximated by L geometric terms on each of L dyadic input columns; ratio |c_j-k|/(n+c_j+1) ≤1/3, with one extra exact k=0 column, yielding rank≤1+L². Gamma-ratio weighted column estimates summed across k≥2^L give squared Hilbert–Schmidt tail ≤C(L+1)2^-τL for τ=min(beta-alpha-2,-alpha)>0. Thus norm error ≤C(3^-L+sqrt(L+1)2^-τL/2) and s_N≤C exp(-c sqrt N), hence S_p all p>0. The proof uses infinite tail estimates; inspected source exact rational finite checker only corroborates kernel identities and limited samples. Converse uses earlier Li–Zhou compactness theorem.

## originality

FAIL

The published October 18 full differential Hilbert result proves the same S_p all p>0 classification and a STRONGER root-exponential rank-(1+J²) estimate C(3^-J+2^{-δJ/2}), δ=beta-alpha-2, using the same Cauchy kernel with dyadic ROW shells. Present column-shell version has τ≤δ and extra sqrt(L+1); it establishes no new spectral implication beyond the earlier published theorem. Merely dualizing the approximate block direction is an alternative implementation without a motivated new mathematical conclusion.

## value

FAIL

A constructive quasi-Schatten classification and low-rank approximation is mathematically useful, but this exact operator and complete parameter/exponent range were already proved with a stronger approximation bound. The present mechanically analogous dyadic column variant and weaker error estimate do not justify an independent new finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
