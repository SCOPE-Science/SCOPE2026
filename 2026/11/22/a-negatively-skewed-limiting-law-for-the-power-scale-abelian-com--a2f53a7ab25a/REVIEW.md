# Scientific self-review

## Correctness — PASS
The claim has been reconstructed from definitions of the digit-three counter, Abelian factor complexity, and phase normalization. The published exact recurrence at powers of four yields the exact continuous phase identity, not an asymptotic guess. The Fourier coefficient computation is an elementary piecewise-cosine integral, and Parseval yields the positive variance series. The negative third centered moment is bounded by an explicit finite midpoint quadrature with a proved Lipschitz error, a uniformly bounded tail, and high-precision evaluation; no finite experiment is used to assert an infinite combinatorial statement. Independent substring counting over every occurring adjacent-block pair agrees with six exact small exponents. The package contains its executable checker and results. The third moment's sign is rigorous at the stated wide precision, not certified to all reported decimal digits.

## Originality — PASS relative to inspected literature
The 2026-10-02 Allouche--Rampersad--Rigo--Shallit--Stipulanti article proves the underlying recurrence, phase irrationality, and nonregularity, not an empirical law, exact mean/variance, or a negative centered third moment. The closely relevant 2026-10-26 published published-finding corpus family explicitly gives phase functions and intervals for exponents at least four; its full RESULT was read. That prior result can motivate the phase representation for exponent three and is *not* claimed as new. The new claim concerns the exact probability distribution and non-symmetric shape of the original exponent-three example, backed by the Fourier moment formula and the signed error certificate. The 2026-11-02 extension proves nonregularity for other exponents, not the statistical law. Searched aliases include normalized power-length complexity, Fourier phase waveforms, higher central moments, negative skewness, and the original arXiv identifier. Undiscovered papers and a routine-method overlap risk remain; absence of indexed matches is not absolute priority proof.

## Value — PASS
The original breakthrough proves a binary automatic word has nonregular Abelian complexity, while prior phase analysis for related examples supplies possible accumulation values. This result quantifies how often normalized complexity visits those values under the natural uniform-log-length sampling and distinguishes the shape from a symmetric fluctuation by a certified signed third moment. The mean, variance and entire pushforward law are exact and usable for calibrated statistical comparison of power-scale complexity, not an arbitrarily chosen finite slice. It does not purport to solve complexity at all lengths.

## Closest sources and limits
- Allouche et al., arXiv:2610.03837, 2026-10-02; its Sections 2–4 were read in full.
- published-finding corpus record `7b09e62adf22`, 2026-10-26; entire public RESULT.md read.
- published-finding corpus record `f292807a24e1`, 2026-11-02; mathematical theorem, assumptions and initial proof excerpt read.
- Broader background: Couvreur et al., arXiv:2504.13584.

Residual risks: unindexed equivalent moment computations, possible alternative standard derivations of the same law, and no classification of the law's absolute continuity or exact endpoint constants. The numerical check has a wide explicit error bound. The scope is only the powers \(4^m\).

Self-review: passed. Independent audit: not yet performed.
