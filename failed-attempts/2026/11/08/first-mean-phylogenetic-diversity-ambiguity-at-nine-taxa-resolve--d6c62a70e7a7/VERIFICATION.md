---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

PASS: A rooted edge is retained in PD exactly when at least one descendant leaf survives, so mean(q)=2n-2-sum_e q^{clade_size}; equality over all probabilities is equivalent to equality of full clade-size multisets. The complete recurrence for nonplane full binary shapes gives 1,1,2,3,6,11,23,46 shapes at n=2..9 and 45 distinct n9 fingerprints, one two-member class. Nested indicators have Cov(I_e,I_f)=q^{|C(e)|}-q^{|C(e)|+|C(f)|}, giving variance difference 2q^7(1-q) for the exhibited pair. Independent all-46-shape fingerprint and ancestral-pair computations reproduce this exact difference. Grafting a common outer tree preserves mean collisions. All claims stay within unit-edge Bernoulli homogeneous independent survival; finite tree-size census is exhaustive only through n=9.

## originality

FAIL

FAIL: OEIS A382440 (original entry March 25, 2025) already tabulates rooted full-binary shapes modulo the multiset of rooted subtree sizes: the 8-internal-node value is 45 versus 46 total shapes, with all smaller values matching, which is exactly the submitted first mean-PD collision after translating nonroot clade leaf counts to subtree internal counts plus one. Moreover the full published October 18, 2026 theorem 'Sixteen leaves are the sharp threshold for two-moment phylogenetic-rarefaction ambiguity' establishes that complete mean+variance profiles identify all rooted unit-edge full-binary shapes through 15 leaves. Bernoulli(p) raw moments are Bernstein mixtures over uniform fixed-size samples; linear independence of the Bernstein basis makes complete Bernoulli mean and second-moment profiles *equivalent* to full fixed-count profiles. Hence the submitted variance-resolves-nine classification is an immediate special case of stronger exact coverage. Faller–Pardi–Steel 2008 full primary Lemma 2.1 already gives the nested-clade covariance formula, from which the displayed 2p(1-p)^7 gap is a routine explicit two-tree evaluation. Neither reformulation nor specific gap creates an unaddressed original substantive claim.

## value

FAIL

FAIL for original scientific contribution: The first collision threshold and all-size 15 two-moment identification are pre-established. The attractive explicit variance gap is a small special-case numerical identity from a 2008 general covariance formula applied to the already documented size-multiset collision; no new classification, structural obstruction, or independent theorem remains after those prior results are credited. It is a useful worked illustration but not a new valuable finding under the stated V bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
