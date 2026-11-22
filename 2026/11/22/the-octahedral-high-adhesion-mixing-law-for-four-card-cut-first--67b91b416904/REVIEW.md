# Scientific review: octahedral four-card high-adhesion mixing

## Correctness — PASS

The theorem concerns three explicitly defined four-card Markov chains, fixed rescaled time \(t>0\), and \(q=1-p\downarrow0\). The complete proof first reduces the \(24\)-state chain to six four-rotation classes by a finite-dimensional fast/slow perturbation argument. It then derives the exact one-break departure coefficients \(9/16\), \(7/12\), and \(7/4\), explains why the reverse-orientation class has zero first-order transition, and uses label symmetry to assign the remaining mass equally to four neighbors. The octahedral spectrum yields the two-exponential total-variation law, and monotonicity gives the asserted mixing threshold. A separately executable, exact-rational checker enumerates every cut, bond configuration and permitted merge; it passes 7,471 assertions and reports 18 small-noise comparisons. The asymptotic statement rests on the finite-state perturbation argument, not on finite enumeration alone. No claim is made at rescaled time zero or for thresholds at least \(5/6\).

## Originality — PASS against examined sources

Jiang [1] defines precisely these three shuffles and proves the order \(\Theta((1-p)^{-1})\) at fixed deck size. The exact strong-adhesion rate constants, octahedral six-class generator and two-exponential limiting distance are not given in the inspected Definitions 2.1–2.3, Theorem 10.1, Sections 12–13, or their numerical tables. Jonasson–Morris [2] investigates a Markovian label-driven clumpy shuffle with a different cut mechanism, and Sellke–Shi–Wang [3] proves cutoff for ordinary card-interleaved riffles with general cut laws, not the adhesive one-break quotient. Related publicly indexed studies of riffle inversion counts and two-tag Thorp-shuffle spectra have different objects and conclusions. The search does not prove priority against all historical or unindexed literature.

## Value — PASS

At four cards the six cyclic orders form the first nontrivial orientation quotient after deterministic-like rotational mixing. The result gives the full macroscopic trajectory of total-variation distance rather than only a mixing-time order, and separates three implementations sharing the same power-law divergence by exact, substantially different constants. The octahedral identification and the universal profile expose the mechanism; this is neither a numerical optimization at one adhesion value nor a restatement of the motivating bound. Extension to larger decks is open and not needed for the stated finite-deck result.

## Closest literature and limitations

[1] Yunjiang Jiang, *Adhesive riffle shuffles: simple one-parameter models, interpolation, and parameter-dependent mixing bounds*, arXiv:2611.02092v1 (2026), https://arxiv.org/html/2611.02092v1. [2] Jonasson and Morris, *Rapid mixing of dealer shuffles and clumpy shuffles*, ECP 20 (2015), https://doi.org/10.1214/ECP.v20-3682. [3] Sellke, Shi and Wang, *Universality of Cutoff for Riffle Shuffling*, arXiv:2510.22783 (2025), https://arxiv.org/abs/2510.22783. The model [1] is a publicly available working manuscript rather than an independently refereed theorem source. The derivation remains conditional only on its explicit model definitions; all mathematical claims above are proved anew. Historical priority and independent mathematical assessment remain open.

Self-review: passed. Independent audit: not yet performed.
