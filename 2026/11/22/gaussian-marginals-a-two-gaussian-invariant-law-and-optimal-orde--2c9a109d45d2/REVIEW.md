# Self-review

## Correctness — PASS

The epoch matrices contract by at most \(c\) in the positive-definite Hessian norm, proving uniqueness and geometric approach to an invariant probability law with finite second moment. The proposed two-normal mixture is invariant because every complete sweep replaces both coordinates by linear functions of one input Gaussian marginal and two independent Gaussian innovations; both component covariances retain the same diagonal. Direct fourth-moment and trace identities prove the cumulant and exact stationary objective, including the boundary and equality cases. Exact symbolic assertions and independently generated epoch-chain simulation agree. Risk: this proof covers epoch boundaries under fresh independent noises and orders only.

## Originality — PASS, with priority qualification

Primary full-text reading of the 2018 quadratic coordinate-permutation paper and the 2021 random-shuffling SGD study found noiseless convergence-rate and finite-sum convergence statements, rather than a stationary two-coordinate heteroscedastic Gaussian-oracle law. A 2014 incompatible-Gibbs paper proves a general two-variable mixture phenomenon for random single-coordinate scans; this is an acknowledged antecedent, not a claimed invention of Gaussian mixing. The present *full-permutation epoch* model differs, and the strict noisier-first stationary objective rule, order-independent Gaussian marginals, and explicit mixed cumulant are not established by its stated results. A closely related published noisy randomized-Kaczmarz theorem concerns single-row with-replacement transitions, rather than independent complete epochs. Its full theorem/proof were read and compared. A published scalar finite-sum reshuffling example instead has a different recursion and objective. Priority risk: an older equivalent exact full-sweep noisy-Gauss–Seidel law may exist; mathematical novelty cannot be guaranteed by searches.

## Value — PASS

Heteroscedastic noisy coordinate oracles and randomly reshuffled epochs are standard algorithmic design ingredients. The exact invariant gives an otherwise hidden distributional distinction: univariate Gaussian diagnostics completely miss the fourth-order joint mismatch, while a simple deterministic order strictly dominates randomized full-sweep ordering in long-run quadratic error under unequal oracle noise. The full classification and exact nonzero penalty offer a rigorous design benchmark rather than an arbitrary finite calculation. Scope does not imply transient or higher-dimensional dominance.

## Closest literature and limits

Gürbüzbalaban et al. (2018), arXiv:1803.08200, defines the noiseless permutation coordinate method. Safran–Shamir (2021), arXiv:2106.06880, addresses finite-sum SGD. Chen–Ip (2014), DOI:10.1080/00949655.2014.968159, supplies a substantive general incompatible-Gibbs mixture precursor. *Gaussianity is exactly a nonorthogonality-graph compatibility condition for noisy randomized Kaczmarz* (2026) studies different sampling mechanics. An exact pre-existing full-sweep specialization cannot be ruled out; further independent priority review is warranted.

Self-review: passed. Independent audit: not yet performed.
