# Scientific assessment: monomorphic ESS rarity in Gaussian co-colonization games

## Correctness — PASS

The claimed random object is exactly the independent Gaussian interaction ensemble and structured payoff in Nassor et al. [1, Eq. (22)]. For every fixed integer \(N\ge2\), the proof reduces strict pure-state evolutionary stability to \(N-1\) negative invasion fitnesses, derives the one-site Gaussian integral by conditioning on a diagonal, and verifies the zero-ratio count is a binomial sum of independent row-maximum indicators. Gaussian integration by parts proves strict decline of the mean for \(N\ge3\). An exact two-site overlap integral is expanded with an integrable Gaussian second-order remainder, while independent antisymmetric pair contrasts give \(O_N(\mu^{-2})\) triple-overlap control. Finite inclusion-exclusion establishes the full trichotomy. The code checks finite examples, not the limit proof.

Potential error boundaries: the formula concerns strict **monomorphic** ESS states only; \(N\) is fixed before \(\mu\to\infty\); and diagonal interactions are independent Gaussians rather than deterministically zero.

## Originality — PASS, within inspected literature

Nassor et al. [1, §§4.2–4.3 and Figs. 15–16] specify the same Gaussian structured ensemble and measure ESS multiplicities numerically over all supports. Their reported disappearance of multiple ESSs as \(\mu\) grows does not give the exact monomorphic mean or its fixed-\(N\) asymptotic coefficient. Madec and Gjini [2] analyze the co-colonization model and antisymmetric limit, with some other interaction-distribution or diagonal conventions; neither is a direct derivation of this fixed-\(N\) pure-state count. Hart, Rinott and Weiss [3] prove random-game ESS statements for a different, independent-payoff ensemble. Chawanya and Tokita [4] analyze antisymmetric dynamics, but only their abstract was accessible and the full comparison remains limited. Searches for equivalent correlated Gaussian invasion-proof vertex laws and stronger rare-mutual-invasion laws did not surface the same theorem. This is a literature-bounded assessment, not a claim of universal priority.

## Scientific value — PASS

The count of distinct one-strain ESS endpoints is a natural restricted multiplicity statistic for alternative strain dominance. The exact zero-ratio binomial law, monotone expectation and the sharp \(\mu^{-1}\) correction determine how quickly **alternative monomorphic states** disappear as co-colonization becomes rare. The coefficient is explicit for every finite community size and supplies a quantitatively testable benchmark for simulations at intermediate interaction ratios. These are stronger than the known qualitative antisymmetric-endpoint exclusion; the phenomenon and invariant are directly motivated by the initiating ecological model, not chosen as an arbitrary parameter slice.

## Closest prior sources and residual risks

[1] H. Nassor et al., *A system-centered probabilistic formalism linking multiple equilibria and biodiversity in ecological and evolutionary models*, arXiv:2609.17232v1, https://arxiv.org/abs/2609.17232 (full HTML §§4.1–4.3 inspected).

[2] S. Madec and E. Gjini, *The ratio of single to co-colonization is key to complexity in interacting systems with multiple strains*, https://pmc.ncbi.nlm.nih.gov/articles/PMC8258234/ (primary full text, different model statements and diagonal convention compared).

[3] S. Hart, Y. Rinott and B. Weiss, *Evolutionarily Stable Strategies of Random Games*, https://arxiv.org/abs/0801.3353 (PDF proof and main results examined; independent random-game payoff model).

[4] T. Chawanya and K. Tokita, *Large-dimensional replicator equations with antisymmetric random interactions*, doi:10.1143/JPSJ.71.429 (abstract only). Its full paper and possible unindexed near-antisymmetry equivalents are a residual historical-priority risk.

The theorem does not determine the probability of any ESS when mixed supports are included, does not provide uniformity as the number of strains grows, and does not prove ecological or epidemiological clinical outcomes.

Self-review: passed. Independent audit: not yet performed.
