# Scientific review: rectangle-free matrix Walsh stability

## Correctness

**PASS.** Equation (1) partitions all \(C_4\)-free \(3\times n\) matrices into light columns, pair-labelled heavy columns occurring at most once each, and a possible single all-one column. The integer divisibility proof groups triple-pair assignments into signed \(3\times3\) permanents, each even, while every remaining light factor is even. The explicit three-special-column frequency gives exactly \(-2^{n-2}\); four all-zero-light-weight columns give a genuine zero. At widths two and three, the total and one-coordinate counts imply the full Walsh spectrum is \(2\pmod4\), proving nonvanishing independently of finite extrapolation.

The two standalone exact checkers agree on all sizes through five, with the C++ whole-transform checker extending to seven. Each complete spectrum satisfies Parseval. The spectral-theorem normalization is counting convolution, so the pseudoinverse norm is the reciprocal of the least nonzero multiplier, with no hidden group-size factor.

## Originality

**PASS within the stated bounded comparison.** Kitaev–Mansour–Vella (2005), Section 3.1, count matrices avoiding a monochromatic \(2\times2\) rectangle in *either* binary color; they do not address the all-one-only \(C_4\)-free set's signed transform. Their \(3\times3\) count \(168\) differs from the one-color count \(334\). Ju–Seo (2011), introduction and conclusion, explicitly distinguish single-color avoidance from simultaneous-color avoidance and identify the former with \(C_4\)-free bipartite graphs; their treatment is enumerative, not an all-frequency inverse-stability theorem. Relevant mathematical-record comparisons on binary rectangular graph families, graph-exclusion Fourier sampling, and \(K_{3,n}\) spanning trees, matchings and orientations found different indicator families or sampling operators. Claim implication and complement duality were examined; nothing inspected determines the present uniform dyadic gap and four-column singularity.

Unindexed signed-graph tables and unpublished generalizations remain a historical-priority risk. Bounded searches are not a proof of universal uniqueness.

## Value

**PASS.** The condition of forbidding a \(2\times2\) all-one rectangle is the exact \(C_4\)-free condition for labelled bipartite graphs, a standard extremal-combinatorial family. Already at a fixed three-vertex shore, its full Fourier recovery changes sharply between width three (complete recovery) and width four (a nontrivial kernel). The theorem gives not just a positivity or parity test but the exact least nonzero multiplier, exact inverse-on-range Hilbert norm, and exact positive-spectrum condition number for every width. These determine a natural stability invariant of the convolution operator that does not follow from the ordinary counting sequence.

## Closest literature and scientific limitations

The 2005 article's two-color monochromatic avoidance and the 2011 article's one-color enumeration are the nearest primary references. The result does not generalize to four or more rows, determine all high-width Fourier nullities, or provide endpoint Banach-space inverse norms. The \(n=4\) rank is computed by exhaustive exact integer arithmetic; only the all-width threshold and gap are proven symbolically.

Self-review: passed. Independent audit: not yet performed.
