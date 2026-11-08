# Scientific review: sharp maximum-offspring laws for subtractive random forests

## Correctness — PASS

For each positive vertex, the completed offspring count has the exact Poisson-binomial law from distinct iid lag variables. Matching marginal log-tail exponents are obtained by the first-\(k\)-children lower event and an exponential Markov bound on the generating product. Specifically, stretched-exponential lag masses give \(-\log\Pr(D\geq k)\sim c k^{\beta+1}/(\beta+1)\), while polynomial masses give \(-\log\Pr(D\geq k)\sim s k\log k\). The maximum upper bound uses the union bound over at most \(n\) positive vertices. The lower bound uses \(\lfloor(n-1)/(k+1)\rfloor\) disjoint arrival blocks, each producing \(k\) offspring with probability \(\prod_{j=1}^k q_j\); the corresponding events are independent. A dyadic Borel–Cantelli argument and monotonic interpolation establish both almost-sure limits for finite-time and completed degrees. Boundary conditions, full support, the fixed iid law and the exclusion of nonpositive roots are explicit. The supplied standard-library checker completed 398 exact finite assertions for geometric lags; finite enumeration is a consistency test, not an infinite proof.

## Originality — PASS, with historical-priority qualification

The directly relevant full-text source Broutin, Devroye, Lugosi and Oliveira, *Subtractive random forests* (arXiv:2210.10544, submitted 19 October 2022), Proposition 5, proves a distribution-free one-sided upper bound of order \(\log n/\log\log n\), and Remark 5 supplies the single-vertex Bernoulli representation. Neither asserts matching almost-sure constants nor stretched-exponential and polynomial universality classes; the known upper bound cannot yield either result by itself. Calvillo, Devroye and Lugosi, *Subtractive random forests with two choices* (arXiv:2405.10455), studies a different attachment process. Searches for maximum-degree and offspring extremes under alternate terminology did not find the same result. The related Baccelli–Sodre renewal-forest source was available only at abstract level; it remains an explicit priority uncertainty, not a full-text negative comparison. Classical extreme-value or Poisson-binomial tail theorems may offer alternate proofs and are not claimed to be new.

## Mathematical value — PASS

The original model's published maximum-degree bound is uniform across all lag laws. These two tail classes have fundamentally different sharp degree-growth scales: the geometric model is of square-root-logarithmic order instead of logarithmic-over-logarithmic order, and a polynomial mass law has a sharp multiplicative coefficient depending on its exponent. Both the original lag mechanism and extreme positive-vertex offspring are mathematically natural; the result quantitatively explains the influence of local attachment decay and supplies a matching-lower-bound method despite dependence between nearby vertex degrees. It is not a mere finite table or a renamed standard estimate.

## Literature and limitations

- N. Broutin, L. Devroye, G. Lugosi and R. I. Oliveira, *Subtractive random forests*, arXiv:2210.10544, Section 6, Proposition 5, Remark 5. https://arxiv.org/html/2210.10544v3
- F. Calvillo, L. Devroye and G. Lugosi, *Subtractive random forests with two choices*, arXiv:2405.10455. https://arxiv.org/abs/2405.10455
- F. Baccelli and A. Sodre, *Renewal processes, population dynamics, and unimodular trees*, Journal of Applied Probability 56 (2019), 339–357. Full content not inspected; relevance to extreme offspring degrees cannot be fully excluded.

Only first-order almost-sure maxima are established. No distributional limit or second-order correction is claimed. Absence from examined sources does not establish absolute historical novelty.

Self-review: passed. Independent audit: not yet performed.
