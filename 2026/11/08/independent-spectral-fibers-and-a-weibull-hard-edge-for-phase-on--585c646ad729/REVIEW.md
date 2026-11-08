# Scientific review

## Correctness — PASS

The normalization is unit window norm, with exactly \(2p\) atoms in dimension \(2p\). Even-modulation orthogonality reduces the exact frame operator to \(p\) Hermitian \(2\times2\) Gram blocks. Both columns in each block have norm one. The cyclic seam swaps the two half-block coordinates; using the seam's **sum** of phase differences, together with ordinary first differences elsewhere, is essential. The corresponding integer phase map has determinant of magnitude two and hence pushes product Haar measure to product Haar measure, making all spectral blocks exactly independent. Elementary angular integration yields the finite lower-bound law. The hard-edge and ratio limits follow from the \(\sqrt{x}\) lower-tail expansion. The all-positive-moment limit has an explicit common integrable tail; the inverse-moment threshold uses a two-sided local power law. The log-determinant law follows from the classical Fourier series for \(\log(2\sin u)\). The accompanying checker passes 27,979 finite checks, including direct full synthesis matrices and exact phase-map determinants.

Risk: the infinite probabilistic statements rely on the analytic Haar and asymptotic arguments, not on the finite checker. The theorem is restricted to the stated geometry and ensemble.

## Originality — PASS relative to checked sources

Asipchuk–De Carli–Rodriguez (arXiv:2605.16139) establish subgroup-based block equivalence, but this structural result alone does not imply independent spectral fibers, a finite exact CDF or the hard-edge law. Salanevich (arXiv:1902.01062) and Salanevich–Strachan (arXiv:2509.01325) treat random time-frequency matrices, including constant-modulus Steinhaus windows, chiefly by nonasymptotic frame-bound estimates and generic or high-cardinality sampling designs. In the inspected relevant sections, neither gives the exact two-translation/even-modulation square-ensemble law or its sharp \(p^{-2}\) scaling. Searches also considered phase-only and Gaussian random-window aliases, complete frame-spectrum laws, hard edges and cyclic block transformations. The result is distinguishable by its cyclic seam and integer Haar-map mechanism.

Risk: an unindexed specialized result may contain this exact law under another normalization; publication priority is not independently certified.

## Mathematical value — PASS

The lower frame bound governs worst-direction noise amplification. Here a natural unit-norm, square, constant-modulus Gabor measurement system has an exactly solvable dependent random-matrix spectrum, unexpectedly independent after a phase change of variables. The exact finite CDF, \(p^{-2}\) Weibull scale, associated Fréchet condition-ratio limit, sharp moment threshold and explicit log-volume law distinguish this family from the Gaussian-amplitude setting. The insight is not merely numerical or a reparameterization of an already known frame bound: it identifies the special phase-geometry mechanism responsible for a different hard-edge exponent.

Risk: other translations, sampling patterns and phase distributions may behave differently, and the theorem does not assert universality.

Self-review: passed. Independent audit: not yet performed.
