# Self-review

## Correctness — PASS

The domain is the real affine-regular hexagonal plane \(G=(\mathbb R^2,\max\{|x|,|y|,|x+y|\})\). The quantity is the maximum minimum length of the images of two unit vectors under a contraction from \(G\) to Euclidean \(\mathbb R^2\), constrained to be orthogonal there. The critical factorization \(\omega_\perp(G)=\max\|[u\ v]^{-1}\|^{-1}\) is justified in both directions, including unequal image lengths. The exact inverse-operator norm comes from all six vertices of the hexagonal unit ball. Every pair of edges reduces, using signed isometries, to the same-edge case or the single symmetric two-parameter cross-edge case. The cross-edge optimization has three exhaustive regions; the derivative signs, transition curve and endpoint comparison prove the upper bound, and the explicit inverse matrix attains it. The proof is infinite/continuous in its quantifiers; the standalone finite checker is supplementary and passed 90,154 numerical assertions.

## Originality — PASS, subject to bibliographic priority risk

Zhang--Xu--Liu--Li, *Von Neumann--Jordan Constants in Banach Tensor Products* (arXiv:2609.37503, first public 27 September 2026), defines the orthogonal-contact index in equation (7). Its Example 3.12 establishes only that the affine-regular hexagonal plane cannot have two **unit** orthogonal Hilbert contacts, hence \(\omega_\perp(G)<1\), not a numerical sharp maximum. The exact tensor von Neumann--Jordan constant \(1+\sqrt3/2\) appearing in a separate indexed result bounds the contact index from above by \(\sqrt{(2+\sqrt3)/4}\), which is strictly weaker than the exact value found here. The known Euclidean Banach--Mazur distortion \(2/\sqrt3\) gives a strictly weaker feasible lower bound \(\sqrt3/2\). The same hexagonal geometry and related Birkhoff/James/Schäffer orthogonality constants do not determine this distinct optimization. Exact-phrase, numerical-value and equivalent-factorization literature comparisons found no matching result, but non-indexed prior work cannot be excluded. The primary paper was inspected in the relevant full-text material; the cited separately indexed comparator's full text was not accessible, leaving a bounded bibliographic risk.

## Mathematical value — PASS

The index is introduced to quantify orthogonality preserved by contractions into Hilbert spaces and is used in lower bounds for tensor Banach geometry. The published qualitative hexagonal counterexample is canonical. Its exact contact index resolves a motivated natural optimization, gives a sharp contraction witness and determines the numerical deficit \(1-(3-\sqrt3)/\sqrt2\). The value is not a cosmetic rearrangement of the qualitative obstruction or a recomputation of an indexed table. No general tensor inequality improvement is asserted.

## Closest sources, limits and verification

The primary published source is https://arxiv.org/abs/2609.37503 (equation (7), Example 3.12). Comparison records include *Exact von Neumann--Jordan constant of Hilbert--hexagon tensor products* (dated 1 November 2026) and *Euclidean Banach--Mazur profile of a classical hexagonal family* (dated 4 October 2026). The formula applies only to the real two-dimensional norm shown in RESULT.md; it does not prove an all-dimensional orthogonal-contact classification. The automated finite script complements but cannot replace the analytic proof, and no independent validation is claimed.

Self-review: passed. Independent audit: not yet performed.
