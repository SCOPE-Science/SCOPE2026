# Self-review

## Correctness — PASS

The theorem was reconstructed from the continuous-time generator and regenerative site representation. Conditional Poisson immigration gives the stationary single-site PGF exactly; the first-order expansion is controlled for each positive site reset rate, and multiplying independent site PGFs yields a normalized compound-Poisson law. The one-founder birth–death transition probability was independently checked by its linear-fractional form. On the high-fitness scaling, the proof verifies the essential quantifier condition \(n(1-\ell)\to0\) from \(n r(\ell)\to s>0\) and \(0<\nu<1\). The moving-index geometric factors have a small-\(y\) negligible part and an integrable majorant elsewhere, establishing the Bessel kernel. The included `CHECK.py` passed 319 consistency checks; no finite computation stands in for the limit proof. The exact probability law of a simultaneous interacting finite network remains unproved.

## Originality — PASS (best-knowledge priority)

The motivating full text by Grange (2023) establishes the local-reset mean-field model and mean density, while Kapodistria, Phung-Duc and Resing (2015) already prove fixed-site factorial moment formulas. A previously available same-model study, *A hidden co-occupation threshold below fitness condensation*, proves the integrated pair-occupancy threshold. An accessible earlier result also covers all higher-order integrated factorial-intensity transitions; accordingly, no moment threshold is presented as novel here. The present assessed claim is instead the entire dilute-level compound-Poisson jump law and the universal near-critical Bessel moving-size limit. Full relevant primary sections and the earlier pair result's complete text were inspected. Searches for Bessel-family cutoff equivalents in published-finding corpus and broader branching-catastrophe literature found no matching statement, but publication-priority uncertainty remains, particularly for differently named immigrant-family representations.

## Mathematical value — PASS

The result describes actual large-family jump intensities, not just their low-order moments or a slight parameter variation. A single rescaled function \(2\sqrt{s}K_1(2\sqrt{s})\) predicts the whole crossover between critical family-size abundance and the clearing cutoff, revealing the characteristic size scale and its non-exponential stretched-tail shape. That observable supplies a new physical diagnostic of fitness-dependent clearing. It is confined to a rigorously specified mean-field marginal system and is not asserted to solve finite-network joint fluctuations.

## Closest literature and limits

See Grange, arXiv:2311.12414v1, Sections 3–5; Kapodistria et al., Eurandom 2015-006, Lemma 3.1 and Section 5.3; the published prior pair-threshold result; and Lambert, arXiv:1009.0118 (log-series background). The full texts of Lambert and Dori et al. were not inspected, so unindexed near-critical branching-family equivalences are a residual scientific risk. The parameter window is \(0<\nu<1\) with the multiplicity limit before the joint fitness/large-family limit.

Self-review: passed. Independent audit: not yet performed.
