# Self-review

## Correctness — PASS
The Gaussian-STFT calculation is exact and normalization is explicit: a positive rescaling balances the independent endpoint coefficient variances. Rouché's theorem is applied only on the unit circle, which almost surely contains no zero, and the direct identity \(\overline C P-A P^*=u(D+du)\) handles both signs of the endpoint modulus difference. The iid circular Gaussian orthogonalization gives \(T\sim N(0,1)\), independent of middle Rayleigh amplitude, and its scalar Laplace transform gives \(q_\beta\). The polynomial has exactly two simple nonzero roots almost surely, and each corresponds to one zero per temporal period. The bundled independent direct-root checker passed 451,910 finite comparisons; these corroborate rather than prove the all-parameter claim.

## Originality — PASS relative to inspected evidence
The closest fully inspected result, *Exact modal bifurcation of three-line Gaussian spectrogram zeros*, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-modal-bifurcation-of-three-line-gaussian-spectrogram-zeros--106a484313d3/RESULT.md, establishes the expected one-point intensity and its threshold \(\beta=4\), but does not compute the random 0/1/2 zero-count distribution. The fully inspected two-line zero-count result, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-zero-count-laws-and-non-self-averaging-for-two-line-gaussi--6079d35cb6de/RESULT.md, concerns one zero per temporal period. The motivating source [1] has an accessible abstract focused on expected intensity and spectrum recovery, not the asserted three-point count. General random-Gaussian-polynomial zero statistics in [4] are potentially relevant, and an older equivalent count formula cannot be excluded because the full source was inaccessible. The new result does not claim the shared random polynomial reduction itself to be original.

## Mathematical value — PASS
One-point zero intensity does not determine finite-window count fluctuations: the count expectation here is always one, whereas the variance runs through the entire interval \((0,1)\) according to an exact formula. The spectral symmetry balance frequency is intrinsic rather than arbitrarily chosen. The smooth count law contrasted with the sharp modality threshold distinguishes two natural observables of a three-line spectrogram. This is a motivated complete classification of an exact second-order statistical invariant, not just a numerical parameter evaluation.

## Limitations and publication priority
Equal frequency spacings and independent circular Gaussian line amplitudes are essential. This calculation does not address four spectral lines or broadband spectra. The complete texts of the motivating 2026 paper and the older Forrester–Honner source could not be inspected, so a priority risk remains. Independent validation is not claimed.

Self-review: passed. Independent audit: not yet performed.
