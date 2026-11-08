# Review of the exact Type-II pairwise label-recovery formulas

## Correctness — PASS

The result is one finite exact theorem: the binomial-rational formula recovers the residual size-two-component distribution at full pair coverage, and the skip-death recurrence recovers the expected remaining and total label-recovery draws. The proof handles the nontrivial stopping-time condition by comparing the first *forbidden* edge clock with the maximum of both the complementary coverage time and the latest selected-pair clock. This avoids the false simplification that the complement must always finish last. For a singleton complement, internal coverage is infinite and the specified matching cannot survive; for an empty complement, internal coverage is immediate. The ordered-matching factor and factorial-moment inversion have their usual exact meanings, and the transition probabilities in the recurrence sum to one. Exact independent graph-state enumeration verifies all claimed formulas for sizes 3 through 6, with further rational normalization and moment checks through size 13. See `verify.py` and `VERIFICATION.md`. The proof, rather than finite experimentation, establishes all finite \(n\ge3\).

## Originality — PASS

The accessible full texts of Berrebi et al. (arXiv:2502.02968), Tan et al. (arXiv:2507.15231), and Barak-Pelleg and Berend (arXiv:2510.23249) supply the two-coupon recovery model, a general graph-state Markov method, and a polylogarithmic upper bound on the post-coverage expected delay. The latter paper explicitly bounds the number of size-two components at coverage instead of enumerating its exact factorial moments. Its upper bound alone does not imply the displayed finite binomial-rational identities. The earlier Markov method can in principle compute exact fixed-size means, but it does not give this stopping-time formula for the complete residual law. The edge-order and exponential-race reduction is an additional exact representation. Focused published-record and semantic-database searches found no theorem implying the full statement. Standard coupon-cover inclusion-exclusion is explicitly attributed rather than claimed as new. Historical priority remains a risk because unexamined general graph-process enumerations could subsume the result.

## Mathematical value — PASS

The unresolved size-two-component count is the precise obstruction separating merely seeing all coupons from identifying every pair of coupon-label matches. Its exact law at the **random** full-coverage stopping time is not available from a fixed-time random-graph calculation without additional work. The formula gives a finite closed rational expectation for the original Type-II recovery problem, not just an order bound or isolated numerical instances; the sums use polynomially many rational operations and also recover the residual distribution. It answers a natural quantitative question left by the original Markov-chain and asymptotic analyses. It does not claim a new coupon-coverage inclusion-exclusion identity or an unproved asymptotic expansion.

## Closest literature and limits

- Berrebi et al., *The Labeled Coupon Collector Problem with Random Sample Sizes and Partial Recovery*, https://arxiv.org/abs/2502.02968 (2025-02-05): graph-component recognition and alternative Markov analysis.
- Tan et al., *The Labeled Coupon Collector Problem*, https://arxiv.org/abs/2507.15231 (2025-07-21): Type-I/II definitions and finite-state expected-time computation.
- Barak-Pelleg and Berend, *On Conjectures concerning the Labeled Coupon Collector Problem*, https://arxiv.org/abs/2510.23249 (2025-10-27): \(O((\log n)^5)\) post-coverage expectation bound, not the exact residual law in the inspected argument.
- Tauraso, *Edge cover time for regular graphs* (2008), https://art.torvergata.it/handle/2108/27711: ordinary edge-coverage context; only an abstract was accessible.

Independent review and historical-priority certification have not been performed. The theorem is limited to uniform pair drawings with replacement, Type-II label recovery and integer \(n\ge3\).

Self-review: passed. Independent audit: not yet performed.
