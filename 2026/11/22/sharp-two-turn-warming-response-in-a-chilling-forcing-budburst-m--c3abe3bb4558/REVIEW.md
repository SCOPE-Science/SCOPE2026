# Scientific review: sharp two-turn warming response in a chilling–forcing budburst model

## Correctness — PASS

The claim is restricted to the explicit exponential forcing requirement and quadratic cold-exposure curve in RESULT.md. Reconstructing its derivative reduces every turning point to intersections of a nonnegative function \(R(x;b,h)\) with level one. Its logarithmic derivative has exactly one zero, because \(x^2(1-s/2)\) increases strictly from zero to infinity. The tangency conditions eliminate to \(v^2=v+2h\), yielding the stated unique threshold. Critical point sign order, equality, the continuation at the chilling boundary, and the square-root splitting follow analytically. Exact symbolic simplification of the local Taylor coefficients agrees with the proof; the supplied numerical checker passed 11,288 supplemental assertions. No finite numerical check is treated as a proof of uniqueness.

## Originality — PASS (provisional)

The exact quadratic cold-exposure / linear-spring-ramp phase diagram is not identified in the primary sources inspected. Cannell and Smith (1983) supply the historical exponential chilling–forcing relation, and Cannell and Smith (1986) establish the possibility of advance or delay, but neither accessible abstract states this exact two-turn threshold. Full-text model-comparison studies by Chuine, Cour and Rousseau (1999) and Fu et al. (2012) discuss chilling and forcing functions, calibration, and climatic responses, rather than the sharp boundary \(b_c(h)\) or the square-root birth of two turning points. Searches for two-turn and nonmonotone budburst thresholds found no exact dominating theorem. This is evidence of noncoverage in the inspected materials, not a proof of historical novelty. The original 1983 full text was inaccessible and remains a priority risk.

## Value — PASS

The phase diagram sharply separates models that always predict advancing budburst under warming from models capable of an intermediate *delay window*, and bounds the response to two turns. The explicit threshold, monotonic baseline dependence, and square-root onset furnish reproducible benchmarks for sensitivity testing in a historically motivated chilling–forcing model. The finite triangular winter interpretation shows that both reversals need not rely solely on offsets beyond a real winter interval. The result is a mathematical benchmark, not an observation or calibrated species forecast; simple calculus alone is not taken as proof of biological significance.

## Closest literature and remaining limitations

- Cannell and Smith, *Thermal Time, Chill Days and Prediction of Budburst in Picea sitchensis* (1983), DOI 10.2307/2403139: empirical exponential heat/chill relation; only the abstract/bibliographic record accessible.
- Cannell and Smith, *Climatic Warming, Spring Budburst and Frost Damage on Trees* (1986), DOI 10.2307/2403090: qualitative warming advance/delay mechanism; abstract accessible.
- Chuine, Cour and Rousseau, *Selecting models to predict the timing of flowering of temperate trees* (1999), DOI 10.1046/j.1365-3040.1999.00395.x: alternative physiological response models, full HTML inspected.
- Fu et al., *The Impact of Winter and Spring Temperatures on Temperate Tree Budburst Dates* (2012), DOI 10.1371/journal.pone.0047324: full open text inspected; field calibration and broader weather effects remain outside the theorem.

The biological chilling law, thermal ramp, and cold-margin continuation are idealized and may not remain valid under large climate changes. No general result for empirical temperature time series, photoperiod constraints, or individual trees is claimed. A comparable closed-form theorem in incompletely accessible historical work cannot be ruled out.

Self-review: passed. Independent audit: not yet performed.
