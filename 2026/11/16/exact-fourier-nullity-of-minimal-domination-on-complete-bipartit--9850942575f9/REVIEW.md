# Scientific assessment: exact Fourier nullity for biclique minimal domination

## Correctness — PASS

The exact domain is every ordered pair of integers \(m,n\ge2\) with counting-measure, unnormalized convolution on \(\mathbb F_2^{m+n}\). The minimal dominating sets have exactly three forms: the two full shores and the cross-shore pairs. Their character sums give \(W=(m-2i)(n-2j)+(-1)^i+(-1)^j\). A modulo-four argument proves the even-even zero condition; separating equal and opposite sign parities proves the even-odd conditions, including the uniquely selected near-central weight pair. Binomial multiplicities give the displayed three-case nullity. Character diagonalization yields rank, pseudoinverse norm and the condition number, with explicit frequencies attaining the least positive modulus and the trivial character attaining the maximum. The packaged checker recomputes the support and exact coefficients independently through side sizes six, and checks weighted nullity through size forty. Finite checks are not used as a general proof.

## Originality — PASS under bounded comparison

Anthony and Picollelli's 2013 full-text article on complete multipartite domination polynomials proves graph-identification results for an unsigned, univariate generating function, not the all-frequency signed transform or its zero-multiplier arithmetic. The 2014 full-text work of Kanté, Limouzy, Mary and Nourine addresses enumeration reductions and algorithms, with no Walsh theorem located in the inspected manuscript. The accessible indexed sections of Golovach and collaborators' 2016 chordal-bipartite enumeration paper address incremental-polynomial enumeration and structural flipping. They do not present the character-weight zero count in the accessed material, but that complete article was inaccessible for a page-by-page examination. Current mathematical record searches and comparison against available closely related earlier results did not identify a statement implying the exact nullity formula. General minimal-set enumeration and the elementary support classification themselves are not claimed as original; the new claim is the complete two-parameter signed-spectrum classification.

## Mathematical value — PASS

The theorem determines a natural harmonic-analysis invariant for every complete bipartite graph in an infinite two-parameter family: exact convolution rank, sharp Hilbert-space inverse stability and a parity-controlled full-rank transition. For balanced graphs it gives the exact loss of Fourier modes as \(2^{-N}\binom N{N/2}\) for even \(N\), versus none for odd \(N\), with a proved square-root asymptotic for the singular proportion. This is not determined by the ordinary one-variable domination polynomial, which forgets the individual vertex phases. The natural question is recoverability of a signal under convolution with a minimally dominating configuration mask, not an arbitrary chosen parameter slice.

## Closest literature and limitations

References are listed in `RESULT.md`. Historical-priority verification is bounded, with residual risk from an unidentified multivariate minimal-domination or signed character-sum identity. The full 2016 article was not accessible in this examination. No inference is made for shores of size one or for non-complete bipartite graphs. Endpoint \(\ell^1\)/\(\ell^\infty\) projection constants and independent mathematical validation are not provided.

Self-review: passed. Independent audit: not yet performed.
