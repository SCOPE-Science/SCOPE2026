# Mathematical assessment

## Correctness: PASS

The exact bfloat16 encoding formula reduces all relevant values to integers at scale \(2^{-133}\); all rounding decisions and modulo operations use exact integer comparisons. `check.py` exhaustively checks both successor graphs, independently recomputes every edge with rational fractions, and independently recomputes every directed cycle and its basin using two graph algorithms. It confirms cycle periods, exhaustive basin sums, maximal transient times and the exact changed-edge count. Invariance of the finite state space is proved directly from the output bounds. The claim is a finite-state theorem, not an inference about infinite real trajectories.

## Originality: PASS within checked literature

The source paper (Moysis et al., 2022, equations (4), (23), Figure 5 and numerical-accuracy discussion) specifies this remainder-added map and parameters but not its bfloat16 functional graph. Klöwer et al. (2023, sections on floating-point orbits, logistic and Bernoulli maps) demonstrate the general phenomenon of precision-induced periodicity, not these counts. The published binary16 beta-shift two-rounding census treats a different map, format and parameter, so its statements do not imply this specific graph. The exact-real remainder-added confinement and golden-ratio transport result likewise does not imply the finite-precision counts. A previous bfloat16 state-dependent logistic calculation concerns a distinct polynomial and has no reduction establishing these cycles. Unindexed identical computations remain a residual priority risk, not an established implication.

## Value: PASS

The chosen parameters are the published figure's canonical simplest-linear example, and the precision is a standard low-cost 16-bit format. The source's proposed digit-mixing chaotification is explicitly motivated by pseudo-random output and numerical implementation, so the complete cycle and basin inventory answers a motivated design-evaluation question. The exact period-spectrum change from \(18,24\) to at most \(3\) is substantial and not a generic finite-state tautology: finite-state periodicity alone gives none of these periods or basin counts. The finite classification is reproducible, but makes no unsupported cryptographic-security claim.

## Limits and nearest comparisons

The exact counts do not generalize to other rounding stages or integer parameters. The underlying real-valued map's expansion is not contradicted. Closest comparisons: 2022 source DOI `10.3390/math10152801`; 2023 low-precision analysis DOI `10.1038/s41598-023-37004-4`; and the published beta-shift rounding-order census at https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-two-exact-cycle-spectra-for-differently-rounded-half-precision-b--384041ddfda5.

Self-review: passed. Independent audit: not yet performed.
