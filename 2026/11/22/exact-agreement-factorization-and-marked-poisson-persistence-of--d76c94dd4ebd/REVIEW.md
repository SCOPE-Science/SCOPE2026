# Scientific review

## Correctness — PASS

The general coupled-choice model is exactly specified, and each cell's joint indicators factor over an independent row-pair and column-pair. Enumerating same-cell, nonattacking, same-row, and same-column contributions yields the stated finite covariance identity. For any fixed marked factorial moment, nonattacking tuples factor exactly and the total contribution of attacking tuples is bounded by \(O_r(1/m+1/n)\), using the distinct-index bound \(1/[k(k-1)]\) for a paired choice. This proves the three independent Poisson point-process limits. The payoff-retention formula follows by conditioning on the candidate retention and integrating the joint comparison probability. Its limiting coefficient follows from a boundary Laplace integral. The attached reproducibility script passes 224 exact and finite checks, including exhaustive order and map enumeration. The computations do not substitute for the proof.

## Originality — PASS, subject to historical-priority risk

The closest identified one-game results give an asymptotic Poisson-one equilibrium count but do not determine cross-version covariance or common-cell intensity. Stanford (1996) investigates symmetry within one game; Mimun, Quattropani and Scarsini (2022) correlate the two players' payoffs *within* a game, producing different equilibrium statistics, while Heinrich et al. (2023) analyze equilibrium existence and best-response dynamics in a single game. The near-neighbor perturbation work of Varsos, Flouris and Bitsaki (2023) uses additive misinformation and finite two-by-two games. The exact agreement factorization and the coupled marked Poisson laws are not implied by the inspected statements. Stanford's full text was not accessible and a broader historical general theorem of coupled random mappings may exist; the searched sources do not establish its absence.

## Value — PASS

The single-game count remains asymptotically Poisson with mean one for every retention level, concealing a substantive loss of stability. The new exact factorization separates row-choice and column-choice agreement, and the limiting three-color law quantifies surviving equilibria, losses, births, and simultaneous nonexistence. A half-retained random payoff array has limiting common-equilibrium intensity only \(1/9\). These are natural robustness quantities for random ordinal games and random bipartite choice networks, rather than a relabeling of one-time counts.

## Limits

The result assumes independent players' payoff tables, atomless distributions and both dimensions diverging. The primary mathematical classification is combinatorial probability (MSC2020 `60C05`); the game-theoretic interpretation is an application. Historical priority is not equivalent to a proof of uniqueness, and independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
