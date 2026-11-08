# Scientific review

## Correctness — PASS
The claim quantifies over fixed distinct positive Gaussian parameters and strictly positive continuous spectra with at most polynomial upper growth. The zero-intensity normalization is the scaled version of the published formula; an independent Gaussian-tilted variance calculation gives \(I_c=2c\operatorname{Var}\). Equality at one resolution gives an exponential affine relation between Gaussian convolutions. Entire Laplace transforms and Fourier uniqueness give the exact raw spectral shift-tilt orbit. Compatibility of two such orbits yields a global finite-difference equation for \(\log S\), whose solutions are Gaussian exponentials multiplied by positive periodic functions. The growth hypothesis excludes the otherwise degenerate non-Gaussian branches. A direct two-width construction supplies the converse and ensures nonproportional aliases. The accompanying executable checker reproduces the key formulas and a nonconstant smooth example. Computation is corroboration, not proof.

## Originality — PASS relative to inspected evidence
The strongest direct predecessor is Escudero, Koliander, and Romero, arXiv:2609.18689, Theorem 1.1 and Remark 5.1. It gives a single-width first intensity and a smoothed-PSD affine gauge, not the intersection of two widths. Earlier stationary-Gaussian-analytic-function work by Feldheim (arXiv:1105.3929) provides the general expected-zero framework, not a two-resolution inverse classification. A known single-window raw-spectral orbit is acknowledged and used as the first step; it does not supply the two-width finite-difference classification. Searches for heat-kernel log-curvature equivalences, Gaussian-periodic ambiguities and two-resolution spectrogram identifiability found no directly dominating statement; this is not a proof of literature-wide novelty. Residual risk: a heat-semigroup inverse problem or periodic exponential-family paper may already encode the equivalence.

## Value — PASS
One-width zero-intensity data has a genuine translation-exponential gauge ambiguity. The theorem answers a motivated design question: whether changing the Gaussian width breaks that gauge. It gives generic recovery, an exact exceptional family rather than an ad hoc counterexample, and constructive smooth nonconstant aliases. The nonuniqueness class is infinite-dimensional and identifies a boundary relevant to population spectral inference. No finite-sample or stability claim is made.

## Scientific scope
Only strict positive continuous spectra and complete population profiles at two fixed distinct resolutions are handled. Equality of first intensities does not mean equality of entire zero processes. Identification is up to global power scale in the generic case. No publication-priority or independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
