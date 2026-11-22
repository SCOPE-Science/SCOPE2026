# Scientific review

## Correctness: PASS

The claim is universal over \(L<U\), \(c>0\), \(\mu\le L\), and all \(A\ge0\) for the specified piecewise parabolic response. Analytic differentiation in the cold-truncated regime gives the exact stationarity equation; its left side is strictly increasing on \((0,\pi/2)\). The stationary point lies strictly before the hot cutoff, after which a strictly decreasing integral kernel proves no second optimum. The boundary \(\mu=L\) is handled separately. A factorized derivative proves the sharp universal warmest-temperature bounds and both endpoint limits. The supplied standalone code independently compares sine quadrature against closed formulas across 1,835 checks; it is not substituted for the universal proof.

## Originality: PASS, provisionally

The primary literature on sine-wave degree-day accumulation, quadratic growth-versus-amplitude regression, Jensen effects on thermal performance, and preferred *mean* temperature under varying climate does not directly state or imply the exact all-offset optimizer or universal \(2/\pi\)-to-\(3/4\) warmest-temperature law for the specified model. The nearest known work is Baskerville and Emin (1969), Tian and Dong (2006), Martin and Huey (2008), Folguera et al. (2009), and Estay et al. (2014). The last was inspected in an open complete article; Martin and Huey's full published article and article-length transcriptions of Tian and Dong/Folguera were also examined. Baskerville and Emin were accessible by abstract and bibliographic details only. Allen (1976), a modified sine degree-day calculation, was not available in full, so its comparison is a named historical-priority risk rather than a whole-paper exclusion. The conclusion is relative to inspected evidence, not a priority guarantee.

## Value: PASS

The cold-mean case is where degree-day models predict no development from the mean alone, yet warm intervals can generate development. Increasing diurnal variability has competing cold-rescue and hot-dilution effects. The theorem proves a **single**, not merely experimentally suggested, turnover and a universal strict safe-side location of the best day's maximum below upper thermal cutoff, with exact sharp constants independent of the cold offset. That provides an interpretable benchmark and a stress test for idealized rate-summation simulations; it is stronger than just calculating a sinusoidal integral or plotting one parameter case. It does not justify operational thermal management for real organisms without measured response curves and exposure physiology.

## Closest literature and limitations

Relevant references and exact distinctions appear in RESULT.md. Real thermal performance can be skewed, temperature cycles may not be sinusoidal, and exposure can induce biological memory or damage. These departures can invalidate the sharp bound. Priority comparisons are incomplete for inaccessible older complete papers.

Self-review: passed. Independent audit: not yet performed.
