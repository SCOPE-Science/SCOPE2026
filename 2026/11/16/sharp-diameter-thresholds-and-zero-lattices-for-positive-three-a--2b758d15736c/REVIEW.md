# Scientific review: sharp Fourier-zero thresholds for positive three-atom measures

## Correctness — PASS

The cosine rule classifies cancellation of exactly three prescribed positive phasor lengths. The three successive direction gaps are the external angles of the weight triangle, so the shortest phase-covering arc is exactly \(\pi+\gamma_*\). Every real frequency maps the three sites into a real projected interval whose length is at most the Euclidean diameter multiplied by frequency norm. This gives the claimed constant with no hidden measure regularity assumption. Equality follows from simultaneous tightness of the minimal-arc and Cauchy--Schwarz inequalities. A noncollinear construction verifies attainability for all strict weight triangles. With rank two, solving the two phase congruences yields the two affine lattice cosets and the Gram-inverse minimum. A standalone numerical checker exercises cancellations, constructions and special cases but is not the proof.

Boundary checks: strict positivity of all weights; strict triangle inequalities; equal weights and tied smallest weights; all dimensions \(d\ge2\); rank-one (collinear) sites excluded only from the lattice formula; and the nontriangle zero obstruction. The statement does not claim equality attainment for degenerate weight triangles, complex-frequency zeros, or infinite-support measures.

## Originality — PASS within inspected evidence

The closest 2026 preprint, Gómez-Serrano et al., *An isoperimetric problem for Fourier zeros of centrally symmetric convex bodies* (arXiv:2609.10517), studies Fourier transforms of continuous convex-domain indicators and fixed-volume optimization. Its central theorems address bipyramids and regular centrally symmetric polygons, not weighted three-point measures. Benguria--Levitin--Parnovski (JFA 2009) treats the same domain-indicator functional. Kolountzakis--Révész (CJM 2006) proves a different support-restricted positive-definite-function extremal problem. The retrieved published three-point cyclic Fourier result concerns zero counts on finite torsion groups, and does not imply the continuum diameter/mass-angle theorem. The retrieved variance-at-a-Fourier-zero estimate is a general variance stability result and has no identified implication yielding the strict triangle-angle equality classification.

Comparisons used statements and hypotheses, not only title similarity. The key non-implication is that a fixed-volume bound on the zeros of the transform of an indicator does not transfer to a weighted atomic measure; neither does a finite-group Fourier-zero count determine the first real Euclidean frequency or the geometry of its extremizers. Historical priority remains provisional: an equivalent phasor-diameter result in diffraction, acoustic array factors, probability characteristic functions or signal-processing literature may exist. The accessible full mathematical text of the two closest repository records was not available, and only their published summaries were assessed. That is a documented residual risk, not evidence of a priority proof.

## Mathematical value — PASS

The diameter of a measure's support is a canonical geometric scale for a zero-free frequency ball. For arbitrary positive measures the elementary semicircle obstruction gives the universal normalized \(1/2\) threshold; the exact three-atom weight triangle increases it continuously to \(2/3\), and determines when cancellation is impossible at every real frequency. The theorem supplies sharp constants for all strict weight triples, all noncollinear equality configurations, and an exact two-coset formula for the entire real zero set. These are intrinsic spectral properties of atomic Fourier transforms rather than an arbitrary parameter slice. The mass-angle transition and mandatory geometry of the extremizing support explain precisely why three atoms differ from the universal two-phase threshold. They are useful for zero-free frequency design and three-source diffraction arrays. The theorem does not resolve the convex-body maximization question that motivated the study.

## Closest literature and limitations

- J. Gómez-Serrano et al., arXiv:2609.10517 (2026-09-09): first-Fourier-zero distance for centrally symmetric convex bodies; fully different measure class and extremal constraint. The preprint's introductory theorems, proofs on bipyramids, and polygon analysis were materially inspected.
- R. Benguria, M. Levitin and L. Parnovski, *Fourier transform, null variety, and Laplacian's eigenvalues*, JFA 257 (2009): convex-domain indicators and spectral geometry, not three atomic masses.
- M. N. Kolountzakis and Sz. Gy. Révész, *On pointwise estimates of positive definite functions with given support*, CJM 58 (2006): pointwise positive-definiteness problem, not the exact real zeros of a three-atom transform.
- Published records on three-point cyclic Fourier zeros and quadratic concentration at a Fourier--Stieltjes zero: related geometric and positivity language but no identified implication; full-text access limitations remain.

No historical uniqueness or external certification is claimed. The analytic proof, not the finite checker, supports the universal quantifiers.

Self-review: passed. Independent audit: not yet performed.
