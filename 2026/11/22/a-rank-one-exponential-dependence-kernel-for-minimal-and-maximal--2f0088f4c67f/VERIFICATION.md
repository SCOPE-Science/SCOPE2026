---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The source/sink indicators are original-edge absence events, since any nontrivial directed path into a vertex has a last original incoming edge, and the outgoing statement is dual. The two marginal products follow from disjoint incoming and disjoint outgoing edge families. A minimal indicator at i and maximal indicator at j share one edge if j<i and none otherwise; their positive covariance is p q^(n+i−j−2) in the shared case. The resulting weighted geometric sum gives (4), including n=2. For the joint generating function, differentiating the two-copy edge-pair interpolation gives the product of finite differences multiplied by pq. For edge j→i the difference factors are (1−z)(1−w) with the selected indicators removed, and the two remaining absence events fix disjoint edge-pair coordinates with probability q^(n+i−j−3). For a central pair, the first L minimal and last L maximal indicators use disjoint coordinates, none fixed by conditioning, so their conditional joint PGF is exactly F_L(z)F_L(w). Each other minimal/maximal indicator has at most one incident coordinate made non-marginal by conditioning; after a union bound its additional contribution on the closed unit bidisk is O_p(q^(L−1)). The noncentral pairs up to gap L have at most 2L positions per gap, and the larger gaps have a geometric tail O_p(n q^(n−2+L)). With L of order log n and q^L≤n^−3, this bounds the integrated error uniformly by O_p((1+log n)q^(n−1)). The full weight sum multiplied by pq is n q^(n−1)+O_p(q^(n−1)); replacing F_L by F adds only a geometric error. This gives the normalization in (1), vanishing correction on either marginal axis, and Cauchy extraction gives (2) and the strictly positive leading (1,1) cell in (3).

## originality

PASS

The one-variable law is known, and the exact finite covariance (4) already appears in the proof of an earlier public Resultary record, even though that record's main asymptotic regime is sparse. Do not count (4) as novel. The substantive frozen result is (1), the full first dense joint-to-product correction with rank-one factorization, with (2)–(3) as consequences. The compared results do not give that correction. This is a qualified assessment against inspected evidence, not global priority certification.

## value

PASS

The uniform bivariate result quantifies the dependence left after two natural boundary counts have become asymptotically independent. It determines the leading signed joint law, including the simultaneous unique-minimum/maximum excess, far beyond one covariance or two marginal distributions. Its scale and factorization follow from explicit edge sharing and localization, not from an arbitrary parameter slice or numerical estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
