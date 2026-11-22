# Scientific review: certified leading covariance eigenvalue

## Correctness — PASS
The kernel is checked from the centered uniform score; positivity and trace class come from its covariance representation. The operator's polynomial action follows by Fubini. The Hilbert–Schmidt trace is independently reconstructed as \(109/8100\), rather than imported as an unchecked premise. A reproducible standard-library exact-rational checker constructs six polynomial iterates and proves the Rayleigh-quotient, residual, second-eigenvalue and Temple inequalities. The logarithmic-tail implication follows from the Gaussian spectral expansion and finite exponential moments below the dominant pole. The numerical eigenvalue is an enclosure, not a finite-rank guess or a claimed closed form.

## Originality — PASS, with residual priority risk
The original 2021 preprint by Ebner, Liebenberg and Visagie proves the limiting covariance and computes cumulants, but its Section 6 expressly leaves the leading eigenvalue uncalculated. Their fourth cumulant gives only general moment information, not the new certified interval. Relevant prior work on exact finite-sample covariance with Cramér–von Mises and on finite-sample skewness for the same statistic concerns other invariants and does not imply this spectral enclosure. Exact-title, kernel, numerical-constant, alternate-formulation and published-finding searches did not identify direct coverage. The variational and Temple inequalities are classical: the model-specific rational computation, narrow enclosure and resulting tail calibration are the claimed contribution. Indexed search cannot exclude every independent approximation or unpublished note.

## Value — PASS
The original paper specifically calls out the leading eigenvalue as needed for approximate local Bahadur efficiencies. A certified thirteen-decimal enclosure for that previously uncalculated natural invariant provides a reproducible calibration parameter for its non-Gaussian null law. This is not an arbitrary parameter slice, an unmotivated finite table, or a rerun of the already-published first four cumulants. Exact rational computation is particularly useful because it converts an operator approximation into an infinite-dimensional theorem.

## Scope and residual limitations
The result applies to the fully specified, continuous simple null only. It does not settle the fitted-parameter case, calculate all eigenvalues, or determine full finite-sample critical values. No independent mathematical audit has yet been performed.

Self-review: passed. Independent audit: not yet performed.
