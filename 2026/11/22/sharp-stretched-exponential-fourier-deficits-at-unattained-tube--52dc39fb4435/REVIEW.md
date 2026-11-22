# Scientific assessment

## Correctness

**PASS.** The construction is translation bounded and has the explicitly summable Poisson-series transform. The general logarithmic asymptotic follows from a continuous saddle point and a discretization lemma with a uniform polynomial counting error. The lower bound at integer frequencies is positive, independent of signs from shared dyadic frequencies. In the quadratic specialization, a complete-cell Fourier character annihilates all frozen-level contributions except the saddle-level term, with the freezing error of relative size \(o(1)\) and the reverse exponential branch negligible. This proves the claimed global two-sided \(O(1)\) remainder for every sufficiently large real frequency, not just integers. The finite checker supplied alongside the proof verifies 242 supplementary assertions; the proof supplies the infinite quantifiers.

## Originality

**PASS relative to the inspected material, with residual bibliographic risk.** Değer and Favorov, *Analogs of crystalline measures in tube sets* (arXiv:2611.16506v1, §3), already construct arbitrary summably weighted dyadic shifted lattices with heights approaching an unattained strip boundary and derive their exact transform formula. They establish qualitative \(o(e^{2\pi|t|})\) local variation, not the sharp tunable exponent, coefficient, or uniform bounded-error law here. Favorov and Değer, *Some properties of Fourier quasicrystals and measures on a strip* (arXiv:2605.10766v1), give general exponential-growth bounds, not a matching local deficit asymptotic. The bounded-remainder result has an additional cancellation issue resolved by the frequency-cell selector, which is not a consequence of the prior qualitative bound alone. Semantic searches of published research summaries found no same-object matching assertion. Unindexed or differently named prior saddle estimates remain possible.

## Value

**PASS.** The support-function bound \(e^{2\pi|t|}\) is natural in the theory of complex tube Fourier transforms. The present finding explains quantitatively how an unattained boundary can force a continuum of exact fractional-growth deficits, while the quadratic case establishes a genuinely matching global two-sided exponential envelope. The dyadic character-selection argument is a usable technique for handling cancellation from an infinite accumulation of frequency lattices. The work does not assert a universal law for all tube measures or determine the quadratic model's bounded oscillatory prefactor.

## Closest sources and limitations

- Değer and Favorov, arXiv:2611.16506v1, §3, exact underlying measure architecture and transform, but only qualitative decay from the boundary exponential.
- Favorov and Değer, arXiv:2605.10766v1, exponential-type comparison, without the claimed sharp local asymptotic.
- The finite computational checks do not establish the infinite or continuous-frequency results, and the possibility of an equivalent unindexed theorem is not eliminated by search alone.

Self-review: passed. Independent audit: not yet performed.
