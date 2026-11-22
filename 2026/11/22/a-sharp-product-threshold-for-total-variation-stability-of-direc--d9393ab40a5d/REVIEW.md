# Self-review

**Correctness — PASS.** An exact edge-increment representation gives nonnegative coefficients under \(ab\le1\), with column sums that yield the full finite-path dissipation identity. The converse uses a six-value monotone profile and the specified fast-tail hypothesis to force a negative output edge for every \(ab>1\). Exact rational checks replay the argument on examples. The proof does not conflate one-input variation decrease with two-input nonexpansivity.

**Originality — PASS, qualified.** Harten (1983, Lemma 2.2) supplies the generic sufficient incremental-form criterion and is explicitly acknowledged as covering that method. Tomasi–Manduchi (1998), Pianykh (2010), and Galiano–Velasco (2015) provide the bilateral-filter definition, performance analysis and rearrangement formulation, respectively; the inspected material does not give the *if and only if* directed product threshold, six-point failure witness or the finite-path exact dissipation identity. The sharp necessity is not a consequence of Harten's one-way lemma. Risk: some specialized edge-aware signal-processing papers remain uninspected, so independent priority confirmation is pending.

**Mathematical value — PASS.** The exact geometric-mean boundary for asymmetric left/right smoothing weights is a complete stability classification for a natural finite-path nonlinear filter family, uniform over Gaussian and many non-Gaussian range affinities. It identifies precisely when filtering can create an oscillation from monotone data and provides a computable nonnegative variation-loss decomposition. This matters for repeated smoothing and designing directional local filters; no claim is made for general image filters or for two-input Lipschitz coefficients.

## Scope and closest literature

Harten's coefficient criterion dominates the elementary sufficient direction, but not the necessary converse under fast affinity decay. The foundational bilateral-filter sources analyze definitions, noise-response metrics and rearrangement algorithms rather than this exact variation dichotomy. The original 1998 conference PDF was not independently replayed page by page; the accessible historical HTML version and the original IEEE bibliographic entry were examined, alongside the two arXiv full texts and Harten's available full-text transcription. This access limitation is a historical-priority risk, not a correctness dependency.

Self-review: passed. Independent audit: not yet performed.
