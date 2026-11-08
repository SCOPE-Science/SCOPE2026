# Scientific review: Markov persistence and expanding-map fluctuations

## Correctness (C): PASS

The object is precisely the stationary two-state environment coupled to integer circle-expansion maps and the centered coordinate observable. The map-composition identity, conditional-uniformity, exact transfer relation, and matrix Green–Kubo sum reproduce the stated variance and derivative without asymptotic approximations. The derivative identity is exact and has a strictly positive denominator. For the functional limit, the mixing proof uses BV variation contraction and finite-state environmental mixing; the reversed chain has an explicitly bounded Poisson solution, giving bounded martingale differences and the functional martingale CLT. At perfect persistence the environment freezes, producing the stated mixture of two deterministic-map CLTs. Supporting code passes 159 exact-rational finite checks, but does not replace the infinite-time arguments.

## Originality (O): PASS with publication-priority risk

Suzuki, arXiv:2303.17521 (sections 1–5, especially the non-i.i.d. density Theorem 5.1), derives invariant-density formulas but no exact persistence-indexed centered-coordinate asymptotic variance, monotonicity derivative, or frozen-environment mixture transition. Hafouta, arXiv:2109.11073 (intro, general functional limit theorems, and martingale machinery), supplies broad functional limit results; their implication toward a Brownian limit is acknowledged, not claimed new, and does not provide the explicit persistence formula. Aimino–Nicol–Vaienti (2013), Proposition 3.4 and Example 7.3, treats general annealed limit laws for independent integer maps, not Markovian slope persistence; its openly accessible full manuscript was inspected. The closest indexed published mathematical-record full result was also inspected: it addresses zero-variance rigidity and noise-onset under independent switching, not exact monotonicity for a correlated two-state environment. Classical beta-map spectral theory contains the degree-one transfer identity and is credited. An equivalent formula in unindexed studies remains possible. The searched and inspected evidence does not exhibit a dominating previously published theorem with the complete stated parameter and endpoint conclusion.

## Mathematical value (V): PASS

Environmental persistence changes temporal correlation without changing either the invariant positional distribution or the marginal distribution of slopes. The formula and sharp derivative quantify this otherwise hidden dynamical response in a natural fully solvable setting; the frozen-endpoint law demonstrates that convergence of second moments alone cannot preserve Gaussian fluctuation behavior when the driving process loses ergodicity. This is a complete fluctuation classification for a motivated two-state integer-beta family, not a generic re-statement of the functional central limit theorem.

## Limits and priority checks

The original part is the exact parameter law, strict derivative criterion, and non-Gaussian boundary contrast; neither single-map invariance nor generic functional CLT is claimed as original. No noninteger slopes, asymmetric Markov chains, arbitrary observables, quenched limit, or nonstationary initial environments are classified. General Markov additive-functional methods and unindexed random-beta literature could contain an equivalent specialization. Independent mathematical audit and publication-priority certification have not been carried out.

Self-review: passed. Independent audit: not yet performed.
