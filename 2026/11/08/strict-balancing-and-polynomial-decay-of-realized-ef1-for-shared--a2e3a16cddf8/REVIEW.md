# Self-review

## Correctness — PASS

The model specifies a single realized Bernoulli value for each good, shared by all agents, and independent values across goods. With common binary utilities, realized EF1 is exactly the event that the largest and smallest realized bundle-success counts differ by at most one. The proof couples a move from bundle size \(b\) to size \(a\) by transferring one Bernoulli trial, compares the success-count distributions in monotone likelihood-ratio order, and pairs antisymmetric summands. It proves the strictly positive improvement \((b-a-1)p^2(1-p)^{m-2}\), including zero-size bundles, for every \(0<p<1\). Iteration gives the unique optimal bundle-size multiset. The exact finite expression follows from interval inclusion–exclusion, and the decay constant from a binomial local limit and a Gaussian Riemann sum. Direct finite enumerations and a separate independent binary-outcome implementation agree with the package's formula. The infinite conclusions rest on proof, not finite enumeration.

## Originality — PASS, qualified

The closest paper is Igarashi and Oh, *Fair Division of Lotteries* (arXiv:2610.34906v1), which studies exact envy-freeness (EF) and gives a binomial/log-concave balancing result for the probability of equality of realized bundles. Its proposition on identical valuations and appendix's likelihood-ratio lemma do not state this EF1 event or its strict finite-horizon optimizer and polynomial decay constant; the conclusion lists EF1 as future research. Chen and Long (arXiv:2609.23577v1) randomize online assignment under fixed valuations rather than the goods' realized common values. Halpern, Psomas and Zhang (arXiv:2602.12359v1) study truthful mechanisms under stochastic valuations. Aloisio et al. (AAMAS 2024) minimize expected maximum envy instead of maximizing the probability of realized EF1. Search queries targeting binomial range probabilities, majorization, identical-valued stochastic goods and EF1 did not expose an equivalent theorem. The stochastic-order ingredient is classical and is not claimed new. A general unindexed majorization theorem could still imply the finite claim, so publication priority requires external confirmation.

## Mathematical value — PASS

The new question is specifically motivated by the gap from exact EF to EF1 under unrevealed item values. Strict balancing classifies every optimizer for any population and number of goods, while a closed probability formula gives the exact risk. The sharp constant in the \(m^{-(n-1)/2}\) success decay makes precise the limit of guarantees obtainable by a fixed ex-ante EF1 allocation as more uncertain goods arrive. For three agents and six goods with fair Bernoulli values, balanced sizes attain \(23/32\), versus \(9/16\) for \((1,2,3)\). This is not a known-table recomputation, a parameter substitution, or an assertion of a general distribution-free result.

## Scope and residual risks

All goods are exchangeable, have the same fixed \(0<p<1\), and share their realized value across agents. Nothing here proves heterogeneous or correlated-good extensions, independently sampled agent-good values, or a joint limit as the population grows. A strong probabilistic majorization theorem outside the searched literature remains a possible route to coverage. The local central limit calculation is analytic and has not been independently peer-reviewed.

Self-review: passed. Independent audit: not yet performed.
