# Scientific review

**Correctness: PASS.** The full Apéry formula of Liu–Xin–Ye–Yin, Lemma 3.3, applies to \(a=R_n\), \(d=1\), \(k=n-1\), and yields the exact membership heights. The proof checks the endpoint \(R_n=bR_{n-1}+1\), derives every height jump and its nonjoining terminal-suffix block, and proves every nonzero coefficient in the factorized histogram is \(b\). `CHECKER.py` independently verified 26 parameter pairs, including 8,585 missing-integer blocks and shortest-path Apéry tables. The finite checks are not an infinite certificate.

**Originality: PASS on the inspected evidence, with a material residual risk.** The 2023 primary paper gives Apéry, genus and Frobenius invariants, not a stated run-length polynomial or uniform multiplicity. The 2022/2023 generalized-semisgroup paper does not give this statistic either. The 2015/2016 earliest repunit-semigroup paper is highly relevant; only abstract and metadata were accessible, so an implicit exact spectrum cannot be ruled out. Published isolated-gap results for a unit-shift family are not the same objects; two-generator run-frequency results do not dominate a formula uniform over \(n\)-generator repunit semigroups. Prior Apéry formulas encode the underlying data, but extraction of the gap-run factorization requires the proved jump recurrence; novelty is claimed only for that structural distribution, not for its antecedent Apéry description.

**Mathematical value: PASS.** This is a natural, fully classified missing-integer interval statistic for a classic Frobenius family. The statement gives all lengths, an unexpected uniform multiplicity, an explicit product polynomial, sharp endpoint lengths, and the total number of blocks simultaneously across arbitrary base and dimension. It is not a table recomputation, a single finite example or an arbitrary parameter slice.

The main limitation is the unresolved older 2015/2016 full-text priority comparison; it does not make an existing Apéry formula new. Independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
