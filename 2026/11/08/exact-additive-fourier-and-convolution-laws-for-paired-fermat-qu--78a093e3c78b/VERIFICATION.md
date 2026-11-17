---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For odd p and h0!=h1 mod p, the valid inputs n=a+pt for a not forbidden yield q_p(a+h_j+pt)=q_p(a+h_j)-t(a+h_j)^{-1}. Thus their paired vector multiplicity is the sum of R=p-2 distinct-direction affine-line indicators in F_p². Each nonzero Fourier frequency is orthogonal to at most one line: uv(u+v)=0 yields zero, otherwise the exact single p times root-of-unity phase with unique a. For m>=2, base-residue words constant in a give line-supported p^{m-1} contributions; all nonconstant words have rank-two span and contribute p^{m-2} uniformly. Parseval gives E_m=p^{2m-2}(R^{2m}+R(p-1)). For p>=5 the min r_2 is R(R-1)>0 and the image proper, making exact basis order two; p=3 has only one line. Independently checked exact frequencies, m=1..3 convolutions for p=3,5,7,11 and varied signed shifts.

## originality

PASS

Best-of-knowledge exact all-frequency joint Fourier spectrum, all-order convolution law and sharp two-sum representation floor for complete eligible p² period. The basic Fermat-quotient lift identity is prior and gets no credit. Chen–Ostafe–Winterhof (2010) study exactly these delayed quotient vectors and the same lift identity, but their full manuscript proves exponential-sum discrepancy bounds and lattice tests, not the explicit three-line zero spectrum, convolution powers or exact basis order for an eligible full period. The elementary affine-line mechanism increases priority risk: an earlier line-incidence corollary may give the same conclusions.

## value

PASS

This is an exact, all-prime classification of a natural paired arithmetic statistic, describing every Fourier frequency (including phase), every m-fold additive representation count, sharp min two-sum multiplicity, energy and marginal uniformity. These are different invariants from known scalar quotient pseudorandomness bounds, and the full rank-two line geometry is naturally motivated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
