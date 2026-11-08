# Review of the Laplace-window two-tone ridge theorem

## Correctness — PASS
The proof starts from the explicit Fourier transform of \(e^{-a|s|}\) and derives a rational positive-denominator profile for every \(a>0\), \(\omega>0\), time and real angular frequency. The critical derivative is a cubic in squared normalized frequency. Its quadratic coefficient is always negative, its leading coefficient is nonpositive, and its constant term changes sign exactly at \((\omega/a)^2=(1+c)/(5+c)\), with \(c=\cos(2\omega x)\). When the constant is nonpositive, an explicit inequality makes every derivative coefficient nonpositive; when it is positive, Descartes' rule and the intermediate-value theorem give one simple positive root and no others. The boundary is quartically flat and the beat-phase fraction is an elementary exact measure. Symbolic identities and numerical quadrature/root checks are independently replayable; finite tests do not establish the universal statement.

## Originality — PASS relative to inspected evidence
Chand–Nolen–Wu, arXiv:2601.10910 (first posted January 15, 2026), treat the two-tone STFT with a Gaussian window. Their accessible abstract describes bifurcating frequency ridges and bubbles, but does not give the present Laplace/Lorentzian phase diagram, exact root count or arccosine duty law. Iatsenko–McClintock–Stefanovska (2016) study ridge extraction procedures, not this precise classification. Queries for Laplace STFT, Lorentzian/Cauchy doublet peaks, coherent two-tone interference and the exact threshold returned no stronger accessible published claim. Search misses are not novelty proofs. The full 2026 source could not be inspected; an unadvertised general-window lemma there, or an older spectroscopy calculation, remains a priority risk. See the structured comparisons in `AUDIT.json`.

## Value — PASS
Spectrogram ridges are a natural measure of whether two Fourier components can be visually separated. The sharp threshold, the proof that no third ridge can appear, the on/off time fraction and the square-root splitting quantify how a non-Gaussian window resolves close frequencies. This supplies a structurally exact benchmark rather than a routine approximate plot. Applicability is restricted to equal-amplitude stationary tones, the two-sided exponential window and the raw STFT.

Self-review: passed. Independent audit: not yet performed.
