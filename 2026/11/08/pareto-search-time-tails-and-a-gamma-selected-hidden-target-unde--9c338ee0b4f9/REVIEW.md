# Scientific review

## Correctness — PASS

For the stated one-time exponentially distributed target, the fixed-target Laplace transform is derived by an exact renewal decomposition. Beta integration gives the reset-count law and the first two annealed moments. A conditional exponential limit for \(rpT\) as target distance diverges is accompanied by a uniform moment-generating-function bound, so dominated convergence gives the *sharp*, rather than only logarithmic, annealed survival asymptotic. A stopped Poisson-martingale isometry proves \(pN-rpT\to0\) in conditional \(L^2\), and a second dominated-convergence calculation factors the joint conditional law into independent Gamma and exponential variables. The proof treats all \(a>0\), including critical moment thresholds. The standalone checker passed 153 finite identities and inequalities; the analytical argument supplies the infinite-limit proof.

## Originality — PASS, with priority qualification

Evans and Ray's 2024 preprint and its 2025 journal article establish the same random-target framework and identify the conjugate exponential target for Poisson resetting, including its averaged mean first-passage time. The primary full text, relevant supplementary first-passage derivations and the work of Linn and Lawley on frequent-reset asymptotics were compared at the level of their hypotheses and claims. Their formulas entail the initial fixed-target renewal representation, but do not themselves state the power-law constant, all real-moment thresholds, posterior Gamma localization or coupled reset-count/time limit at fixed rate with one quenched random target. General mixture identities may cover the simpler beta-geometric reset-count marginal; that identity alone is not presented as the independent novelty. Targeted searches for equivalent random-target, mixed-renewal and heavy-tail formulations found no directly covering full result. This is a qualified self-review, not a guarantee of publication priority.

## Mathematical value — PASS

The random target is physically motivated by search under unknown target distance. The sharp theorem resolves a concrete and consequential contrast: every fixed target has exponentially light search time, while annealing over a one-time exponential spatial uncertainty produces tunable power laws and exact moment transitions. At the previously motivated conjugate spatial density, the mean remains finite while variance diverges. The conditional Gamma selection explains *which* exceptionally distant targets dominate rare failed searches, and the joint reset-count law connects those rare events with intervention cost. These distinguishable observables are useful beyond a recomputation of known average search time.

## Closest prior literature and limitations

1. Evans and Ray, *Stochastic resetting prevails over sharp restart for broad target distributions*, arXiv:2410.01941v1, 2024-10-02; published in *Physical Review Letters* 134, 247102 (2025): matching target law and mean optimization, but no complete conditional asymptotic claimed here.
2. Linn and Lawley, *First-passage times under frequent stochastic resetting*, arXiv:2302.05409 (2023): rare-success exponential scaling as reset frequency changes, not the posterior mixing at fixed frequency.
3. Pal, Kuśmierz and Reuveni, *Search with home returns provides advantage under high uncertainty*, arXiv:1906.06987 (2019): different home-return protocol and uncertainties.

The conditional limit requires a quenched target and memoryless resets; potential generic mixture-theory coverage remains an originality risk. Computational diagnostics are not independent proof certification. No claims about non-Poisson clocks or rediscovered-target protocols are made.

Self-review: passed. Independent audit: not yet performed.
