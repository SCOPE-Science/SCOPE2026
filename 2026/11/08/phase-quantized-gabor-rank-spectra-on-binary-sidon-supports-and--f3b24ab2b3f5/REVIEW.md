# Self-review

## Correctness — PASS

The proof fixes the exact Hilbert–Schmidt/Euclidean normalization and reconstructs the Weyl eigenvalues \(N|A_g|^2\). Every nonzero shift has either zero overlap or a unique unordered pair of overlap positions, because the group has exponent two and the assumed pair sums are distinct. Each pair's two Walsh-frequency halfspaces yield the exact cosine/sine singular-value levels. Zero-shift Walsh values cannot vanish because support cardinality is odd. Phase resonance is equivalence modulo \(\mu_4\), so the class-partition formula, possible partition spectrum, and balanced finite-alphabet maximum all follow with explicit quantifiers. The conic corollary follows from nonsplit quadratic norm geometry, with a direct line-intersection proof of pair-sum uniqueness. Integer finite-field construction and direct complex ambiguity enumeration checked \(q=2,4,8,16\) for three phase alphabets; separate matrix singular-value checks confirmed normalization at \(q=2\). Remaining correctness risk is lack of independent specialist proof review.

## Originality — PASS under bounded comparison

Cilleruelo's 2010 paper defines Sidon sets by *ordered differences* and studies finite-field combinatorial bounds, which does not imply the exponent-two unordered-pair rank classification. Bojarovska–Flinth's 2015 primary work supplies the general Fourier/Gabor diagonalization and relates frame bounds to ambiguity magnitudes; these are explicitly acknowledged as prior and are not offered as novel lemmas. Their support application concerns classical difference sets and a nonvanishing criterion; its hypotheses and outputs do not state or imply the exact \(\mu_4\)-partition rank spectrum or sharp \(\ell\)-phase alphabet threshold for binary-Sidon supports. Existing published research on odd-characteristic quadratic shells or sharp Fourier extension for conics does not calculate this phase-resolved Gabor operator. The result remains potentially subsumable by a less visible general Fourier frame theorem or by another treatment of phase-labelled binary Sidon sets, so priority claims are carefully bounded.

## Mathematical value — PASS

The precise object is an experimentally relevant full Gabor intensity-lifting operator for sparse equal-amplitude masks; the exact rank describes how many complex matrix directions are linearly observable, and alphabet size is a natural mask-design parameter. The result identifies a finite fourth-root phase obstruction, computes **all** attainable ranks, locates optimal finite-alphabet designs and quantifies an infinite conic family with two distinct limiting recovery fractions. This goes beyond a routine pointwise Walsh evaluation or mere numerical table, and retains mathematically substantive even-versus-odd support and involutive-translation boundaries. No claim is made for nonlinear phase-retrieval injectivity or general weighted extension theory.

## Prior-work limitations

Primary full-text comparisons: arXiv:1003.3576v1, Section 2 definition and finite-field Sidon bounds; arXiv:1503.05800v1, Sections 2.1–2.2 including Gabor eigenvalue/frame relations and difference-set applications. published-finding corpus records of hyperbolic-shell tomography, phase retrieval for two-tap windows, finite-field quadratic conic extension and prime-cyclic Gabor windows were compared at the statement/implication level. No independent audit or exhaustive historic priority check has been performed.

Self-review: passed. Independent audit: not yet performed.
