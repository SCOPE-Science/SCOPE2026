# Mathematical review

## Correctness
**PASS.** Fourier diagonalization on \(\mathbb Z/N\mathbb Z\) gives the exact eigenvalue factor \(a_j[1+\beta F_j(t)]\), with all \(a_j>0\). On the upper-frequency half-grid, an exact integral expression for an adjacent log-ratio, divided by \(2t\), is strictly increasing in \(t\) and changes sign exactly once when the lower index is greater than \(N/4\). A strict continuous unimodality lemma establishes that each adjacent equality is a global two-mode tie. The straddling comparison excludes all lower indices. These establish sharpness, exhaustive strict ordering of all transition times, and the exact full-circulant boundary nullity. The standalone checker independently reproduces 200246 numerical regression and Fourier-DFT assertions on finite instances. Floating-point comparisons are not used as proof of universal inequalities.

## Originality
**PASS, best-knowledge.** The 2024 discrete-Gaussian paper and earlier cyclic heat-kernel/Bessel work supply the unmodulated spectral formula, not the signed-mask positivity threshold or the exact full mode-switching diagram. The 2024 group-heat multiplier treatment addresses regularization and completely positive semigroups rather than finite-cycle modulation. Closest published comparison: the sampled two-harmonic von Mises theorem classifies Fourier eigenvalue order for a different spatial exponential family; its theorem does not imply the current inverse-DFT heat-kernel times cosine-mask result. Existing geodesic-exponential and wrapped-Gaussian infinite-circle modulation results likewise have different base kernels, character sets, and transition equations. The comparable published statements and available prior claims do not establish the current classification. Historical priority is not exhaustively established; a classical cyclic multiplier or discrete covariance identity might be equivalent.

## Mathematical value
**PASS.** Signed modulation of a positive heat kernel need not retain positive type. The first-harmonic case is the minimal nontrivial stationary modulation, and determining the sharp admissible negative coefficient is a natural covariance-design and Fourier-positivity question. The answer is not merely a finite scan: it gives an all-order complete phase diagram with unique adjacent crossings, an exact no-skips law, and boundary nullity at every time. It resolves the mode-selection behavior uniformly for every cycle size, including parity effects, with an independent explicit equation for each transition.

## Closest literature and limits
- Chinta, Jorgenson, Karlsson, Smajlović (arXiv:2409.14344v1; first public 2024-09-22), discrete Gaussian and cyclic spectral expansion.
- Karlsson and Neuhauser (2006), cyclic heat kernels and theta identities.
- Bédos and Conti (2024), heat properties and positive Fourier multipliers for groups.
- Published studies of two-harmonic sampled von Mises spectra, geodesic-exponential circle modulation, and wrapped-circle Gaussian modulation; their precise implications were compared.

The theorem is restricted to one harmonic modulation of the nearest-neighbor cycle heat kernel. Transition roots are unique implicit values, not elementary closed forms. An independent audit and exhaustive historical search have not been performed.

Self-review: passed. Independent audit: not yet performed.
