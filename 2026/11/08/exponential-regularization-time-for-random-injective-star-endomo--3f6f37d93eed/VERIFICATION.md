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

The full pinned RESULT.md uses the exact published regularity criterion for IEnd(S_n) (Dimitrova–Fernandes–Koppitz, arXiv:2401.11741v1, Theorem 2.3, inspected on PDF page 6). The center-excluding-domain type has exact deficiency weights w(m,j)=C(m,j)(m+1)!/(j+1)! and decreasing ratio (m-j)/[(j+1)(j+2)], proving J/sqrt(m)->1 with exponentially bounded relative tails. The uniform predecessor-chain product tends to exp(-x) at x sqrt(m). A Lah-number count gives a negligible O(m^-1/2) acyclic exception, so for typical maps T=L+1. Exact finite survival subtracts the rank-one-power exceptional forests, counted by m![z^(m-t)]exp(sum_{a=1}^t z^a). Independently enumerated actual injective partial graph endomorphisms and direct powers at n=2..6 (sizes 7,26,119,730,5627), including the published regularity witness test at n<=4, and verified all survival coefficients. Neither finite enumeration nor an unproved tail extrapolation supplies the asymptotic proof.

## originality

PASS

The exact first-regular-power law for the star monoid combines a hub-specific obstruction with chain distribution and a bounded-path exceptional correction. The same 2024 star-monoid paper proves elementwise regularity and cardinalities, but not hitting-time distribution. The 2005 general partial-injection paper proves orbit/chain counts and studies products of independently sampled maps, not powers of one uniformly sampled star endomorphism. The 2013 bounded-list EGF kernel is prior and explicitly credited. No equivalence or dominating published hitting-time statement surfaced in the inspected primary comparisons and Resultary searches; residual unindexed priority risk remains.

## value

PASS

First entrance into the regular part of a nonregular finite semigroup under repeated powering is a natural dynamical invariant beyond static regularity. The result gives the complete finite distribution and a nonconcentrated infinite-family Exp(1) limit at the genuine sqrt(n) scale, as well as an exceptional finite forest correction, not a mere renamed nilpotency statistic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
