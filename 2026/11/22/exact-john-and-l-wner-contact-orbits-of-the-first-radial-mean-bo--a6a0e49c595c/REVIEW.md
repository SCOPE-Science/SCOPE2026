# Independent mathematical audit

## correctness

PASS

With the positive-ray Gardner–Zhang normalization, Fubini gives the normalized cube covariogram integral. Sort by largest absolute coordinate and use [0,1]^2 ratios s,t; integrating (1-z)(1-sz)(1-tz) on [0,1] gives H/6, H=sqrt(S)D for S=1+s²+t², D=6−2s−2t+st. The scaled derivatives have difference (s−t)(D−S); D−S decreases in both ratios and vanishes only at (1,1), so interior stationarity is diagonal. Its derivative numerator factors as (1−s)^2(3s−2), giving the only interior candidate (2/3,2/3) with H²=19652/729. On a zero edge the derivative numerator is −2(2t−1)(t−1), yielding candidate squared values 36, 125/4 and 32 including endpoints. On a unit edge the numerator is −2(t−1)^2, yielding endpoint squared values 32 and 27. Hence the interior minimum is strict, with gap 31/729 below the body diagonal, and (0,0) is the only reduced maximum. Convexity at this positive parameter and uniqueness of John and Löwner ellipsoids imply cubic invariance: reflections force zero center and a diagonal form, permutations make that form scalar. Thus extremizing the radial function gives both radii and exactly 3·8 inner and 3·2 outer contacts. The result fixes [-1,1]^3 at p=1; no general p or dimensions are treated. The analytic proof is exhaustive over directions; verify.py was inspected, not executed.

## originality

PASS

Pass the global three-dimensional radial extrema and full contact orbits, not the generally known radial integral or the axis and body-diagonal evaluations. The exact oblique minimizer requires a global two-variable calculation not provided by the strongest inspected sources.

## value

PASS

John and Löwner contacts are canonical geometric data for a fundamental radial-mean test body. Exact oblique equality points disprove the natural axis/diagonal guess and quantify a small but strict body-diagonal gap. This all-direction comparison is useful for sharp geometric bounds and is not simply the evaluation of a known formula at preassigned directions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
