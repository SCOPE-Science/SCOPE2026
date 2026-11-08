# Scientific assessment: quadratic Specht endpoint Fourier projection

## Correctness — PASS
The two-subset permutation action has three orbitals, giving exactly three irreducible constituents, of which the nontrivial complement to the point action has degree \(n(n-3)/2\). The fixed-subset count yields its character \(\binom{X_1}{2}+X_2-X_1\). Its only negative values are \(-1\), occurring at \(X_1\in\{1,2\}\) and \(X_2=0\). Character orthogonality and the convolution kernel prove both sharp operator norms. The cycle-index generating function proves the limiting coefficient; no finite enumeration is used to infer infinitely many cases. Independent exact small-group calculations and the standalone checker reproduce the character convolution identity for groups of orders \(24\) and \(120\), and the norm formula for \(4\le n\le8\).

## Originality — PASS under bounded comparison
Character polynomials and Specht decompositions are classical, as documented in Church–Ellenberg–Farb (arXiv:1204.4533, Sections 3.3–3.4) and Wilson (arXiv:1503.08510, Section 4.1). These inspected portions develop the character-polynomial framework, not the sharp \(\ell^1/\ell^\infty\) central projection norm for the specific \((n-2,2)\) irreducible representation. Published results on the standard Fourier block of doubly transitive actions concern the distinct \((n-1,1)\) representation. Johnson-scheme projector norms concern functions on subsets rather than the full symmetric-group regular representation; their norm claims do not imply this one. Direct searches of exact norms, character aliases, and the negative-character class did not locate prior exact coverage. Search absence cannot establish historical novelty; a general absolute-character-mean formula remains a residual priority risk. The closest published standard-block record was accessible as a scientific summary, not complete text.

## Mathematical value — PASS
The central projector is the first quadratic irreducible block in the canonical action on unordered pairs of points. Its endpoint norm is the exact worst-case amplification when isolating that block from a bounded function on the entire symmetric group, a natural finite noncommutative Fourier question. A complete all-rank formula, all endpoint extremizers, and the exact normalized limit \(3e^{-3/2}/2\) are provided. The remarkable two-statistic sign collapse makes the answer computable through permutations with no short cycles; this is more informative than finite tables or an \(\ell^2\)-orthogonality calculation.

## Limitations
The claim does not determine interior \(\ell^p\) norms, nor give a universal projector formula for arbitrary irreducibles. Historical-priority review is bounded, and external independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
