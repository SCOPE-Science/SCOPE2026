# Scientific review: functional diversity limit for finite-state Markov stick breaking

## Correctness — PASS

The claim is a functional limit over \(0\leq t\leq1\), plus an almost-sure logarithmic diversity law and an explicit two-state coefficient. Bounded break fractions give \(\delta e^{-S_{j-1}}\leq w_j\leq e^{-S_{j-1}}\), an exact residual-tail identity and a positive minimum increment of the log-residual walk. Uniform early-box and late-tail estimates sandwich the entire occupied-box process between renewal counts with horizontal displacement \(O(\log\log n)\). Finite-state Markov Poisson equations produce the additive functional martingale FCLT; inversion supplies the Brownian process limit, including the correct \(\mu^{-3/2}\) normalization. A Borel--Cantelli argument at exponential sample sizes establishes the almost-sure assertion. The two-state covariance identity follows directly from the nontrivial transition eigenvalue. The saved finite rational verifier checks these algebraic ingredients; it is not a substitute for the infinite argument.

## Originality — PASS (provisional historical priority)

The January 23, 2026 source *Markov stick-breaking processes* by Gil-Leyva, Lijoi, Mena and Prünster develops Markov break kernels, ordering and posterior tools; its cluster-count discussion is finite-sample/computational, and its inspected sections and appendix do not give this functional diversity limit. The classic Bernoulli sieve theorem of Gnedin, Iksanov and Marynych (arXiv:1001.4920v1, theorem 1.1) assumes iid residual factors, so a nontrivial Markov chain with nonzero serial covariance is not within its stated hypotheses. A 2016 functional Bernoulli-sieve theorem of Alsmeyer, Iksanov and Marynych treats the number of boxes of sizes at most \(n^t\) after \(n\) observations, not the number observed among the first \(n^t\) draws; its iid factors and general fixed-frequency comparison tools are acknowledged. The iid specialization and the standard Markov additive CLT are established ingredients, not claimed new. The present combination yields an explicit dependence-sensitive process-level occupancy conclusion. No directly covering statement was located through searches for Markov-dependent residual allocation, Markov-modulated Bernoulli sieves, functional occupancy limits, or the exact two-state coefficient. Search absence alone does not prove priority; a more general existing theorem for stationary random frequency sequences is a residual risk.

## Mathematical value — PASS

The count of distinct observed species is a central quantity for random discrete priors, specifically evaluated in the motivating source. Its full logarithmic sample-size fluctuations are not determined by the marginal break law: dependence changes the Brownian variance by the nontrivial Green--Kubo factor even while the diversity growth coefficient remains fixed. For symmetric two-state chains the same marginals produce arbitrarily small or large Gaussian variance coefficients as the persistence eigenvalue varies. This is a motivated scaling law, not an arbitrary finite slice, and the functional result is useful for multiple nested sample sizes. The assumptions and nonclaims (endpoint breaks, nonstationarity, finite-sample variance convergence and numerical rates) are explicit.

## Closest literature and limits

1. Gil-Leyva et al., *Markov stick-breaking processes*, arXiv:2601.16561v1 (2026), main text and appendix B.8, https://arxiv.org/html/2601.16561v1.
2. Gnedin, Iksanov and Marynych, *Limit theorems for the number of occupied boxes in the Bernoulli sieve*, arXiv:1001.4920v1 (2010), section 1 and theorem 1.1, https://arxiv.org/html/1001.4920v1.
3. Alsmeyer, Iksanov and Marynych, *Functional limit theorems for the number of occupied boxes in the Bernoulli sieve*, arXiv:1601.04274v1 (2016), introduction, Theorem 2.2 and section 4, https://arxiv.org/html/1601.04274v1.
4. De Blasi, Mena and Prünster, *Asymptotic behavior of the number of distinct values in a sample from the geometric stick-breaking process* (2022), abstract and stated model, https://doi.org/10.1007/s10463-021-00791-6.
5. Dietz, Lippitt and Sethuraman, *Stick-Breaking Processes, Clumping, and Markov Chain Occupation Laws* (2023), abstract and stated model, https://doi.org/10.1007/s13171-020-00236-x.

This is not an independent validation or a claim of exhaustive historical novelty.

Self-review: passed. Independent audit: not yet performed.
