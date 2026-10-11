---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

Exchangeability and absence of ties make the calibration/future label pattern in the joint score order uniform over all \(\binom{n+m}{n}\) binary interleavings. The map from an interleaving to counts in the \(n+1\) calibration gaps is a bijection with weak compositions of \(m\), proving the fine-gap law. Grouping consecutive gaps gives the displayed Dirichlet-multinomial mass by stars and bars, and its standard moments give the covariance formula. The dynamic program is also exact: after \(b-1\) gaps have prefix total \(t\le s\), there is a unique nonnegative choice \(K_b=s-t\); prefix sums make each row \(O(m)\). A fresh exhaustive interleaving check for \((n,m)=(4,3)\) recovered all 35 weak compositions exactly once at the unlabeled-pattern level, independently corroborating the frozen verifier.

## originality

FAIL

A stronger prior order-statistics theorem was missed by the frozen audit. O'Neill's open 2025 paper derives the joint distribution of an arbitrary vector of order statistics under simple random sampling without replacement and gives its Dirichlet-multinomial mixture representation. Apply that theorem to the random positions of all \(n\) calibration labels in the combined \(n+m\) exchangeable score order: the rank vector is exactly a simple random sample without replacement, and taking all consecutive calibration ranks makes the Dirichlet parameter vector \((1,\ldots,1)\). The induced gap counts are therefore Dirichlet-multinomial with all parameters one, whose mass is constant over weak compositions. Grouped calibration levels are the standard aggregation of the same Dirichlet-multinomial law. Marques independently supplies the conformal one-level beta-binomial marginal. Thus the principal probabilistic theorem is a direct specialization of stronger published order-statistics results; only the elementary prefix-count DP remains, and it does not rescue the combined claim under the implication-based originality rule.

## value

FAIL

Once the published joint order-statistics Dirichlet-multinomial representation is recognized, the conformal multilevel law is a textbook rank-label specialization, and the simultaneous-band algorithm is the elementary dynamic program for counting constrained weak compositions. The result is useful exposition for conformal users but does not clear the required scientific-value bar as an independent mathematical contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
