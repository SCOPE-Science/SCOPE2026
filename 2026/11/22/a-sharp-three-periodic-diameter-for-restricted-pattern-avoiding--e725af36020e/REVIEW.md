# Scientific assessment: sharp diameter of a restricted permutation-swap graph

## Correctness — PASS

The claimed graph is precisely defined by ordinary pattern avoidance and adjacent-position transpositions. The 2022 inversion-vector bijection identifies its vertices with binary words avoiding contiguous \(111\). The independently justified edge correspondence requires the right neighboring inversion digit to be zero. A forced-coordinate argument gives both a lower bound and a legal two-sweep shortest path for every pair. The upper diameter bound packs forced shared-one positions at separation three, and the explicit repeated \(BDC\) construction attains the bound at every length. This is an all-length proof. The standalone `verify.py` checks exact pattern avoidance and edges directly through permutation length eight, and all shortest-path distances through inversion-vector length ten. Finite checks are corroboration, not the infinite proof.

## Originality — PASS, with historical-priority risk

Barcucci, Bernini and Pinzani (arXiv:2204.10069; first public 2022-04-21), inspected in its full publicly available HTML text, prove the inversion encoding and give a Gray listing. They do not state the exact worst-case swap distance or forced-coordinate shortest paths. Mütze's 2023 Gray-code survey is general context; only its landing-page abstract was inspected, so no full-text exclusion is claimed. The indexed 2026 result *Sharp diameter of the 321-avoiding adjacent-swap graph* states an exact metric for a larger avoidance class. A general metric on that larger class is not by itself the sharp diameter of the smaller induced subgraph: restrictions can eliminate geodesics, and optimization over a different endpoint family remains necessary. The two-pattern superclass without the \(2341\) restriction has diameter \(2n-3\), as follows directly by applying the same forced-coordinate lemma to all binary vectors; this does not imply the new smaller-class diameter. Searches found no directly matching indexed result or external exact-diameter statement. The 2026 result's full repository text was inaccessible, and an unindexed equivalent or stronger result remains a genuine priority risk.

## Value — PASS

This is a mathematically motivated global metric question for a reconfiguration graph arising directly from a published Gray-code construction. A Gray code establishes connectivity but gives little about optimal distance between arbitrary states. A single additional four-pattern restriction changes the exact worst-case distance from the unrestricted two-pattern superclass's \(2n-3\) to \(n-1+\lfloor n/3\rfloor\), with a nontrivial three-periodic law and explicit extremal witness family. The exact geodesic cost also provides an optimal constructive routing procedure. The result is limited to the stated graph and does not assert that it resolves generalized forbidden-run diameters.

## Closest work and scientific limitations

Primary original construction: E. Barcucci, A. Bernini and R. Pinzani, *Strings from linear recurrences and permutations: a Gray code*, https://arxiv.org/abs/2204.10069, Sections 4–5. Broad survey: T. Mütze, https://doi.org/10.37236/11023. Closest indexed broader metric: *Sharp diameter of the 321-avoiding adjacent-swap graph*, 2026-10-26; only its indexed summary was accessible. The specific limited-class diameter was established independently by the complete proof in `RESULT.md`; it is not a claim that other class metrics were absent from all historical literature. No independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
