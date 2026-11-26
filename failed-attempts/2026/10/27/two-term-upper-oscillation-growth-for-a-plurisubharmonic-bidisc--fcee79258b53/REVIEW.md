# Independent mathematical audit

## correctness

PASS

The log-radius expression is convex and coordinatewise increasing: the positive square root before negation is the concave geometric mean of the two positive linear forms A' + B' and B', where A' and B' are negative log radii. This gives plurisubharmonicity off the axes, and the upper-semicontinuous extension is −∞ on the axes. Normalized product area gives independent rate-2 exponentials X,Y, so the boundary supremum and the integrable average give UO = E[sqrt((A+B+X+Y)(B+Y))] − sqrt((A+B)B). For S=B+X+Y, the absolute error of replacing sqrt(1+S/A) by 1+S/(2A) is at most S²/(8A²), globally, not only on bounded radii. The moment times sqrt(B+Y) is finite; the boundary term satisfies the same estimate. The first coefficient is E[sqrt(B+Y)]−sqrt(B)>0, and the second is (1/2)E[(B+Y)^(3/2)] + (1/4)E[(B+Y)^(1/2)]−B^(3/2)/2. The rate-2 incomplete-gamma moments give both displayed constants and the claimed error. This is an analytic check for fixed B>0, not a claim of uniformity in B. The frozen verification notes give the same analytic ingredients; no numerical certification is needed.

## originality

FAIL

Chen–Wang do not print the coefficients, but Lemma 3.7 already gives the exact normalized oscillation for this same function and arbitrary interior radii. A direct Taylor expansion in that specific integral, with the elementary exponential moment bound, yields both coefficients and the exact order of the error. This is demonstrated prior implication, not merely the observation that the divergence was known or a failure to find literature.

## value

FAIL

The example and growth question are natural, but for this precise one-parameter slice the prior paper already furnishes the specialized exact oscillation integral. The two coefficients follow by an ordinary Taylor expansion and elementary moments, with no further quantitative obstruction, varying-radius estimate or other distinct mathematical result. The Finding is thus a correct explanatory calculation, not a surviving valuable new invariant under the non-mechanical requirement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
