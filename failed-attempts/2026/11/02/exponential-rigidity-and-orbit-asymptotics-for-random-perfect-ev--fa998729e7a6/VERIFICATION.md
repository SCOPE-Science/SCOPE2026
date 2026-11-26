---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

RESULT.md lines 43–90: invertible M makes the squares a basis. Orthogonality of images of distinct natural vectors forces at most one nonzero entry per row of the change matrix, hence monomiality by invertibility. Comparing images of squares gives t_i²M_(σi,σj)=t_jM_ij; this is sufficient as well as necessary. For a permutation of support s, the free parameter count is bounded by the number of ordered-pair orbits, with only (n−s)² fixed pairs; integrality gives the ceiling in the exponent. A diagonal map with s entries different from 1 forces s(n−s) zeros from rows scaled by 1 to other columns and a disjoint sum of m_c² zeros within equal nonunit scalars; their sum is at least sn/(q−2). There is no diagonal term for q=2. Dividing the unrestricted mean by p_(n,q) bounds the conditioned mean, and Markov's inequality controls the probability. Burnside identifies the normalized orbit-count error with that very conditioned mean. For fixed q the diagonal majorant is geometrically summable with exponentially small ratio and the other part is at most 2n²(1−1/q)^n for large n; p_(n,q) is bounded below by the positive infinite product. This includes n=1 with the appropriate empty sums, and does not assert a joint q,n limit.

## originality

FAIL

Demonstrable earlier coverage: the 2026-10-25 Resultary corank paper 340420fa11f4 gives, in (6)–(10), an explicit bound for the sum of nonidentity monomial fixed fractions on all matrices and its O_q(n²(1−1/q)^n) estimate. At corank zero the stabilizer is exactly the algebra automorphism group, so this majorant divided by p_(n,q) proves exponential decay of the same mean, the probability bound and the same leading orbit asymptotic. This is not just a hit for a related dimension or an unevaluated Burnside sum. The frozen diagonal count is a different but weaker asymptotic estimate; the earlier modal-multiplicity bound is explicit and O_q(nq^(−n)). The specific Δ formula is a sufficient error majorant, not a new statistic or sharp correction.

## value

FAIL

The natural question is worthwhile: a mean stabilizer bound is substantially more useful for Burnside than generic rigidity in probability. But the earlier all-corank fixed-fraction result already supplies that bound and class asymptotic. The alternative sufficient Δ bound leaves no separately motivated exact fact or improvement: its permutation component is the same count up to rounding and its diagonal analysis weakens the earlier exponential rate for q>3. No surviving valuable repair is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
