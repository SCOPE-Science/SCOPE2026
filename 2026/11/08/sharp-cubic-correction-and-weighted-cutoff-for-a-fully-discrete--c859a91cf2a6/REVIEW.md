# Review: sharp cubic correction for the fully discrete Hilbert kernel

## Correctness

**PASS (self-review).** The defining Fourier integral and kernel normalization match the accessible primary source. The proof derives endpoint derivatives and reflection, controls the seventh-order remainder, obtains a sharp two-sided asymptotic, and uses the nonzero leading coefficient for both summability and divergence. The endpoint convolution norm identities are exact. The finite reproducibility script is supplementary, not a proof.

## Originality

**PASS relative to inspected evidence.** Petrov's original Section 4.2 proves only the quadratic-order upper estimate and unweighted summability; this result computes two nonzero sharp coefficients, the precise weighted threshold, and the endpoint truncation constant. The nearest mathematical-record results concern finite cyclic Hilbert kernels, which are different operators. Equivalent results in older Fourier-kernel asymptotic literature remain a possibility and independent priority has not been established.

## Value

**PASS.** The correction is the exact operator-level discrepancy between a new discrete boundary Hilbert transform and its classical half-shift counterpart. Its sharp tail replaces a non-sharp first-order truncation rate by a second-order one and identifies the exact weighted moment cutoff needed for local weighted convolution estimates. The problem is intrinsically tied to approximating this natural kernel, not an arbitrary numeric instance.

## Limits and literature

The theorem is one-dimensional, does not give sharp intermediate \(\ell^p\) truncation norms, and does not automatically transfer to other transforms. Closest source: Petrov (2025 preprint / 2026 journal), Section 4.2, Lemma 4.2; earlier semi-discrete context: Ciaurri and collaborators (2017). Independent mathematical and priority audits remain outstanding.

Self-review: passed. Independent audit: not yet performed.
