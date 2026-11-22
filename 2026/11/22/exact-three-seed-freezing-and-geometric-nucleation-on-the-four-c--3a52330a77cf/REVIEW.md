# Scientific review: three-seed freezing on the four-cube

## Correctness — PASS

The claimed process has independent rate-one site clocks, unit ferromagnetic couplings, certain flips for energy decreases, fair-coin flips for ties, and no flips for increases. Its exact integer-scaled transition rates are 2, 1 and 0. The change in disagreeing-edge count is \(4-2d\), so the finite equations can be solved energy layer by energy layer, retaining within-layer neutral moves. The 222-orbit exact rational certificate is independently rebuilt by `verify_orbit_exact.py`. An independently coded full-state checker verifies the harmonic identity at all 65,536 configurations and all 720,896 transitions; its independent directed-graph decomposition finds exactly ten singleton recurrent classes. Its complete enumeration of 560 three-seed placements confirms all six exact rational probabilities and the one/two/three-seed boundary. No numerical simulation or finite-to-infinite inference is used.

## Originality — PASS on inspected evidence, with residual priority risk

The closest same-model and same-graph source is Chen–Machta–Newman–Stein (arXiv:2506.19949). Its examined model, results and frozen-state sections include finite-dimensional numerical ground-state statistics, a geometric frozen-state framework, and the theorem excluding blinkers below dimension eight. The inspected main paper does not supply a rational exact six-geometry three-seed table or sharp minimal-seed boundary. Camia–De Santis–Newman studies infinite-volume \(\mathbb Z^2\), and Jovanovski studies low-temperature crossover barriers rather than this finite zero-temperature absorption. The full text of the closest published synchronous-majority four-cube result was compared: its deterministic simultaneous update and tie-retention convention yield different dynamics and cannot imply these probabilities. The published odd-by-odd bipartite Glauber race has no tied fields and a different graph. Failed indexed searches do not establish global historical uniqueness; unindexed work and possible unpublished data underlying numerical studies remain risks.

## Mathematical value — PASS

The four-cube is a canonical smallest nontrivial even-dimensional hypercube for the four-neighbor zero-temperature spin process and is directly motivated by prior studies of frozen domains and hypercube dynamics. The six exact three-seed classes and sharp boundary identify a concrete finite nucleation threshold: two minority spins never freeze, whereas a dispersed three-spin droplet sometimes produces an eight-spin frozen half-cube despite no temperature-driven uphill flip. A contiguous three-site path cannot do so. This geometry-dependent kinetic distinction, along with fully exact basin probabilities, is not merely a rephrasing of the standard absorbing-Markov-chain method or a previously reported static fixed-point count.

## Closest literature and limits

- Camia, De Santis and Newman, arXiv:math/0103050 (2001-03-07): fair-tie zero-temperature coarsening on the infinite square lattice.
- Jovanovski, arXiv:1508.07769 (2015-08-31): low-temperature hypercube energy-barrier crossover.
- Chen, Machta, Newman and Stein, arXiv:2506.19949 (2025-06-24): closely related exact model, numerical ground-state probabilities and a separate no-blinker theorem.
- Published four-cube synchronous-majority census and complete-bipartite Glauber consensus result, URLs in `RESULT.md`.

The claim is only for standard continuous-time fair-tie dynamics on \(Q_4\), with exactly stated initial seeds. External historical-priority verification and independent scientific audit have not been performed.

Self-review: passed. Independent audit: not yet performed.
