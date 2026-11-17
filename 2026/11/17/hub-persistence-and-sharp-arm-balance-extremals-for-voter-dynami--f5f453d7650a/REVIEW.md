# Self-review

## Correctness — PASS

The theorem is stated for the explicit rate-one vertex-update voter model, with a single initial center opinion-one and all peripheral opinions zero. Freezing the center before its first flip is legitimate because each root-copy clock can be split independently over the arms. Within each rooted path, the unique domain wall evolves as a birth–death chain. The return-before-absorption probability is exactly \(1-2/(2r-1)\) from the first positive interface state. The number of interface visits to the zero-prefix state is geometric; their total holding time has an exponential law of rate \(1/(2r-1)\). Averaging the independent root-copy hazards produces the full product. The fixation probability follows from the standard degree-weighted voter martingale, and strict concavity establishes sharp extremal arm allocations. Edge cases \(r=1\), \(k=1\), \(L=k\), and \(L=k+1\) are explicitly covered. Independent direct finite-generator and interface-generator calculations agree with the exact identities; neither is used as an infinite proof.

## Originality — PASS, qualified

The foundational persistence paper of Ben-Naim–Frachebourg–Krapivsky (arXiv:cond-mat/9511040) treats infinite-lattice and mean-field persistence/change counts, not the finite spider-tree center no-flip probability. Sood–Redner (arXiv:cond-mat/0412599) establishes classical heterogeneous-graph fixation and consensus behavior but not center persistence on arbitrary spider trees. Pickering–Lim (arXiv:1408.2130) studies complete and complete-bipartite networks and related urn state propagation, not the tree-path no-flip probability. A previous hub-persistence calculation for clique bouquets shares the central-persistence observable and the length-one star boundary; it does not encompass path arms of length at least two or the length-balancing extremal law. Semantic searches of mathematical research records and searchable literature found no direct covering result. The possibility of unindexed earlier formulas remains a residual risk and is not treated as proof of uniqueness.

## Mathematical value — PASS

The infinite-family formula extracts the effect of *arm placement*, not just total vertices and center degree, on a natural dynamic persistence event. The strict majorization extremal is mathematically informative: at fixed \((k,L)\), the same consensus winning probability \(k/(2L)\) coexists with distinct, exactly ordered no-flip probabilities. At \(L=2k\), balancing versus concentrating peripheral lengths changes the large-\(k\) persistence limits from \(e^{-3}\) to \(e^{-1}/3\), a non-vanishing structural contrast. The result is motivated by the distinction between persistence and fixation in the classical voter literature, and it is not simply an arbitrary finite table entry.

## Closest sources and remaining limitations

The principal related sources are the 1995 persistence paper, the 2004 heterogeneous-graph voter paper, and the 2014 spectral analysis cited in `RESULT.md`. The neighboring clique-bouquet claim concerns a different family and supplies no formula for nontrivial path arms. Full distributions of first-center-flip times, arbitrary initial configurations, and other attached graphs remain outside the theorem. Independent scientific validation and exhaustive historical-priority certification are not claimed.

Self-review: passed. Independent audit: not yet performed.
