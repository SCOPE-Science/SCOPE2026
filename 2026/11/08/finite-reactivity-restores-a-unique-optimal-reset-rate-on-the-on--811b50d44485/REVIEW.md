# Scientific review

## Correctness — PASS

The free-walk resolvent satisfies the two-sided recurrence and its value at the origin is the reciprocal of \(\sqrt{r(r+4)}\). Rank-one killing and first-reset renewal yield the explicitly stated mean, with all rates, integer distance, boundary values and order of limits specified. Differentiation gives a polynomial with exactly one coefficient sign change and opposite endpoint signs, proving a unique simple optimizer for every finite positive reaction rate. Separating the objective into perfect-absorber and reaction-resistance terms, then differentiating their strictly increasing ratio, proves strict reactivity monotonicity. The nearest-neighbor root and its square-root singular asymptotic follow algebraically. The embedded checker verifies exact rational identities on a parameter grid and independent root checks, but is not substituted for the analytic proof. Risk: modeling normalization must retain unit hopping **per edge**, not unit total jump rate; this is fixed by the generator definition.

## Originality — PASS, qualified

Hartmann and Majumdar, arXiv:2505.19903 (Secs. on one-dimensional perfectly absorbing lattice targets and high-reset neighbor behavior), already prove the singular perfect-absorption phenomenon. Das and Giuggioli (2022), J. Phys. A 55, 424004 (Secs. 2.4 and 3.1.3), already give discrete-time partially absorbing lattice resetting mean expressions capable of determining the present continuous-time mean by scaling. Hence **neither the resetting renewal equation nor the exact mean itself is original**. Whitehouse–Evans–Majumdar (2013) and Schumm–Bressloff (2021) treat continuum partially reactive resetting and non-lattice geometric optimizations. Against those sources, the newly checked claim is the all-distance uniqueness, strict reaction-rate dependence, and exact nearest-neighbor crossover to an infinite optimal reset rate. Targeted searches for equivalent lattice-reactivity optimization results and a semantic index search did not identify a published theorem giving this combined classification. The limitation is an unindexed or overlooked stronger optimization theorem, or a discrete-time result whose parameter transformation implies all three conclusions implicitly.

## Value — PASS

The nearest-neighbor lattice anomaly is qualitatively unstable under physically natural finite trap reactivity: an infinite optimal reset rate becomes a finite unique one, and the singular \(\sqrt\kappa\) crossover precisely quantifies how the ideal-target approximation fails. The same theorem proves unique design calibration and monotone rate tuning for every lattice separation, while identifying the sharp distinction between neighbor and farther targets. This is a natural complete structural classification rather than an arbitrary finite parameter slice or merely a rearrangement of a known mean. It supplies actionable asymptotic information absent from a raw renewal expression. It does not claim broad multidimensional optimality or microscopic chemical realism.

## Closest literature and residual risks

- Hartmann–Majumdar (2025), arXiv:2505.19903: perfect absorbing target and nearest-neighbor infinite-rate optimum, already known.
- Das–Giuggioli (2022), DOI 10.1088/1751-8121/ac9765: partial-absorption lattice mean formula in discrete time; underlying resolvent dependence is prior work.
- Whitehouse–Evans–Majumdar (2013), arXiv:1301.2489: continuum partial reactivity adds inverse-absorption-rate correction.
- Schumm–Bressloff (2021), arXiv:2104.09372: general renewal and continuum partially absorbing target optimization.

The global all-distance lattice theorem has not been independently audited. A stronger indexed or unindexed lattice optimization result could supersede originality, and extension beyond the specified generator is not proved.

Self-review: passed. Independent audit: not yet performed.
