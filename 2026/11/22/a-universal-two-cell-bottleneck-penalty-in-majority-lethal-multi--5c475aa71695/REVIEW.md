# Scientific review of the three-bottleneck fragmentation theorem

## Correctness

**PASS.** The statement fixes the exact parent composition, uniform-without-replacement daughter assignment, strictly-greater-than-half lethal rule, and all three observables. The two survival tests reduce to \(2j\le a\) and \(2j\ge a\), ensuring that equality can permit both daughters. Full hypergeometric enumeration for the three daughter sizes gives the displayed symbolic formulas. All claimed strict differences factor into expressions positive for every integer \(m\ge3\); no inference about arbitrary larger daughter sizes is made. `CHECK.py` provides independent labeled-configuration enumeration at \(m=3\) and finite exact-rational corroboration for \(3\le m\le149\); the infinite result rests on the symbolic proof.

## Originality

**PASS, subject to literature-coverage limitations.** The 2026 Garcia-Casillas–Wagner primary study explicitly models random daughter partitioning, infection-load-dependent death, and mixed infected–healthy contacts, and reports population-level advantages of extreme asymmetric reproduction. It does not give this conditional all-even-size parity lemma and joint analytic strict comparison of the one-, two-, and three-cell daughter sizes. The 2024 Marguet–Smadi partition-kernel work considers continuous parasite sharing at division into daughter cells and long-run population survival, not this exact finite-cell majority-lethal offspring experiment. Classical hypergeometric probabilities and simple counting identities are pre-existing tools and are not themselves asserted to be novel. Searches for the precise triple comparison, equivalent half-lethality terminology, and stronger fragmentation claims found no decisive coverage in accessible material. The presence of non-indexed combinatorial equivalents remains possible; originality is a best-knowledge assessment rather than exhaustive priority certification.

## Value

**PASS.** The exact half-lethal threshold is biologically motivated by the source's rule that organisms die once pathogen load exceeds a limit. The source's two proposed advantages of asymmetry—infectious-unit purging and within-organism transmission isolation—make expected surviving infected cells and surviving infected–healthy contact opportunities natural observables. The theorem reveals a parity mechanism that makes an intermediate offspring size systematically worse than both neighboring sizes for every even parent size from six onward; an additional prevalence-normalized comparison prevents an interpretation based solely on the intermediate split preserving more cells. These sharp bounds are a tractable test case for mechanistic models of fragmentation, without asserting general population fitness or multigeneration optimality.

## Closest prior literature and limitations

The primary comparator is A. Garcia-Casillas and A. Wagner, “Single-cell bottlenecks in multicellular reproduction can hinder the spreading of infectious disease,” *Frontiers in Ecology and Evolution* 14 (2026), https://doi.org/10.3389/fevo.2026.1816826 , especially Methods §§2.2–2.4 and Results/Discussion. The secondary comparator is A. Marguet and C. Smadi, “Parasite infection in a cell population: role of the partitioning kernel,” *Journal of Mathematical Biology* 89, article 14 (2024), https://arxiv.org/abs/2305.06962 , especially the Introduction, model §1, and analytic partitioning comparisons §3.2. The latter is structurally related but has different units and observables; it does not settle the specified claim. Full historical coverage across unindexed literature remains incomplete.

The finding is restricted to binary cell infection, half-infected parents, the strict \(1/2\) death threshold, a single random split followed by culling, and the three daughter sizes. It should not be read as a theorem for the full infection–growth–competition dynamics or for realized stochastic transmissions. No independent scientific validation has been performed.

Self-review: passed. Independent audit: not yet performed.
